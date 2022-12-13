import numpy
import os
import shutil
parent_path = os.getcwd()
image_path = f"{parent_path}/Billeder"
cache_path = f"{parent_path}/Intimediary_files"
meshroom_path = f"{parent_path}/Meshroom-2021.1.0/meshroom_batch"
output_path = f"{parent_path}/Blender_conversion/files"
blender_path = f"{parent_path}/Blender Foundation/Blender 3.3"
blender_file_des = f"{parent_path}/Game/roaming-ralph/models/ralph.egg"
texture_file_des = f"{parent_path}/Game/roaming-ralph/models/tex"
try:
    for f in os.listdir(cache_path):
        shutil.rmtree(os.path.join(cache_path, f))
except OSError as e:
    print("Error: %s : %s" % (cache_path, e.strerror))
for f in os.listdir(output_path):
    os.remove(os.path.join(output_path, f))

cmdLine = f"{meshroom_path} --input {image_path} --cache {cache_path} --output {output_path} --pipeline photogrammetry --forceCompute"
os.system(cmdLine)
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
