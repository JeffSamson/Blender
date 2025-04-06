import bpy

# Loop through all node groups and delete those not in use
for node_group in bpy.data.node_groups:
    if node_group.users == 0:  # Directly compare users to 0
        bpy.data.node_groups.remove(node_group)
