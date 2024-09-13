import os
from tkinter import *
from tkinter import filedialog
from PIL import Image
import customtkinter as ctk
import constants as c 
import utils as u 

if __name__ != "__main__" : 
    class Solid:
        def __init__(self, master):
            self.img = Image.open(c.previewPath)     
            self.Path = os.getcwd()+"\\export"

            leftTabFrame, frameTop, frameScroll, frameBottom = u.tabFrame(master)

            #### Input ####
            frame1 = ctk.CTkFrame(frameScroll)
            frame1.pack()

            frame2 = ctk.CTkFrame(frameScroll)
            frame2.pack()

            frame3 = ctk.CTkFrame(frameScroll)
            frame3.pack(padx=1,side=LEFT)

            frame01 = ctk.CTkFrame(frame1, width=c.cellW2, height=c.cellH2)
            frame01.pack(padx=2, pady=2, side=LEFT)
            frame01.propagate(False)

            frame02 = ctk.CTkFrame(frame2, width=c.cellW, height=c.cellH)
            frame02.pack(padx=2, pady=2, side=LEFT)
            frame02.propagate(False)

            frame03 = ctk.CTkFrame(frame2, width=c.cellW, height=c.cellH)
            frame03.pack(padx=2, pady=2, side=LEFT)
            frame03.propagate(False)

            frame04 = ctk.CTkFrame(frame3, width=c.cellW, height=c.cellH)
            frame04.pack(padx=2, pady=2, side=LEFT)
            frame04.propagate(False)

            frame06 = ctk.CTkFrame(frameTop, width=400, height=30)
            frame06.pack(padx=2, pady=2)
            frame06.propagate(False)
        
            
            self = u.outputDir(self,frame06)
            
            previewImage = ctk.CTkImage(light_image=self.img, size=(480, 480))
            self.previewLabel = ctk.CTkLabel(leftTabFrame, image=previewImage, text='')
            self.previewLabel.pack(pady=c.previewBorderWidth,padx=c.previewBorderWidth)


            extractMethod = ["Input","Output"]
            self.varA = ctk.IntVar()
            self.preview = ctk.CTkSegmentedButton(frameBottom, state=DISABLED,variable=self.varA,width=250, values=extractMethod,  font=c.bFont)
            self.preview.set(extractMethod[1])
            self.preview.pack(pady=2, padx=4, side=LEFT)



            self.exportButton = ctk.CTkButton(frameBottom, text="Export",width=198, height=40,state=DISABLED,command=lambda: [self.export(),self.update_preview()], font=c.bFont)
            self.exportButton.pack(pady=2, padx=2, side=RIGHT)
            
            generateButton = ctk.CTkButton(frameBottom, text="Generate",width=198, height=40,command=lambda: [self.generate(),self.update_preview()], font=c.bFont)
            generateButton.pack(pady=2, padx=2, side=RIGHT)

            self.refreshButton = ctk.CTkButton(frameBottom, text="Refresh",width=20, height=40, command=self.update_preview, font=c.bFont)
            self.refreshButton.pack(pady=2, padx=2, side=RIGHT)

            self.openButton = ctk.CTkButton(frameBottom, text="Open",width=20, height=40, font=c.bFont)
            self.openButton.pack(pady=2, padx=2, side=RIGHT)

            previewFrame = ctk.CTkFrame(frameBottom, width=50,fg_color="#2b2b2b")
            previewFrame.pack(padx=8, pady=2, side=RIGHT)

            """
            self.redBut = u.previewColorChannel(self,previewFrame,"red","")
            self.greenBut = u.previewColorChannel(self,previewFrame,"green","")
            self.blueBut = u.previewColorChannel(self,previewFrame,"blue","")
            self.alphaBut = u.previewColorChannel(self,previewFrame,"white","")
            """


            self.butVarRed = ctk.IntVar()
            self.butVarRed.set(TRUE)
            self.Button = ctk.CTkCheckBox(previewFrame,text="",
                                            width=1,font=c.bFont,
                                            checkbox_height=32,checkbox_width=32,
                                            variable=self.butVarRed,
                                            hover_color="red")
            self.Button.pack(pady=1, padx=1, side=LEFT)

            self.butVarGreen = ctk.IntVar()
            self.butVarGreen.set(TRUE)
            self.Button = ctk.CTkCheckBox(previewFrame,text="",
                                            width=1,font=c.bFont,
                                            checkbox_height=32,checkbox_width=32,
                                            variable=self.butVarGreen,
                                            hover_color="green")
            self.Button.pack(pady=1, padx=1, side=LEFT)

            self.butVarBlue = ctk.IntVar()
            self.butVarBlue.set(TRUE)
            self.Button = ctk.CTkCheckBox(previewFrame,text="",
                                            width=1,font=c.bFont,
                                            checkbox_height=32,checkbox_width=32,
                                            variable=self.butVarBlue,
                                            hover_color="blue")
            self.Button.pack(pady=1, padx=1, side=LEFT)

            self.butVarAlpha = ctk.IntVar()
            self.butVarAlpha.set(TRUE)
            self.Button = ctk.CTkCheckBox(previewFrame,text="",
                                            width=1,font=c.bFont,
                                            checkbox_height=32,checkbox_width=32,
                                            variable=self.butVarAlpha,
                                            hover_color="white")
            self.Button.pack(pady=1, padx=1, side=LEFT)

            #### Color ####
            labelColor = ctk.CTkLabel(frame01, text="Color (RGBA)", font=c.mFont)
            labelColor.pack(pady=6, padx=16)
            
            self.sliderRed = u.slider(frame01,"Red",FALSE)
            self.sliderGreen = u.slider(frame01,"Green",FALSE)
            self.sliderBlue = u.slider(frame01,"Blue",FALSE)
            self.sliderAlpha = u.slider(frame01,"Alpha",TRUE)

            
            #### FILENAME ####
            labelFilename = ctk.CTkLabel(frame02, text="File Name", font=c.mFont)
            labelFilename.pack(pady=6, padx=16)

            self.inputFilename = ctk.CTkEntry(frame02, width=c.entryWidth, font=c.mFont)
            self.inputFilename.pack(pady=6, padx=16)
            self.inputFilename.insert(0, "T_SolidColor")

            #### SIZE ####
            labelSize = ctk.CTkLabel(frame03, text="Size", font=c.mFont)
            labelSize.pack(pady=6, padx=16)

            self.inputSizeWidth = ctk.CTkEntry(frame03, width=c.entryWidth/2, font=c.mFont)
            self.inputSizeWidth.pack(pady=6, padx=8,side=LEFT)
            self.inputSizeWidth.insert(0, "512")

            labelSize = ctk.CTkLabel(frame03, text="x", font=c.mFont)
            labelSize.pack(pady=6, padx=0,side=LEFT)

            self.inputSizeHeight = ctk.CTkEntry(frame03, width=c.entryWidth/2, font=c.mFont)
            self.inputSizeHeight.pack(pady=6, padx=8,side=LEFT)
            self.inputSizeHeight.insert(0, "512")

            #### FILETYPE ####
            labelFiletype = ctk.CTkLabel(frame04, text="File Type", font=c.mFont)
            labelFiletype.pack(pady=6, padx=16)

            self.Filetype = ctk.StringVar()
            self.Filetype.set(c.Extensions[0])
            self.inputFiletype = ctk.CTkSegmentedButton(frame04,width=250,variable=self.Filetype, values=c.Extensions,  font=c.sFont)
            self.inputFiletype.pack(pady=6, padx=16)

        def set_directory(self):
            self.Path = filedialog.askdirectory(title="Directory")
            if self.Path:
                self.mainDirectoryPath.configure(text=self.Path,text_color="white")

        def generate(self):
            self.exportButton.configure(state=NORMAL)

            R1 = self.sliderRed.get()
            G1 = self.sliderGreen.get()
            B1 = self.sliderBlue.get() 
            A1 = self.sliderAlpha.get()
            OutputDir = self.Path
            Filename = self.inputFilename.get()
            Filetype = self.Filetype.get()

            Filetype = Filetype.lower()
            Width = int(self.inputSizeWidth.get())
            Height = int(self.inputSizeHeight.get())
            
            if Filetype == "jpg":
                self.img = Image.new(mode="RGB", size=(Width, Height))
            else:
                self.img = Image.new(mode="RGBA", size=(Width, Height))

            for w in range(Width):
                for h in range(Height):
                    R = int(R1 * 255 )
                    G = int(G1 * 255 )
                    B = int(B1 * 255 )
                    self.img.putpixel((w, h), (R, G, B))

            if Filetype != "jpg":
                A = int(A1 * 255)
                self.img.putalpha(A)
                
            self.full_path = os.path.join(OutputDir, Filename + "."+Filetype)

        def export(self):
            self.exportButton.configure(state=DISABLED)
            self.img.save(self.full_path)

        def update_preview(self):
            """
            r = self.butVarRed.get()
            g = self.butVarGreen.get()
            b = self.butVarBlue.get()
            a = self.butVarAlpha.get()

            print(r)
            print(g)
            print(b)
            print(a)
            print("------------")

            

            R1, G1, B1, A1 = 0,0,0,0

            while (r == 1):
                R1 = 1
            while (g == 1): 
                G1 = 1
            while (b == 1):
                B1 = 1
            while (a == 1): 
                A1 = 1

            self.img = self.img.resize((480,480),resample=Image.LANCZOS)

            Width, Height = self.img.size

            print(self.img.size)
            for w in range(Width):
                for h in range(Height):
                    R,G,B = self.img.getpixel((w,h))

                    R2 = R * R1
                    G2 = G * G1
                    B2 = B * B1

                    self.img.putpixel((w, h), (R2, G2, B2))
            """
            img_preview = ctk.CTkImage(light_image=self.img, size=(480, 480))

            self.previewLabel.configure(image=img_preview)
            self.previewLabel.image = img_preview
