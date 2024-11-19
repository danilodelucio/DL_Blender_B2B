![cover_v002](https://github.com/user-attachments/assets/50e5d971-9840-4395-8af6-5523221aa27a)


This repository provides a complete **AOV - Back to Beauty** workflow from Blender to Compositing in Nuke or Fusion:
- **DL_FileOutput** for Blender to set the AOV names automatically;
- AOVs Back to Beauty Templates for Nuke/Fusion;

# DL_FileOutput
This free addon creates a File Output node inside Blender and sets the AOV names (render passes), automatically.

It was developed and tested in **Blender 4.1.0**.

![testing_buttons_v003_](https://github.com/user-attachments/assets/4f3d9781-2a4e-4a1d-9c4a-bff0bf65115e)


There are two buttons:

- **AOV Standard Setup**: uses the enabled passes from the Render Layer node;
- **AOV Compact Setup**: Uses the enabled passes from the Render Layer node along with the default light passes;

In summary, the Compact setup provides a straightforward AOV combination directly inside Blender, so you will get the final result for some render passes.

For example:
- **Diffuse Light** = Diffuse Direct + Diffuse Indirect;
- **Diffuse Albedo** = which is the original Diffuse Color;
- **Reflection** = Glossy Color x (Glossy Direct + Glossy Indirect);
- **Refraction** = Transmission Color x (Transmission Direct + Transmission Indirect);
- **Volume** = Volume Direct + Volume Indirect;

> [!IMPORTANT]
> _For now, this add-on has been designed to work only with Cycles and Eevee engines._


<br>

# Back to Beauty Templates for Nuke/Fusion ☢️

It includes Nuke/Fusion AOV templates, which are custom setups for rebuilding the render passes (also known as **Back to Beauty**).

- Blender_AOVs_BacktoBeauty_Standard_Cycles_v1;
- Blender_AOVs_BacktoBeauty_Compact_Cycles_v1;
- Blender_AOVs_BacktoBeauty_Standard_Eevee_v1;
- Blender_AOVs_BacktoBeauty_Compact_Eevee_v1;

> _They were made by following the original [Blender documentation](https://docs.blender.org/manual/en/3.2/render/layers/passes.html)._

![Screenshot 2024-11-06 153242](https://github.com/user-attachments/assets/341dfd62-a290-4cd4-89a1-d7aab073c42e)
![Screenshot 2024-11-18 175012](https://github.com/user-attachments/assets/2d5da5fb-774d-4699-a9bb-13e606eebd95)

<br>

Once you download it, you can drag and drop the **.nk**/**.setting** files into your Nuke/Fusion. 

<br>![DragAndDrop_templates_v003_](https://github.com/user-attachments/assets/de296ec1-3c2a-42fb-bd1e-517253bbdf00)


> [!TIP]
> Alternatively, click one of these setups (here on this GitHub page), then click "copy raw file" on the right side of the screen and paste it into your Nuke/Fusion.

![image](https://github.com/user-attachments/assets/03fd757e-b595-437d-b8b1-3ae285d7b409)


> _These Nuke setups use Stamps. You don't need to have it installed, but if you want to, you can download it [here](https://www.nukepedia.com/gizmos/other/stamps)._



<br><h1>Installing DL_FileOutput ⚙️</h1>

Click on the green button and download the zip file.

![Screenshot 2024-11-06 175507](https://github.com/user-attachments/assets/1421eaa6-baac-4494-b2a9-38c41dcbc8aa)

Once you have downloaded and extracted the files, open Blender and go to **Edit** -> **Preferences** -> **Addons** -> then click on the **Install** button.
Locate the **DL_FileOutput.py** file and check the box to enable the Add-on.

![Screenshot 2024-11-06 182751](https://github.com/user-attachments/assets/1490a9ee-b6f3-4f50-a7f6-812d8f266067)

Now you should see the Addon in the Compositor editor.

![Screenshot 2024-11-06 183122](https://github.com/user-attachments/assets/b31311f9-b184-4ccb-9371-23c387245147)


<br><h1>Troubleshooting 🛠️</h1>

<br>

If you have feedback, suggestions, or feature requests, please visit the [Discussions](https://github.com/danilodelucio/DL_FileOutput_for_Blender/discussions) page and create a **New Discussion**.<br>
For bugs, please go to the [Issues](https://github.com/danilodelucio/DL_FileOutput_for_Blender/issues) page and create a **New Issue**.
<br>

<br><h1>Supporters 💪</h1>

- Marco Silva;

<br><h1>Support me! 🥺</h1>

![image](https://github.com/user-attachments/assets/1268bd3e-07cd-40a0-980a-3543e4e35e78)

This personal project required significant time and extra hours of hard work to make it available to everyone. <br>

If you find this tool useful, please consider supporting me on [Buy Me A Coffee](https://www.buymeacoffee.com/danilodelucio). ☕ <br>
_If you donate any amount, please mention this tool (also your preference name if you want to), so your name will appear in the Supporters list above._

You can also share this tool or send me a positive message, it would help me in the same way.

---

Thanks to Gustavo Goncalves, Marco Silva and Natan Manzano for testing this tool.

<h1>Cheers! 🥂</h1>
