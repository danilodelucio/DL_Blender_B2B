# DL_FileOutput_for_Blender
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


<br><h1>Nuke Back to Beauty Templates ☢️</h1>

![Screenshot 2024-11-06 153242](https://github.com/user-attachments/assets/341dfd62-a290-4cd4-89a1-d7aab073c42e)

It includes Nuke AOV templates, which are custom setups for rebuilding the render passes within Nuke (also known as **Back to Beauty**).

- Blender_AOVs_BacktoBeauty_Standard_Cycles_v1;
- Blender_AOVs_BacktoBeauty_Compact_Cycles_v1;
- Blender_AOVs_BacktoBeauty_Standard_Eevee_v1;
- Blender_AOVs_BacktoBeauty_Compact_Eevee_v1;

> _They were made by following the original [Blender documentation](https://docs.blender.org/manual/en/3.2/render/layers/passes.html)._

<br>
Once you download it, you can drag and drop the Nuke files into your Nuke. 

<br>![DragAndDrop_templates_v001_](https://github.com/user-attachments/assets/bbcfd655-84cc-463d-a03b-ca0a740ca1f0)


> [!TIP]
> Alternatively, click one of these setups (located in the Nuke folder here on this GitHub page), then click "copy raw file" on the right side of the screen and paste it into your Nuke.

![image](https://github.com/user-attachments/assets/03fd757e-b595-437d-b8b1-3ae285d7b409)


> _These Nuke setups use Stamps. You don't need to have it installed, but if you want to, you can download it [here](https://www.nukepedia.com/gizmos/other/stamps)._



<br><h1>Installing ⚙️</h1>

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

<br><h1>Support me! 🥺</h1>

![image](https://github.com/user-attachments/assets/1268bd3e-07cd-40a0-980a-3543e4e35e78)

This personal project required significant time and extra hours of hard work to make it available to everyone. <br>

If you find this tool useful, please consider supporting me on [Buy Me A Coffee](https://www.buymeacoffee.com/danilodelucio). ☕ <br>
You can also share this tool or send me a positive message, it would help me in the same way.

---
<h1>Cheers! 🥂</h1>
