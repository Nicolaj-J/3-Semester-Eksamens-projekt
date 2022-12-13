import numpy
import os
import shutil
import datetime
date = datetime.datetime.now()
import drive
parent_path = os.getcwd()
image_path = f"{parent_path}/Billeder"
cache_path = f"{parent_path}/Intimediary_files"
meshroom_path = f"{parent_path}/Meshroom-2021.1.0/meshroom_batch"
output_path = f"{parent_path}/Blender_conversion/files"
blender_path = f"{parent_path}/Blender Foundation/Blender 3.3"
blender_file_des = f"{parent_path}/Game/roaming-ralph/models/ralph.egg"
texture_file_des = f"{parent_path}/Game/roaming-ralph/models/tex"
model_path = f"{parent_path}/models"
zipped_models = f"{model_path}/Zipped"
try:
    for f in os.listdir(cache_path):
        shutil.rmtree(os.path.join(cache_path, f))
except OSError as e:
    print("Error: %s : %s" % (cache_path, e.strerror))
for f in os.listdir(output_path):
    os.remove(os.path.join(output_path, f))
drive.downlaod_files()
model_name = f"Model_{date.day}-{date.month}-{date.year}_{date.hour}-{date.minute}"
zip_folder = f"{model_path}/{model_name}"
os.mkdir(zip_folder)
shutil.copytree(image_path,f"{zip_folder}/images")
cmdLine = f"{meshroom_path} --input {image_path} --cache {cache_path} --output {output_path} --pipeline photogrammetry --forceCompute"
os.system(cmdLine)
for i in os.listdir(image_path):
    os.remove(f"{image_path}/{i}")
shutil.copytree(output_path,f"{zip_folder}/Mesh")
try:
    os.remove(blender_file_des)
except:
    pass

try:
    for f in os.listdir(texture_file_des):
        shutil.rmtree(os.path.join(texture_file_des, f))
    os.remove(texture_file_des)
except OSError as e:
    print("Error: %s : %s" % (texture_file_des, e.strerror))


os.chdir(blender_path)
cmdLine = f"blender -b --python G:/3_semester_projekt_final/Blender_automation.py"
os.system(cmdLine)
shutil.copy(blender_file_des, f"{zip_folder}/ralph.egg")
shutil.make_archive(f"{zipped_models}/{model_name}", 'zip', zip_folder)
drive.backup(f"{zipped_models}")
try:
    for f in os.listdir(zipped_models):
        os.remove(f"{zipped_models}/{f}")
except OSError as e:
    print("Error: %s : %s" % (zipped_models, e.strerror))