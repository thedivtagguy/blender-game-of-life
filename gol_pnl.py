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
        
        layout.label(text="Procedural Generator")

        # 2 Columns with buttons
        row = layout.row()
        col = row.column()
        col.operator("gol.start", text="Start")
        col.operator("gol.spawn", text="Fill Grid")

        col = row.column()
        col.operator("gol.stop", text="Stop")