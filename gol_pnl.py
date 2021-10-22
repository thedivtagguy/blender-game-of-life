import bpy

from bpy.types import Panel

class GOL_PT_Panel(Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = "Game of Life"
    bl_category = "Game of Life"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        
        # Heading
        layout.label(text="Procedural Generator", icon='MESH_CUBE')
        # 2 Columns with buttons
        row = layout.row()
        col = row.column()
        # Seperator
        col.separator()
        # Description text
        col.label(text="1. Turn on seeding mode")
        col.operator("gol.seeder", text="Seeder")
        col.separator()
        col.label(text="2. Generate the Grid")
        col.operator("gol.spawn", text="Fill")
        row = layout.row()
        col = row.column()
        col.separator()
        col.label(text="Add Scene Camera", icon="CAMERA_DATA")
        col.operator("gol.camera", text="Add Camera")
