from PIL import Image
import tkinter as tk 
import customtkinter as ctk
import constants as c 

# Initialize root
root = ctk.CTk()

# Create a label that will show the image
label = ctk.CTkLabel(master=root, text='')
label.pack()

previewImage = ctk.CTkImage(light_image=Image.open(c.previewPath), size=(480, 480))
label = ctk.CTkLabel(root, image=previewImage, text='')
label.pack(pady=3,padx=3)



inputHexEntry = ctk.CTkEntry(root, width=128, font=c.sFont)
inputHexEntry.pack(pady=6, padx=16)
inputHexEntry.insert(0, "1")


img = Image.new(mode="RGBA", size=(64, 64))
def generate():
    global img, full_path
    for w in range(64):
        for h in range(64):
            R = int(inputHexEntry.get())
            G = 0
            B = 0
            A = 255

            img.putpixel((w, h), (R, G, B))

    img.putalpha(A)

    full_path = "E:\.Temp\T_Solid_64x64.png"


def export():
    img.save(full_path)

def update_preview():
    img_preview = ctk.CTkImage(light_image=img, size=(480, 480))
    label.configure(image=img_preview)
    label.image = img_preview

button = ctk.CTkButton(root, command=lambda: [generate(),update_preview()], text="generate")
button.pack(pady=10)

button = ctk.CTkButton(root, command=lambda: [export(),update_preview()], text="export")
button.pack(pady=10)

# Start the application loop
root.mainloop()
