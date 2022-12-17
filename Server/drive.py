from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from datetime import datetime
from time import sleep
import os 

# Establish connection 
gauth = GoogleAuth()
gauth.LoadCredentialsFile("credentials.txt")
if gauth.credentials is None:
    # Authenticate if they're not there
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    # Refresh them if expired
    gauth.Refresh()
else:
    # Initialize the saved creds
    gauth.Authorize()
# Save the current credentials to a file
gauth.SaveCredentialsFile("credentials.txt")

# drive object created with the established
drive = GoogleDrive(gauth)

def download_files():
    path = f"{os.getcwd()}/billeder"
    os.chdir(path)
    folder_id = get_folder_id("Uploads") 
    file_list = drive.ListFile({"q": f"'{folder_id}' in parents and trashed=false"}).GetList()
    for file in file_list:
        print("title: %s, id: %s" % (file["title"], file["id"]))
        file.GetContentFile(file['title'])

def backup(path):
    folder_id = get_folder_id("Backup")
    for x in os.listdir(path):
        print(f"Uploading {x}")
        #f = drive.CreateFile({'title': x})
        f = drive.CreateFile({'title': x, 'parents': [{'id': folder_id }]})
        f.SetContentFile(os.path.join(path, x))
        f.Upload()

        f = None
    delete_used()

def delete_used():
    folder_id = get_folder_id("Uploads") 
    file_list = drive.ListFile({"q": f"'{folder_id}' in parents and trashed=false"}).GetList()
    for file in file_list:
        print("Deleting title: %s, id: %s" % (file["title"], file["id"]))
        file.Delete()

# Function defined for finding the folder ID for a folder with a given name ## Problems occur with duplicates 
def get_folder_id(folder_name : str):
    fileList = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
    fileID = ""
    for file in fileList:
        print('Title: %s, ID: %s' % (file['title'], file['id']))
    # Get the folder ID that you want
        if(file['title'] == folder_name):
            fileID = file['id']
    sleep(1)
    print(f"Retuning the folder ID: {fileID}")
    return fileID

# Define function for folder creation on the google drive 
def create_folder(folder_name : str):
    folder = drive.CreateFile({'title' : folder_name, 'mimeType' : 'application/vnd.google-apps.folder'})
    folder.Upload()