import bpy
for material in bpy.data.materials:
    if material.users == 0:
        bpy.data.materials.remove(material)
