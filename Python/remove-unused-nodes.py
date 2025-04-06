import bpy
# Loop through all node groups and delete those not in use
for node_group in bpy.data.node_groups:
    if len(node_group.users) == 0:
        bpy.data.node_groups.remove(node_group)
