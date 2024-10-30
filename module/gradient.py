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
            self.img = Image.open(c.previewPath)     
            self.Path = c.basePath

            leftTabFrame, frameTop, frameScroll, frameBottom = u.tabFrame(master)

            #### Input ####
            frame1 = ctk.CTkFrame(frameScroll)
            frame1.pack()

            frame11 = ctk.CTkFrame(frameScroll)
            frame11.pack()

            frame2 = ctk.CTkFrame(frameScroll)
            frame2.pack()

            frame3 = ctk.CTkFrame(frameScroll)
            frame3.pack(padx=1,side=LEFT)

            frame01 = ctk.CTkFrame(frame1, width=c.cellW2, height=c.cellH2-30)
            frame01.pack(padx=2, pady=2, side=LEFT)
            frame01.propagate(False)

            frame011 = ctk.CTkFrame(frame11, width=c.cellW2, height=c.cellH2-30)
            frame011.pack(padx=2, pady=2, side=LEFT)
            frame011.propagate(False)


            frame02 = ctk.CTkFrame(frame2, width=c.cellW, height=c.cellH)
            frame02.pack(padx=2, pady=2, side=LEFT)
            frame02.propagate(False)

            frame03 = ctk.CTkFrame(frame2, width=c.cellW, height=c.cellH)
            frame03.pack(padx=2, pady=2, side=LEFT)
            frame03.propagate(False)

            frame04 = ctk.CTkFrame(frame3, width=c.cellW, height=c.cellH)
            frame04.pack(padx=2, pady=2, side=LEFT)
            frame04.propagate(False)

            frame05 = ctk.CTkFrame(frame3, width=c.cellW, height=c.cellH)
            frame05.pack(padx=2, pady=2, side=LEFT)
            frame05.propagate(False)

            frame06 = ctk.CTkFrame(frameTop, width=400, height=30)
            frame06.pack(padx=2, pady=2)
            frame06.propagate(False)
        
            
            self = u.outputDir(self,frame06)
            
            previewImage = ctk.CTkImage(light_image=self.img, size=(480, 480))
            self.previewLabel = ctk.CTkLabel(leftTabFrame, image=previewImage, text='')
            self.previewLabel.pack(pady=c.previewBorderWidth,padx=c.previewBorderWidth)



            self.varA = ctk.IntVar()
            self.previewMethod = ctk.CTkSegmentedButton(frameBottom, state=DISABLED,variable=self.varA,width=250, values=c.extractMethod,  font=c.bFont)
            self.previewMethod.set(c.extractMethod[1])
            self.previewMethod.pack(pady=2, padx=4, side=LEFT)

            self.exportButton = ctk.CTkButton(frameBottom, text="Export",width=198, height=40,state=DISABLED,command=lambda: [u.export(self),u.update_preview(self)], font=c.bFont)
            self.exportButton.pack(pady=2, padx=2, side=RIGHT)
            
            generateButton = ctk.CTkButton(frameBottom, text="Generate",width=198, height=40,command=lambda: [self.generate(),u.update_preview(self)], font=c.bFont)
            generateButton.pack(pady=2, padx=2, side=RIGHT)

            previewFrame = ctk.CTkFrame(frameBottom, width=50,fg_color="#2b2b2b")
            previewFrame.pack(padx=8, pady=2, side=RIGHT)


            #### Color A ####
            labelColor = ctk.CTkLabel(frame01, text="Color A (RGB)", font=c.mFont)
            labelColor.pack(pady=6, padx=16)
            
            self.AsliderRed = u.slider(frame01,"Red",FALSE)
            self.AsliderGreen = u.slider(frame01,"Green",FALSE)
            self.AsliderBlue = u.slider(frame01,"Blue",FALSE)
            #self.AsliderAlpha = u.slider(frame01,"Alpha",TRUE)

            #### Color B ####
            labelColor = ctk.CTkLabel(frame011, text="Color B (RGB)", font=c.mFont)
            labelColor.pack(pady=6, padx=16)
            
            self.BsliderRed = u.slider(frame011,"Red",FALSE)
            self.BsliderGreen = u.slider(frame011,"Green",FALSE)
            self.BsliderBlue = u.slider(frame011,"Blue",FALSE)
            #self.BsliderAlpha = u.slider(frame01,"Alpha",TRUE)
            
            #### FILENAME ####
            labelFilename = ctk.CTkLabel(frame02, text="File Name", font=c.mFont)
            labelFilename.pack(pady=6, padx=16)

            self.inputFilename = ctk.CTkEntry(frame02, width=c.entryWidth, font=c.mFont)
            self.inputFilename.pack(pady=6, padx=16)
            self.inputFilename.insert(0, "T_Gradient")

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

            #### Orient ####
            labelFiletype = ctk.CTkLabel(frame05, text="Orient", font=c.mFont)
            labelFiletype.pack(pady=6, padx=16)

            self.inputFlip = ctk.StringVar()
            self.inputFlip.set(c.orient[0])
            self.inputFlip = ctk.CTkSegmentedButton(frame05,width=250,variable=self.inputFlip, values=c.orient,  font=c.sFont)
            self.inputFlip.pack(pady=6, padx=16)


        

        def generate(self):
            self.exportButton.configure(state=NORMAL)

            OutputDir = self.Path
            Filename = self.inputFilename.get()
            Filetype = self.inputFiletype.get().lower()

            Orient = self.inputFlip.get()
            Width = int(self.inputSizeWidth.get())
            Height = int(self.inputSizeHeight.get())
            
            self.img = Image.new(mode="RGB", size=(Width, Height))

            R1 = self.AsliderRed.get()
            G1 = self.AsliderGreen.get()
            B1 = self.AsliderBlue.get() 
            R2 = self.BsliderRed.get()
            G2 = self.BsliderGreen.get()
            B2 = self.BsliderBlue.get() 

            for w in range(Width):
                for h in range(Height):
                    if Orient == "H" or Orient == "H.F":
                        v = int((h / Height) * 255) 
                    else:
                        v = int((w / Width) * 255)
                    if Orient == "H.F" or Orient == "V.F":
                        v = abs(v - 255)

                    R = int(v * R2 + abs(v - 255) * R1)
                    G = int(v * G2 + abs(v - 255) * G1)
                    B = int(v * B2 + abs(v - 255) * B1)

                    self.img.putpixel((w, h), (R, G, B))

            self.full_path = os.path.join(OutputDir, Filename + "."+Filetype)
        
