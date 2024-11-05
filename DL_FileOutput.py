# -----------------------------------------------------------------------------------
#  DL_FileOutput [Blender]
#  Version: v01.0
#  Author: Danilo de Lucio
#  Website: www.danilodelucio.com
#  Created Date: 31/Oct/2024
#  Last update: 05/Nov/2024
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
#  [Summary]
#  This addon creates a File Output node and sets the AOV names automatically.
#  Blender version: 4.1.0
# -----------------------------------------------------------------------------------

bl_info = {
    "name": "DL_FileOutput",
    "author": "Danilo de Lucio",
    "version": (1, 0),
    "blender": (4, 1, 0),
    "location": "Compositor > DL FileOutput",
    "description": "Creates an Output File node and sets all the AOV names automatically.",
    "warning": "",
    "doc_url": "https://github.com/danilodelucio/DL_FileOutput_for_Blender",
    "category": "DL FileOutput",
}


import bpy


TOOL_NAME = "DL FileOutput"


# Main Class
class DL_FileOutput:
    def __init__(self) -> None:
        self.eevee_engine = "BLENDER_EEVEE"
        self.cycles_engine = "CYCLES"

        scene = bpy.context.scene
        scene.use_nodes = True

        self.render_engine = scene.render.engine
        self.nodes = scene.node_tree.nodes
        self.links = scene.node_tree.links
        self.tree = bpy.context.scene.node_tree

        # Selected Render Layer node
        self.selected_RenderLayer_node = bpy.context.scene.node_tree.nodes.active

        if self.selected_RenderLayer_node and self.selected_RenderLayer_node.type == 'R_LAYERS':
            print(f"\nRunning {TOOL_NAME} setup...")
            print("- Render engine: ", scene.render.engine)

            self.renderLayer_location = self.selected_RenderLayer_node.location
        
        else:
            self.error_msg()
            return

    def enable_passes(self) -> None:
        current_viewLayer = bpy.context.view_layer
        current_renderEngine = bpy.context.scene.render.engine

        current_viewLayer.use_pass_combined = True

        # CYCLES ###################################################
        if current_renderEngine == self.cycles_engine:
            # Diffuse
            current_viewLayer.use_pass_diffuse_direct = True
            current_viewLayer.use_pass_diffuse_indirect = True
            current_viewLayer.use_pass_diffuse_color = True

            # Glossy
            current_viewLayer.use_pass_glossy_direct = True
            current_viewLayer.use_pass_glossy_indirect = True
            current_viewLayer.use_pass_glossy_color = True

            # Transmission
            current_viewLayer.use_pass_transmission_direct = True
            current_viewLayer.use_pass_transmission_indirect = True
            current_viewLayer.use_pass_transmission_color = True

            # Volume
            current_viewLayer.cycles.use_pass_volume_direct = True
            current_viewLayer.cycles.use_pass_volume_indirect = True

            # Other passes
            current_viewLayer.use_pass_emit = True
            current_viewLayer.use_pass_environment = True

        #  EEVEE ###################################################
        elif current_renderEngine == self.eevee_engine:
            # Diffuse
            current_viewLayer.use_pass_diffuse_direct = True
            current_viewLayer.use_pass_diffuse_color = True

            # Specular
            current_viewLayer.use_pass_glossy_direct = True
            current_viewLayer.use_pass_glossy_color = True
            
            # Other passes
            current_viewLayer.use_pass_emit = True
            current_viewLayer.use_pass_environment = True
            current_viewLayer.eevee.use_pass_volume_direct = True
            # current_viewLayer.eevee.use_pass_bloom = True

    def create_FileOutput_node(self, incr_x, incr_y):
        # Adding File Output node
        output_file_node = self.nodes.new(type='CompositorNodeOutputFile')
        output_file_node.location = self.renderLayer_location[0] + incr_x, self.renderLayer_location[1] + incr_y

        # Setting the file path
        output_file_node.base_path = "//output/"

        # Setting all the main info
        output_file_node.name = TOOL_NAME
        output_file_node.label = TOOL_NAME

        output_file_node.format.file_format = 'OPEN_EXR_MULTILAYER'
        output_file_node.use_custom_color = True
        output_file_node.color = (0.227267, 0.0768554, 0.116828)

        output_file_node.file_slots.clear()

        return output_file_node

    def aov_standard(self):
        if self.selected_RenderLayer_node and self.selected_RenderLayer_node.type == 'R_LAYERS':
            output_file_node = self.create_FileOutput_node(700, 0)
            self.create_slots_OutputFile(output_file_node, self.final_passes())

            self.clear_selection()
        
        else:
            self.error_msg()
            
        print("- AOV Standard Setup has been completed!")
        return

    def aov_compact(self):
        if self.selected_RenderLayer_node and self.selected_RenderLayer_node.type == 'R_LAYERS':
            self.enable_passes()

            # Creating File Output node
            output_file_node = self.create_FileOutput_node(1100, 0)
            self.create_slots_OutputFile(output_file_node, self.combined_passes())

            # CYCLES
            if self.render_engine == self.cycles_engine:
                # ADDING COLOR MIX (ADD) ###########################################
                diffuse_light = self.create_colorMix_node("diffuse_light", 400, 70, "ADD")
                self.link_nodes(self.renderLayer_output("DiffDir"), diffuse_light.inputs[1])
                self.link_nodes(self.renderLayer_output("DiffInd"), diffuse_light.inputs[2])

                reflection_total = self.create_colorMix_node("reflection_light", 400, 140, "ADD")
                self.link_nodes(self.renderLayer_output("GlossDir"), reflection_total.inputs[1])
                self.link_nodes(self.renderLayer_output("GlossInd"), reflection_total.inputs[2])

                refraction_total = self.create_colorMix_node("refraction_light", 400, 200, "ADD")
                self.link_nodes(self.renderLayer_output("TransDir"), refraction_total.inputs[1])
                self.link_nodes(self.renderLayer_output("TransInd"), refraction_total.inputs[2])

                volume = self.create_colorMix_node("volume", 400, 270, "ADD")
                self.link_nodes(self.renderLayer_output("VolumeDir"), volume.inputs[1])
                self.link_nodes(self.renderLayer_output("VolumeInd"), volume.inputs[2])

                # ADDING COLOR MIX (MULTIPLY) #########################################
                reflection = self.create_colorMix_node("reflection", 600, 160, "MULTIPLY")
                self.link_nodes(reflection_total.outputs[0], reflection.inputs[1])
                self.link_nodes(self.renderLayer_output("GlossCol"), reflection.inputs[2])

                refraction = self.create_colorMix_node("refraction", 600, 210, "MULTIPLY")
                self.link_nodes(refraction_total.outputs[0], refraction.inputs[1])
                self.link_nodes(self.renderLayer_output("TransCol"), refraction.inputs[2])

                # Linking all Mix nodes to File Output node
                self.link_nodes(self.renderLayer_output("DiffCol"), output_file_node.inputs["diffuse_albedo"])
                self.link_nodes(diffuse_light.outputs[0], output_file_node.inputs["diffuse_light"])
                self.link_nodes(reflection.outputs[0], output_file_node.inputs["reflection"])
                self.link_nodes(refraction.outputs[0], output_file_node.inputs["refraction"])
                self.link_nodes(volume.outputs[0], output_file_node.inputs["volume"])
            
            # EEVEE
            elif self.render_engine == self.eevee_engine:
                # ADDING COLOR MIX (MULTIPLY) #########################################
                reflection = self.create_colorMix_node("reflection", 600, 160, "MULTIPLY")
                self.link_nodes(self.renderLayer_output("GlossDir"), reflection.inputs[1])
                self.link_nodes(self.renderLayer_output("GlossCol"), reflection.inputs[2])

                # Linking all Mix nodes to File Output node
                self.link_nodes(self.renderLayer_output("DiffDir"), output_file_node.inputs["diffuse_light"])
                self.link_nodes(self.renderLayer_output("DiffCol"), output_file_node.inputs["diffuse_albedo"])
                self.link_nodes(reflection.outputs[0], output_file_node.inputs["reflection"])
                self.link_nodes(self.renderLayer_output("VolumeDir"), output_file_node.inputs["volume"])

            self.clear_selection()
        
        else:
            self.error_msg()

        print("- AOV Compact Setup has been completed!")
        return

    def create_colorMix_node(self, label, x, y, operation):
        mix_node = self.nodes.new(type='CompositorNodeMixRGB')
        mix_node.label = label
        mix_node.location = self.renderLayer_location[0] + x, self.renderLayer_location[1] - y
        mix_node.blend_type = operation
        mix_node.hide = True

        return mix_node

    def renderLayer_output(self, output_name):
        return self.selected_RenderLayer_node.outputs[output_name]

    def link_nodes(self, output_node, input_node):
        self.links.new(output_node, input_node)

    def create_slots_OutputFile(self, output_file_node, final_passes):
        for k, v in final_passes.items():
            output_file_node.file_slots.new(name=v)
            try:
                self.links.new(self.selected_RenderLayer_node.outputs[k], output_file_node.inputs[v])
            except:
                continue
        
        #################################################
        # CRYPTOMATTES
        def identify_active_cryptomattes(outputs):
            cryptomattes = {
                "CryptoObject": [],
                "CryptoMaterial": [],
                "CryptoAsset": []
            }
            for output in outputs:
                for key in cryptomattes.keys():
                    if output.startswith(key):
                        cryptomattes[key].append(output)
                        
            return cryptomattes

        def create_slots(file_output_node, cryptomattes):
            for key, values in cryptomattes.items():
                if values:
                    file_output_node.file_slots.new(name=key)

                    for value in values:
                        if value != key:
                            file_output_node.file_slots.new(name=value)

        def connect_outputs(tree, render_layer_node, file_output_node, cryptomattes):
            for key, values in cryptomattes.items():
                if values:
                    tree.links.new(render_layer_node.outputs['Image'], file_output_node.inputs[key])

                    for value in values:
                        if value != key:
                            tree.links.new(render_layer_node.outputs[value], file_output_node.inputs[value])

        outputs = [output.name for output in self.selected_RenderLayer_node.outputs if output.enabled]
                
        cryptomattes = identify_active_cryptomattes(outputs)
        create_slots(output_file_node, cryptomattes)
        connect_outputs(self.tree, self.selected_RenderLayer_node, output_file_node, cryptomattes)

        return

    def final_passes(self) -> dict:
        # Current name / new name
        viewlayer_passes = {"Image":"rgba", "Alpha":"alpha", "Depth":"depth", "Mist":"mist", "Position":"position", 
                        "Normal":"normal", "Vector":"motion", "UV":"uv", "IndexOB":"indexOB", "IndexMA":"indexMA",
                        "DiffDir":"diffuse_direct", "DiffInd":"diffuse_indirect", "DiffCol":"diffuse_color", "GlossDir":"glossy_direct", "GlossInd":"glossy_indirect", 
                        "GlossCol":"glossy_color", "TransDir":"transmission_direct", "TransInd":"transmission_indirect", "TransCol":"transmission_color", "Emit":"emission", 
                        "Env":"env", "Shadow":"shadow", "Shadow Catcher":"shadow_catcher", "AO":"ambient_occlusion", "Denoising Data":"denoising_data", "Sample Count":"sample_count",
                        "VolumeDir":"volume_direct", "VolumeInd":"volume_indirect", "BloomCol":"bloom", "Transp":"transparent",
                        "Debug Sample Count":"debug_sample_count", "Noisy Image":"noisy_image", "Noisy Shadow Catcher":"noisy_shadow_catcher",
                        "Denoising Normal":"denoising_normal", "Denoising Albedo":"denoising_albedo", "Denoising Depth":"denoising_depth"}

        cryptomattes = ["CryptoObject00", "CryptoObject01", "CryptoObject02",
                        "CryptoMaterial00", "CryptoMaterial01", "CryptoMaterial02",
                        "CryptoAsset00", "CryptoAsset01", "CryptoAsset02"]
        
        enabled_passes = [slot.name for slot in self.selected_RenderLayer_node.outputs if slot.enabled]

        final_passes = {}

        # Adding the enabled regular passes
        for slot in enabled_passes:
            for k, v in viewlayer_passes.items():
                if slot == k:
                    final_passes[k] = v
        
        return final_passes

    def combined_passes(self):
        self.enable_passes()

        final_passes = self.final_passes()

        pos_index = list(final_passes.keys()).index("DiffDir")
        input_channels_list = list(final_passes.items())

        if self.render_engine == self.cycles_engine:
            new_channels = ["diffuse_light", "diffuse_albedo", "reflection", "refraction", "volume"]

        if self.render_engine == self.eevee_engine:
            new_channels = ["diffuse_light", "diffuse_albedo", "reflection", "volume"]

        new_channels.reverse()

        for channel in new_channels:
            input_channels_list.insert(pos_index+1, (channel, channel))

        final_passes = dict(input_channels_list)

        combined_channels = ["DiffDir", "DiffInd", "DiffCol", "GlossDir", "GlossInd", "GlossCol", "TransDir", "TransInd", "TransCol", "VolumeDir", "VolumeInd"]

        for slot in combined_channels:
            if slot in final_passes:
                final_passes.pop(slot)

        return final_passes

    def clear_selection(self):
        # Deselect the nodes
        for node in bpy.context.scene.node_tree.nodes: 
            node.select = False

    def report(self, type, message):
        def draw(self, context):
            self.layout.label(text=message)
        bpy.context.window_manager.popup_menu(draw, title="Info", icon='INFO')

    def error_msg(self):
        error_msg = "Please select the Render Layer node first!"
        print("[INFO] " + error_msg)
        self.report({'INFO'}, error_msg)

# Operators
class AOVStandardOperator(bpy.types.Operator):
    bl_idname = "wm.aov_standard_operator"
    bl_label = "AOV Standard Setup"
    bl_description = "Uses the enabled passes from the Render Layer node"
    
    def execute(self, context):
        dl_output = DL_FileOutput()
        dl_output.aov_standard()
        return {'FINISHED'}


class AOVCompactOperator(bpy.types.Operator):
    bl_idname = "wm.aov_compact_operator"
    bl_label = "AOV Compact Setup"
    bl_description = "Uses the enabled passes from the Render Layer node along with the default light passes"
    
    def execute(self, context):
        dl_output = DL_FileOutput()
        dl_output.aov_compact()
        return {'FINISHED'}


# UI Panel
class DL_Panel(bpy.types.Panel):
    bl_label = TOOL_NAME
    bl_idname = "SCENE_PT_my_compositing_tools"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = TOOL_NAME
    bl_context = 'objectmode'

    def draw(self, context):
        layout = self.layout
        
        # Description
        layout.label(text="Creates an Output File node and sets all the AOV names automatically.")
        layout.separator()

        # Buttons
        # box.label(text="Subpainel")
        row1 = layout.row()
        row1.scale_y = 2.0
        row1.operator("wm.aov_standard_operator")
        row2 = layout.row()
        row2.scale_y = 2.0
        row2.operator("wm.aov_compact_operator")
        
        # Credits
        layout.separator()
        box = layout.box()
        box.label(text="Developed by Danilo de Lucio | VFX Compositor and TD")
        box.label(text="www.danilodelucio.com")


# Register / Unregister
def register():
    bpy.utils.register_class(AOVStandardOperator)
    bpy.utils.register_class(AOVCompactOperator)
    bpy.utils.register_class(DL_Panel)

def unregister():
    bpy.utils.unregister_class(AOVStandardOperator)
    bpy.utils.unregister_class(AOVCompactOperator)
    bpy.utils.unregister_class(DL_Panel)


if __name__ == "__main__":
    register()
