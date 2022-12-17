import bpy
file_loc = "G:/3_semester_projekt_final/Blender_conversion/files/texturedMesh.obj"
file_des = "G:/3_semester_projekt_final/Game/roaming-ralph/models/ralph.egg"
#imported_object = bpy.ops.import_scene.obj(filepath=file_loc)
imported_object = bpy.ops.wm.obj_import(filepath=file_loc)
obj_object = bpy.context.selected_objects[0]
print('Imported name: ', obj_object.name)
bpy.ops.export.panda3d_egg(filepath=file_des)