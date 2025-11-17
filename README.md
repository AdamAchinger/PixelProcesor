# PixelProcesor

PixelProcesor is a simple program for texture manipulation, designed for game developers, 3D artists.
It enables fast generation, editing, and combining of textures in an intuitive way.

---

## 1. **SolidColor**

The SolidColor module allows you to create single‑color textures based on specified **RGBA** values.

<img width="910" height="734" alt="image" src="https://github.com/user-attachments/assets/219ffe07-dfa1-4d36-9e12-a53275e00aaf" />

**Features:**

* manual color setup (R, G, B, A),
* generation of uniform textures,
* export in selected resolutions.

---

## 2. **Gradient**

A module for creating gradients with number of colors, both vertically and horizontally.

<img width="910" height="733" alt="image" src="https://github.com/user-attachments/assets/561348f2-e45e-4660-bdff-c125017dcb17" />

**Features:**

* vertical and horizontal gradients,
* export in selected resolutions.

---

## 3. **Math**

The Math module allows you to perform mathematical operations on pixel values.

<img width="910" height="1103" alt="pp_Math" src="https://github.com/user-attachments/assets/ddddcb18-b7c3-4524-bd95-e3c762eacc4b" />



**Available operations:**

* multiplication,
* power,
* addition and subtraction,
* setting minimum and maximum pixel values,
* **invert** and **posterize** functions.

All operations can be applied to all channels or selected individual channels.

---

## 4. **Separate**

Provide a texture, and the program splits it into individual channels for export.

<img width="1800" height="2194" alt="pp_separate" src="https://github.com/user-attachments/assets/9db3cb3c-6879-4954-adb4-df26a1d6afd1" />

Example: If you have an ARM texture (Ambient Occlusion, Roughness, Metallic), you can export only the **Roughness** channel without the others.

---

## 5. **Combine**

A module that allows you to merge channels from different textures into a new mask map.

<img width="1800" height="2194" alt="PP_Combine" src="https://github.com/user-attachments/assets/24dbb366-c7ca-4981-abe0-bba8b5c45878" />

**Use cases:**

* creating ARM maps,
* creating RMA maps,
* building fully custom mask maps.

You can freely assign channels (R, G, B, A) from different textures to create a completely new output texture.

---

## Author
Adam Achinger 

