import os
from tkinter import *
from tkinter import filedialog
from PIL import Image
import customtkinter as ctk
import constants as c 
import utils as u 

if __name__ != "__main__" : 
    class Gradient:
        def __init__(self, master):

            
            leftTabFrame, frameTop, frameScroll, frameBottom = u.tabFrame(master)

            previewImage = ctk.CTkImage(light_image=Image.open(c.previewPath), size=(480 , 480))
            label = ctk.CTkLabel(leftTabFrame, image=previewImage, text='')
            label.pack(pady=3,padx=3)

            #### Input ####
            frame1 = ctk.CTkFrame(frameScroll)
            frame1.pack()

            frame2 = ctk.CTkFrame(frameScroll)
            frame2.pack()

            frame3 = ctk.CTkFrame(frameScroll)
            frame3.pack()

            frame01 = ctk.CTkFrame(frame1, width=c.cellW, height=c.cellH)
            frame01.pack(padx=2, pady=2, side=LEFT)
            frame01.propagate(False)

            frame02 = ctk.CTkFrame(frame1, width=c.cellW, height=c.cellH)
            frame02.pack(padx=2, pady=2, side=LEFT)
            frame02.propagate(False)

            frame03 = ctk.CTkFrame(frame2, width=c.cellW, height=c.cellH)
            frame03.pack(padx=2, pady=2, side=LEFT)
            frame03.propagate(False)

            frame04 = ctk.CTkFrame(frame2, width=c.cellW, height=c.cellH)
            frame04.pack(padx=2, pady=2, side=LEFT)
            frame04.propagate(False)

            frame05 = ctk.CTkFrame(frame3, width=c.cellW, height=c.cellH)
            frame05.pack(padx=2, pady=2, side=LEFT)
            frame05.propagate(False)

            frame06 = ctk.CTkFrame(frame3, width=c.cellW, height=c.cellH)
            frame06.pack(padx=2, pady=2, side=LEFT)
            frame06.propagate(False)

            frame07 = ctk.CTkFrame(frameTop, width=400, height=30)
            frame07.pack(padx=2, pady=2)
            frame07.propagate(False)


            #### OUTPUT DIRECTORY ####
            button = ctk.CTkButton(frame07, text="Set Output", width=100, command=self.set_output_dir, font=c.sFont)
            button.pack(pady=2, padx=2, side=RIGHT)

            mainDirectory = ctk.CTkLabel(frame07, text="Output:", font=c.sFont)
            mainDirectory.pack(pady=2, padx=6, side=LEFT)

            #self.mainDirectoryStatus = ctk.CTkLabel(frame08, text="Unset", font=c.sFont, text_color="red")
            #self.mainDirectoryStatus.pack(pady=2, padx=6, side=LEFT)

            self.mainDirectoryPath = ctk.CTkLabel(frame07, text="Unset", text_color="red", font=c.sFont)
            self.mainDirectoryPath.pack(pady=2, padx=6,side=LEFT)


            GenerateButton = ctk.CTkButton(frameBottom, text="Export Gradient", width=c.appWidth, height=40, command=self.generate, font=c.bFont)
            GenerateButton.pack(pady=2, padx=2, side=LEFT)



            #### COLOR 1 ####
            labelColor1 = ctk.CTkLabel(frame01, text="COLOR 1 (RGB)", font=c.mFont)
            labelColor1.pack(pady=6, padx=16)

            self.inputColor1 = ctk.CTkEntry(frame01, width=128, font=c.sFont)
            self.inputColor1.pack(pady=6, padx=16)
            self.inputColor1.insert(0, "0,0,0")

            #### COLOR 2 ####
            labelColor2 = ctk.CTkLabel(frame02, text="COLOR 2 (RGB)", font=c.mFont)
            labelColor2.pack(pady=6, padx=16)

            self.inputColor2 = ctk.CTkEntry(frame02, width=128, font=c.sFont)
            self.inputColor2.pack(pady=6, padx=16)
            self.inputColor2.insert(0, "1,1,1")

            #### FILENAME ####
            labelFilename = ctk.CTkLabel(frame03, text="FILENAME", font=c.mFont)
            labelFilename.pack(pady=6, padx=16)

            self.inputFilename = ctk.CTkEntry(frame03, width=128, font=c.sFont)
            self.inputFilename.pack(pady=6, padx=16)
            self.inputFilename.insert(0, "T_Gradient")

            #### SIZE ####
            labelSize = ctk.CTkLabel(frame04, text="SIZE", font=c.mFont)
            labelSize.pack(pady=6, padx=16)

            self.inputSize = ctk.CTkEntry(frame04, width=128, font=c.sFont)
            self.inputSize.pack(pady=6, padx=16)
            self.inputSize.insert(0, "512x512")

            #### Orientation ####
            labelOrient = ctk.CTkLabel(frame05, text="ORIENTATION", font=c.mFont)
            labelOrient.pack(pady=6, padx=16)
            
            orient = ["HORIZ","HORIZ FLIP","VERTI","VERTI FLIP"]
            
            self.var1 = ctk.IntVar()
            self.inputFlip = ctk.CTkOptionMenu(frame05, variable=self.var1, values=orient, width=128, font=c.sFont)
            self.inputFlip.set(orient[0])
            self.inputFlip.pack(pady=6, padx=16)

            #### FILETYPE ####
            labelFiletype = ctk.CTkLabel(frame06, text="FILETYPE", font=c.mFont)
            labelFiletype.pack(pady=6, padx=16)

            self.var2 = ctk.IntVar()
            self.inputFiletype = ctk.CTkOptionMenu(frame06, variable=self.var2, values=c.Extensions, width=128, font=c.sFont)
            self.inputFiletype.set(c.Extensions[0])
            self.inputFiletype.pack(pady=6, padx=16)

            self.Path = ""
        def set_output_dir(self):
            self.Path = filedialog.askdirectory(title="Directory")
            if self.Path:
                #self.mainDirectoryStatus.configure(text="Ready", text_color="green")
                self.mainDirectoryPath.configure(text=self.Path,text_color="white")
            

        def generate(self):
            Color1 = self.inputColor1.get()
            Color2 = self.inputColor2.get()
            Size = self.inputSize.get()
            OutputDir = self.Path
            Filename = self.inputFilename.get()
            Filetype = self.inputFiletype.get()
            Orient = self.inputFlip.get()
            SizeNew = Size.lower()
            Width = int(SizeNew.split("x")[0])
            Height = int(SizeNew.split("x")[1])
            
            FiletypeNew = Filetype.lower().replace(".", "")

            img = Image.new(mode="RGB", size=(Width, Height))

            Color1 = Color1.replace(" ", "")
            Color2 = Color2.replace(" ", "")
            
            R1, G1, B1 = map(float, Color1.split(","))
            R2, G2, B2 = map(float, Color2.split(","))

            for w in range(Width):
                for h in range(Height):
                    if Orient == "HORIZ" or Orient == "HORIZ FLIP":
                        v = int((h / Height) * 255) 
                    else:
                        v = int((w / Width) * 255)
                    if Orient == "HORIZ FLIP" or Orient == "VERTI FLIP":
                        v = abs(v - 255)

                    R = int(v * R2 + abs(v - 255) * R1)
                    G = int(v * G2 + abs(v - 255) * G1)
                    B = int(v * B2 + abs(v - 255) * B1)

                    img.putpixel((w, h), (R, G, B))

            name = f"{Filename}_{Width}x{Height}.{FiletypeNew}"
            imgOutput = os.path.join(OutputDir, name)

            img.save(imgOutput)
            print(f"Image saved to {imgOutput}")            