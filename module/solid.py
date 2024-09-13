import os
from tkinter import *
from tkinter import filedialog
from PIL import Image
import customtkinter as ctk
import constants as c 
import utils as u 

if __name__ != "__main__" : 
    class Solid:
        def __init__(self, master, Path):
            self.Path = Path+"\\export"

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
            
            previewImage = ctk.CTkImage(light_image=Image.open(c.previewPath), size=(480, 480))
            self.previewLabel = ctk.CTkLabel(leftTabFrame, image=previewImage, text='')
            self.previewLabel.pack(pady=c.previewBorderWidth,padx=c.previewBorderWidth)

            labelPreview = ctk.CTkLabel(frameBottom, text="Preview:", font=c.bFont)
            labelPreview.pack(pady=2, padx=10,side=LEFT)

            extractMethod = ["Input","Output"]
            self.varA = ctk.IntVar()
            self.preview = ctk.CTkSegmentedButton(frameBottom, state=DISABLED,variable=self.varA,width=250, values=extractMethod,  font=c.bFont)
            self.preview.set(extractMethod[1])
            self.preview.pack(pady=2, padx=2, side=LEFT)

            self.exportButton = ctk.CTkButton(frameBottom, text="Export",width=198, height=40,state=DISABLED,command=lambda: [self.export(),self.update_preview()], font=c.bFont)
            self.exportButton.pack(pady=2, padx=2, side=RIGHT)

            generateButton = ctk.CTkButton(frameBottom, text="Generate",width=198, height=40,command=lambda: [self.generate(),self.update_preview()], font=c.bFont)
            generateButton.pack(pady=2, padx=2, side=RIGHT)


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
            img_preview = ctk.CTkImage(light_image=self.img, size=(480, 480))
            self.previewLabel.configure(image=img_preview)
            self.previewLabel.image = img_preview

    class Gradient:
        def __init__(self, master):

            
            leftTabFrame, frameTop, frameScroll, frameBottom = u.tabFrame(master)

            previewImage = ctk.CTkImage(light_image=Image.open(os.path.join('B:\Foldery\Pobrane\default_Base_color_1001.png')), size=(480 , 480))
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
            
    class Math:
        def __init__(self, master):

            frameMaster = ctk.CTkFrame(master,fg_color=c.fgColor)
            frameMaster.pack(fill=Y,expand=TRUE)

            frameTop = ctk.CTkFrame(frameMaster,height=50)
            frameTop.pack(padx=1,pady=1,side=TOP)

            frameScroll = ctk.CTkScrollableFrame(frameMaster,width=400)
            frameScroll.pack(padx=1,pady=1,fill=Y,expand=TRUE)  

            frameBottom = ctk.CTkFrame(frameMaster,height=50)
            frameBottom.pack(padx=1,pady=1,side=BOTTOM)
        
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

            frame08 = ctk.CTkFrame(frameTop, width=400, height=30)
            frame08.pack(padx=2, pady=1)
            frame08.propagate(False)
            
            frame09 = ctk.CTkFrame(frameTop, width=400, height=30)
            frame09.pack(padx=2, pady=1)
            frame09.propagate(False)



            #### INPUT FILE ####
            buttonIn = ctk.CTkButton(frame08, text="Set Input",command=self.set_input_dir, width=100, font=c.sFont)
            buttonIn.pack(pady=2, padx=2, side=RIGHT)
            
            mainDirectoryIn = ctk.CTkLabel(frame08, text="Input:", font=c.sFont)
            mainDirectoryIn.pack(pady=2, padx=6, side=LEFT)

            #self.mainDirectoryStatus = ctk.CTkLabel(frame09, text="Unset", font=c.sFont, text_color="red")
            #self.mainDirectoryStatus.pack(pady=2, padx=6, side=LEFT)

            self.mainDirectoryPathIn = ctk.CTkLabel(frame08, text="Unset", text_color="red", font=c.sFont)
            self.mainDirectoryPathIn.pack(pady=2, padx=6,side=LEFT)   


            #### OUTPUT DIRECTORY ####
            buttonOut = ctk.CTkButton(frame09, text="Set Output",command=self.set_output_dir, width=100, font=c.sFont)
            buttonOut.pack(pady=2, padx=2, side=RIGHT)

            mainDirectoryOut = ctk.CTkLabel(frame09, text="Output:",width=32, font=c.sFont)
            mainDirectoryOut.pack(pady=2, padx=6, side=LEFT)

            #self.mainDirectoryStatus = ctk.CTkLabel(frame08, text="Unset", font=c.sFont, text_color="red")
            #self.mainDirectoryStatus.pack(pady=2, padx=6, side=LEFT)

            self.mainDirectoryPathOut = ctk.CTkLabel(frame09,  text="Unset", text_color="red", font=c.sFont)
            self.mainDirectoryPathOut.pack(pady=2, padx=6,side=LEFT)

            GenerateButton = ctk.CTkButton(frameBottom, text="Export", width=c.appWidth, command=self.generate, height=40, font=c.bFont)
            GenerateButton.pack(pady=2, padx=2, side=LEFT)



            #### Multiply #### 
            labelMultiply = ctk.CTkLabel(frame01, text="MULTIPLY", font=c.mFont)
            labelMultiply.pack(pady=6, padx=16)
            self.inputMultiply = ctk.CTkEntry(frame01, width=128, font=c.sFont)
            self.inputMultiply.pack(pady=6, padx=16)
            self.inputMultiply.insert(0, "1,1,1,1")


            #### Power #### 
            labelPower = ctk.CTkLabel(frame02, text="POWER", font=c.mFont)
            labelPower.pack(pady=6, padx=16)
            self.inputPower = ctk.CTkEntry(frame02, width=128, font=c.sFont)
            self.inputPower.pack(pady=6, padx=16)
            self.inputPower.insert(0, "1,1,1,1")

            #### Add #### 
            labelAdd = ctk.CTkLabel(frame03, text="ADD", font=c.mFont)
            labelAdd.pack(pady=6, padx=16)
            self.inputAdd = ctk.CTkEntry(frame03, width=128, font=c.sFont)
            self.inputAdd.pack(pady=6, padx=16)
            self.inputAdd.insert(0, "0,0,0,0")



            #### Subtract #### 
            labelSubtract = ctk.CTkLabel(frame04, text="SUBTRACT", font=c.mFont)
            labelSubtract.pack(pady=6, padx=16)
            self.inputSubtract = ctk.CTkEntry(frame04, width=128, font=c.sFont)
            self.inputSubtract.pack(pady=6, padx=16)
            self.inputSubtract.insert(0, "0,0,0,0")



            #### Max #### 
            labelMax = ctk.CTkLabel(frame05, text="MAX", font=c.mFont)
            labelMax.pack(pady=6, padx=16)
            self.inputMax = ctk.CTkEntry(frame05, width=128, font=c.sFont)
            self.inputMax.pack(pady=6, padx=16)
            self.inputMax.insert(0, "1,1,1,1")


            #### Min #### 
            labelMin = ctk.CTkLabel(frame06, text="MIN", font=c.mFont)
            labelMin.pack(pady=6, padx=16)
            self.inputMin = ctk.CTkEntry(frame06, width=128, font=c.sFont)
            self.inputMin.pack(pady=6, padx=16)
            self.inputMin.insert(0, "0,0,0,0")       


        def set_input_dir(self):
            self.InputFilePath = filedialog.askopenfilename(title="Input File")
            if (self.InputFilePath != ""):
                #self.InputStatus.configure(text="Ready", text_color="green")
                self.InputFilePath1 = self.InputFilePath.split("/")[-1]
                self.mainDirectoryPathIn.configure(text=self.InputFilePath1,text_color="white")

        def set_output_dir(self):
            self.OutputFilePath = filedialog.asksaveasfilename(title="Output File")
            if (self.OutputFilePath != ""):
                #self.OutputStatus.configure(text="Ready", text_color="green")
                self.OutputFilePath1 = self.OutputFilePath.split("/")[-1]
                self.mainDirectoryPathOut.configure(text=self.OutputFilePath1,text_color="white")



        def generate(self):
            Multiply4 = self.inputMultiply.get()
            Power4 = self.inputPower.get()
            Add4 = self.inputAdd.get()
            Subtract4 = self.inputSubtract.get()
            Min4 = self.inputMin.get()
            Max4 = self.inputMax.get()
            InputFile = self.InputFilePath
            Output = self.OutputFilePath

            # Open image in RGBA mode
            img = Image.open(InputFile).convert("RGBA")
            Width, Height = img.size

            for w in range(Width):
                for h in range(Height):
                    ### Multiply ###
                    if (Multiply4 != "1,1,1,1"):
                        R1, G1, B1, A1 = img.getpixel((w, h))
                        R = int(R1 * float(Multiply4.split(",")[0]))
                        G = int(G1 * float(Multiply4.split(",")[1]))
                        B = int(B1 * float(Multiply4.split(",")[2]))
                        A = int(A1 * float(Multiply4.split(",")[3]))  # Alpha channel
                        img.putpixel((w, h), (R, G, B, A))

                    ### Power ###
                    if (Power4 != "1,1,1,1"):
                        R1, G1, B1, A1 = img.getpixel((w, h))
                        R = int(pow(R1, float(Power4.split(",")[0])))
                        G = int(pow(G1, float(Power4.split(",")[1])))
                        B = int(pow(B1, float(Power4.split(",")[2])))
                        A = int(pow(A1, float(Power4.split(",")[3])))  # Alpha channel
                        img.putpixel((w, h), (R, G, B, A))

                    ### Add ###
                    if (Add4 != "0,0,0,0"):
                        R1, G1, B1, A1 = img.getpixel((w, h))
                        R = int(R1 + (float(Add4.split(",")[0]) * 255))
                        G = int(G1 + (float(Add4.split(",")[1]) * 255))
                        B = int(B1 + (float(Add4.split(",")[2]) * 255))
                        A = int(A1 + (float(Add4.split(",")[3]) * 255))  # Alpha channel
                        img.putpixel((w, h), (R, G, B, A))

                    ### Subtract ###
                    if (Subtract4 != "0,0,0,0"):
                        R1, G1, B1, A1 = img.getpixel((w, h))
                        R = int(R1 - (float(Subtract4.split(",")[0]) * 255))
                        G = int(G1 - (float(Subtract4.split(",")[1]) * 255))
                        B = int(B1 - (float(Subtract4.split(",")[2]) * 255))
                        A = int(A1 - (float(Subtract4.split(",")[3]) * 255))  # Alpha channel
                        img.putpixel((w, h), (R, G, B, A))

                    ### Clamp ###
                    rMin = float(Min4.split(",")[0]) * 255
                    gMin = float(Min4.split(",")[1]) * 255
                    bMin = float(Min4.split(",")[2]) * 255
                    aMin = float(Min4.split(",")[3]) * 255  # Alpha channel min

                    rMax = float(Max4.split(",")[0]) * 255
                    gMax = float(Max4.split(",")[1]) * 255
                    bMax = float(Max4.split(",")[2]) * 255
                    aMax = float(Max4.split(",")[3]) * 255  # Alpha channel max

                    R1, G1, B1, A1 = img.getpixel((w, h))

                    R = int(min(max(R1, rMin), rMax))
                    G = int(min(max(G1, gMin), gMax))
                    B = int(min(max(B1, bMin), bMax))
                    A = int(min(max(A1, aMin), aMax))  # Alpha channel

                    img.putpixel((w, h), (R, G, B, A))

            # Save image with RGBA
            img.save(Output)

    class Combine:
        def __init__(self, master):

            frameMaster = ctk.CTkFrame(master,fg_color=c.fgColor)
            frameMaster.pack(fill=Y,expand=TRUE)

            frameTop = ctk.CTkFrame(frameMaster,height=50)
            frameTop.pack(padx=1,pady=1,side=TOP)

            frameScroll = ctk.CTkScrollableFrame(frameMaster,width=400)
            frameScroll.pack(padx=1,pady=1,fill=Y,expand=TRUE)  

            frameBottom = ctk.CTkFrame(frameMaster,height=50)
            frameBottom.pack(padx=1,pady=1,side=BOTTOM)
        
            #### Input ####
            frame1 = ctk.CTkFrame(frameScroll)
            frame1.pack()

            frame2 = ctk.CTkFrame(frameScroll)
            frame2.pack()

            frame3 = ctk.CTkFrame(frameScroll)
            frame3.pack()

            frame4 = ctk.CTkFrame(frameScroll)
            frame4.pack()

            frame01 = ctk.CTkFrame(frame1, width=c.cellW2, height=c.cellH)
            frame01.pack(padx=2, pady=2, side=LEFT)
            frame01.propagate(False)

            frame02 = ctk.CTkFrame(frame2, width=c.cellW2, height=c.cellH)
            frame02.pack(padx=2, pady=2, side=LEFT)
            frame02.propagate(False)

            frame03 = ctk.CTkFrame(frame3, width=c.cellW2, height=c.cellH)
            frame03.pack(padx=2, pady=2, side=LEFT)
            frame03.propagate(False)

            frame04 = ctk.CTkFrame(frame4, width=c.cellW2, height=c.cellH)
            frame04.pack(padx=2, pady=2, side=LEFT)
            frame04.propagate(False)

            
            frame09 = ctk.CTkFrame(frameTop, width=400, height=30)
            frame09.pack(padx=2, pady=1)
            frame09.propagate(False)



            #### OUTPUT DIRECTORY ####
            buttonOut = ctk.CTkButton(frame09, text="Set Output",command=self.set_output_dir, width=100, font=c.sFont)
            buttonOut.pack(pady=2, padx=2, side=RIGHT)

            mainDirectoryOut = ctk.CTkLabel(frame09, text="Output:",width=32, font=c.sFont)
            mainDirectoryOut.pack(pady=2, padx=6, side=LEFT)

            self.mainDirectoryPathOut = ctk.CTkLabel(frame09,  text="Unset", text_color="red", font=c.sFont)
            self.mainDirectoryPathOut.pack(pady=2, padx=6,side=LEFT)

            GenerateButton = ctk.CTkButton(frameBottom, text="Combine", width=c.appWidth, command=self.generate, height=40, font=c.bFont)
            GenerateButton.pack(pady=2, padx=2, side=LEFT)



            #### Red #### 
            frame011 = ctk.CTkFrame(frame01, width=400, height=40)
            frame011.pack(padx=2, pady=1,fill=X,expand=TRUE)

            frame012 = ctk.CTkFrame(frame01, width=400, height=40)
            frame012.pack(padx=2, pady=1,fill=X,expand=TRUE)

            labelRed = ctk.CTkLabel(frame011, text="Red Channel", font=c.mFont)
            labelRed.pack(pady=6, padx=12, side=LEFT)

                #### INPUT FILE ####
            buttonInRed = ctk.CTkButton(frame011, text="Set Red",command=self.set_red_channel, width=100, font=c.sFont)
            buttonInRed.pack(pady=2, padx=2, side=RIGHT)

                #### EXTRACT ####
            self.var21 = ctk.IntVar()
            self.inputExtractRed = ctk.CTkOptionMenu(frame011, variable=self.var21, values=c.ExtractColors, width=85, font=c.sFont)
            self.inputExtractRed.set(c.ExtractColors[0])
            self.inputExtractRed.pack(pady=2, padx=1,side=RIGHT)

            mainDirectoryInRed = ctk.CTkLabel(frame012, text="Input:", font=c.sFont)
            mainDirectoryInRed.pack(pady=2, padx=6, side=LEFT)

            self.mainDirectoryPathInRed = ctk.CTkLabel(frame012, text="Unset", text_color="red", font=c.sFont)
            self.mainDirectoryPathInRed.pack(pady=2, padx=6,side=LEFT)   

            #### Green #### 
            frame021 = ctk.CTkFrame(frame02, width=400, height=40)
            frame021.pack(padx=2, pady=1,fill=X,expand=TRUE)

            frame022 = ctk.CTkFrame(frame02, width=400, height=40)
            frame022.pack(padx=2, pady=1,fill=X,expand=TRUE)

            labelGreen = ctk.CTkLabel(frame021, text="Green Channel", font=c.mFont)
            labelGreen.pack(pady=6, padx=12, side=LEFT)

                #### INPUT FILE ####
            buttonInGreen = ctk.CTkButton(frame021, text="Set Green",command=self.set_green_channel, width=100, font=c.sFont)
            buttonInGreen.pack(pady=2, padx=2, side=RIGHT)

                #### EXTRACT ####
            self.var22 = ctk.IntVar()
            self.inputExtractGreen = ctk.CTkOptionMenu(frame021, variable=self.var22, values=c.ExtractColors, width=85, font=c.sFont)
            self.inputExtractGreen.set(c.ExtractColors[0])
            self.inputExtractGreen.pack(pady=2, padx=1,side=RIGHT)
            
            mainDirectoryInGreen = ctk.CTkLabel(frame022, text="Input:", font=c.sFont)
            mainDirectoryInGreen.pack(pady=2, padx=6, side=LEFT)

            self.mainDirectoryPathInGreen = ctk.CTkLabel(frame022, text="Unset", text_color="red", font=c.sFont)
            self.mainDirectoryPathInGreen.pack(pady=2, padx=6,side=LEFT)   
            

            #### Blue #### 
            frame031 = ctk.CTkFrame(frame03, width=400, height=40)
            frame031.pack(padx=2, pady=1,fill=X,expand=TRUE)

            frame032 = ctk.CTkFrame(frame03, width=400, height=40)
            frame032.pack(padx=2, pady=1,fill=X,expand=TRUE)

            labelBlue = ctk.CTkLabel(frame031, text="Blue Channel", font=c.mFont)
            labelBlue.pack(pady=6, padx=12, side=LEFT)



                #### INPUT FILE ####
            buttonInBlue = ctk.CTkButton(frame031, text="Set Blue",command=self.set_blue_channel, width=100, font=c.sFont)
            buttonInBlue.pack(pady=2, padx=2, side=RIGHT)

                #### EXTRACT ####
            self.var23 = ctk.IntVar()
            self.inputExtractBlue= ctk.CTkOptionMenu(frame031, variable=self.var23, values=c.ExtractColors, width=85, font=c.sFont)
            self.inputExtractBlue.set(c.ExtractColors[0])
            self.inputExtractBlue.pack(pady=2, padx=1,side=RIGHT)
            
            mainDirectoryInBlue = ctk.CTkLabel(frame032, text="Input:", font=c.sFont)
            mainDirectoryInBlue.pack(pady=2, padx=6, side=LEFT)
            
            self.mainDirectoryPathInBlue = ctk.CTkLabel(frame032, text="Unset", text_color="red", font=c.sFont)
            self.mainDirectoryPathInBlue.pack(pady=2, padx=6,side=LEFT)   

            #### Alpha #### 
            frame041 = ctk.CTkFrame(frame04, width=400, height=40)
            frame041.pack(padx=2, pady=1,fill=X,expand=TRUE)

            frame042 = ctk.CTkFrame(frame04, width=400, height=40)
            frame042.pack(padx=2, pady=1,fill=X,expand=TRUE)

            labelAlpha = ctk.CTkLabel(frame041, text="Alpha Channel", font=c.mFont)
            labelAlpha.pack(pady=6, padx=16, side=LEFT)

                #### INPUT FILE ####
            buttonInAlpha = ctk.CTkButton(frame041, text="Set Alpha",command=self.set_alpha_channel, width=100, font=c.sFont)
            buttonInAlpha.pack(pady=2, padx=2, side=RIGHT)   

                #### EXTRACT ####
            self.var24 = ctk.IntVar()
            self.inputExtractAlpha= ctk.CTkOptionMenu(frame041, variable=self.var24, values=c.ExtractColors, width=85, font=c.sFont)
            self.inputExtractAlpha.set(c.ExtractColors[0])
            self.inputExtractAlpha.pack(pady=2, padx=1,side=RIGHT)

            
            mainDirectoryInAlpha = ctk.CTkLabel(frame042, text="Input:", font=c.sFont)
            mainDirectoryInAlpha.pack(pady=2, padx=6, side=LEFT)

            self.mainDirectoryPathInAlpha = ctk.CTkLabel(frame042, text="Unset", text_color="red", font=c.sFont)
            self.mainDirectoryPathInAlpha.pack(pady=2, padx=6,side=LEFT)   



        def set_red_channel(self):
            self.InputFilePathRed = filedialog.askopenfilename(title="Input Red Channel")
            if (self.InputFilePathRed != ""):
                self.InputFilePathRed1 = self.InputFilePathRed.split("/")[-1]
                self.mainDirectoryPathInRed.configure(text=self.InputFilePathRed1,text_color="white")

        def set_green_channel(self):
            self.InputFilePathGreen = filedialog.askopenfilename(title="Input Green Channel")
            if (self.InputFilePathGreen != ""):
                self.InputFilePathGreen1 = self.InputFilePathGreen.split("/")[-1]
                self.mainDirectoryPathInGreen.configure(text=self.InputFilePathGreen1,text_color="white")

        def set_blue_channel(self):
            self.InputFilePathBlue = filedialog.askopenfilename(title="Input Blue Channel")
            if (self.InputFilePathBlue != ""):
                self.InputFilePathBlue1 = self.InputFilePathBlue.split("/")[-1]
                self.mainDirectoryPathInBlue.configure(text=self.InputFilePathBlue1,text_color="white")

        def set_alpha_channel(self):
            self.InputFilePathAlpha = filedialog.askopenfilename(title="Input Alpha Channel")
            if (self.InputFilePathAlpha != ""):
                self.InputFilePathAlpha1 = self.InputFilePathAlpha.split("/")[-1]
                self.mainDirectoryPathInAlpha.configure(text=self.InputFilePathAlpha1,text_color="white")

        def set_output_dir(self):
            self.OutputFilePath = filedialog.asksaveasfilename(title="Output File")
            if (self.OutputFilePath != ""):
                #self.OutputStatus.configure(text="Ready", text_color="green")
                self.OutputFilePath1 = self.OutputFilePath.split("/")[-1]
                self.mainDirectoryPathOut.configure(text=self.OutputFilePath1,text_color="white",font=c.sFont1)

        InputFilePathRed = ""
        InputFilePathGreen = ""
        InputFilePathBlue = ""
        InputFilePathAlpha = ""


        def generate(self):

            imgInputRed = self.InputFilePathRed  
            extInputRed  = self.inputExtractRed.get()

            imgInputGreen = self.InputFilePathGreen
            extInputGreen  = self.inputExtractGreen.get() 

            imgInputBlue = self.InputFilePathBlue
            extInputBlue = self.inputExtractBlue.get()

            imgInputAlpha = self.InputFilePathAlpha
            extInputAlpha = self.inputExtractAlpha.get()
            
            Output = self.OutputFilePath

            if ( Output != "" ):

                if(imgInputRed == ""):
                    imgRed = Image.new(mode="RGBA", size=(16, 16))
                else:
                    imgRed = Image.open(imgInputRed)
                    imgRed.convert("RGBA")
                    
                if(imgInputGreen == ""):
                    imgGreen = Image.new(mode="RGBA", size=(16, 16))
                else:
                    imgGreen = Image.open(imgInputGreen)
                    imgGreen.convert("RGBA")

                if(imgInputBlue == ""):
                    imgBlue = Image.new(mode="RGBA", size=(16, 16))
                else:
                    imgBlue = Image.open(imgInputBlue)
                    imgBlue.convert("RGBA")

                if(imgInputAlpha == ""):
                    imgAlpha = Image.new(mode="RGBA", size=(16, 16),color=(255,255,255))
                else:
                    imgAlpha = Image.open(imgInputAlpha)
                    imgAlpha.convert("RGBA")
                

                maxsize = max(imgRed.size,imgGreen.size,imgBlue.size,imgAlpha.size)
                Width, Height = maxsize

                imgNew= Image.new(mode="RGBA", size=(Width, Height))

                print(f"w={Width} , h={Height}")
                print(extInputRed)

                imgRed = imgRed.resize((Width,Height),resample=Image.LANCZOS)
                imgGreen = imgGreen.resize((Width,Height),resample=Image.LANCZOS)
                imgBlue = imgBlue.resize((Width,Height),resample=Image.LANCZOS)
                imgAlpha = imgAlpha.resize((Width,Height),resample=Image.LANCZOS)
                
                print(imgRed.size)
                print(imgGreen.size)
                print(imgBlue.size)
                print(imgAlpha.size)

                def pixel_color(imgRed,w,h,extInputRed):

                    Pixel = imgRed.getpixel((w, h))
                    if isinstance(Pixel, int):
                        pR = pG = pB = pA = Pixel
                    else:
                        pR, pG, pB, *pRest = Pixel
                        if(pRest):
                            pA = pRest[0] 
                        else:
                            pA = 255

                    Channels = {
                        "Red": pR,
                        "Green": pG,
                        "Blue": pB,
                        "Alpha": pA
                    }

                    return Channels.get(extInputRed)
                
                R, G, B, A = 0,0,0,255
                for w in range(Width):
                    for h in range(Height):

                        R = pixel_color(imgRed,w,h,extInputRed)
                        G = pixel_color(imgGreen,w,h,extInputGreen)
                        B = pixel_color(imgBlue,w,h,extInputBlue)               
                        A = pixel_color(imgAlpha,w,h,extInputAlpha)

                        #print(f"R={type(R)} G={type(G)} B={type(B)} A={type(A)}")
                        imgNew.putpixel((w, h), (R, G, B, A))

                imgNew.save(Output)

    class Separate:
        def __init__(self, master):

            frameMaster = ctk.CTkFrame(master,fg_color=c.fgColor)
            frameMaster.pack(fill=Y,expand=TRUE)

            frameTop = ctk.CTkFrame(frameMaster,height=50)
            frameTop.pack(padx=1,pady=1,side=TOP)

            frameScroll = ctk.CTkScrollableFrame(frameMaster,width=400)
            frameScroll.pack(padx=1,pady=1,fill=Y,expand=TRUE)  

            frameBottom = ctk.CTkFrame(frameMaster,height=50)
            frameBottom.pack(padx=1,pady=1,side=BOTTOM)
        
            #### Input ####
            frame1 = ctk.CTkFrame(frameScroll)
            frame1.pack()

            frame2 = ctk.CTkFrame(frameScroll)
            frame2.pack()

            frame3 = ctk.CTkFrame(frameScroll)
            frame3.pack()

            frame4 = ctk.CTkFrame(frameScroll)
            frame4.pack()

            frame01 = ctk.CTkFrame(frame1, width=c.cellW2, height=c.cellH)
            frame01.pack(padx=2, pady=2, side=LEFT)
            frame01.propagate(False)

            frame02 = ctk.CTkFrame(frame2, width=c.cellW2, height=c.cellH)
            frame02.pack(padx=2, pady=2, side=LEFT)
            frame02.propagate(False)

            frame03 = ctk.CTkFrame(frame3, width=c.cellW2, height=c.cellH)
            frame03.pack(padx=2, pady=2, side=LEFT)
            frame03.propagate(False)

            frame04 = ctk.CTkFrame(frame4, width=c.cellW2, height=c.cellH)
            frame04.pack(padx=2, pady=2, side=LEFT)
            frame04.propagate(False)

            
            frame09 = ctk.CTkFrame(frameTop, width=400, height=30)
            frame09.pack(padx=2, pady=1)
            frame09.propagate(False)



            #### Input DIRECTORY ####
            buttonIn = ctk.CTkButton(frame09, text="Set Input",command=self.set_input_dir, width=100, font=c.sFont)
            buttonIn.pack(pady=2, padx=2, side=RIGHT)

            mainDirectoryIn = ctk.CTkLabel(frame09, text="Input:",width=32, font=c.sFont)
            mainDirectoryIn.pack(pady=2, padx=6, side=LEFT)

            self.mainDirectoryPathIn = ctk.CTkLabel(frame09,  text="Unset", text_color="red", font=c.sFont)
            self.mainDirectoryPathIn.pack(pady=2, padx=6,side=LEFT)

            GenerateButton = ctk.CTkButton(frameBottom, text="Separate", width=c.appWidth, command=self.generate, height=40, font=c.bFont)
            GenerateButton.pack(pady=2, padx=2, side=LEFT)



            #### Red #### 
            frame011 = ctk.CTkFrame(frame01, width=400, height=40)
            frame011.pack(padx=2, pady=1,fill=X,expand=TRUE)

            frame012 = ctk.CTkFrame(frame01, width=400, height=40)
            frame012.pack(padx=2, pady=1,fill=X,expand=TRUE)

            labelRed = ctk.CTkLabel(frame011, text="Red Channel", font=c.mFont)
            labelRed.pack(pady=6, padx=12, side=LEFT)

                #### OUTPUT FILE ####
            buttonOutRed = ctk.CTkButton(frame011, text="Set Red",command=self.set_red_channel, width=100, font=c.sFont)
            buttonOutRed.pack(pady=2, padx=2, side=RIGHT)

            mainDirectoryOutRed = ctk.CTkLabel(frame012, text="Output:", font=c.sFont)
            mainDirectoryOutRed.pack(pady=2, padx=6, side=LEFT)

            self.mainDirectoryPathOutRed = ctk.CTkLabel(frame012, text="Unset", text_color="red", font=c.sFont)
            self.mainDirectoryPathOutRed.pack(pady=2, padx=6,side=LEFT)   

            #### Green #### 
            frame021 = ctk.CTkFrame(frame02, width=400, height=40)
            frame021.pack(padx=2, pady=1,fill=X,expand=TRUE)

            frame022 = ctk.CTkFrame(frame02, width=400, height=40)
            frame022.pack(padx=2, pady=1,fill=X,expand=TRUE)

            labelGreen = ctk.CTkLabel(frame021, text="Green Channel", font=c.mFont)
            labelGreen.pack(pady=6, padx=12, side=LEFT)

                #### OUTPUT FILE ####
            buttonOutGreen = ctk.CTkButton(frame021, text="Set Green",command=self.set_green_channel, width=100, font=c.sFont)
            buttonOutGreen.pack(pady=2, padx=2, side=RIGHT)

            
            mainDirectoryOutGreen = ctk.CTkLabel(frame022, text="Output:", font=c.sFont)
            mainDirectoryOutGreen.pack(pady=2, padx=6, side=LEFT)

            self.mainDirectoryPathOutGreen = ctk.CTkLabel(frame022, text="Unset", text_color="red", font=c.sFont)
            self.mainDirectoryPathOutGreen.pack(pady=2, padx=6,side=LEFT)   
            

            #### Blue #### 
            frame031 = ctk.CTkFrame(frame03, width=400, height=40)
            frame031.pack(padx=2, pady=1,fill=X,expand=TRUE)

            frame032 = ctk.CTkFrame(frame03, width=400, height=40)
            frame032.pack(padx=2, pady=1,fill=X,expand=TRUE)

            labelBlue = ctk.CTkLabel(frame031, text="Blue Channel", font=c.mFont)
            labelBlue.pack(pady=6, padx=12, side=LEFT)


                #### OUTPUT FILE ####
            buttonOutBlue = ctk.CTkButton(frame031, text="Set Blue",command=self.set_blue_channel, width=100, font=c.sFont)
            buttonOutBlue.pack(pady=2, padx=2, side=RIGHT)

            
            mainDirectoryOutBlue = ctk.CTkLabel(frame032, text="Output:", font=c.sFont)
            mainDirectoryOutBlue.pack(pady=2, padx=6, side=LEFT)
            
            self.mainDirectoryPathOutBlue = ctk.CTkLabel(frame032, text="Unset", text_color="red", font=c.sFont)
            self.mainDirectoryPathOutBlue.pack(pady=2, padx=6,side=LEFT)   

            #### Alpha #### 
            frame041 = ctk.CTkFrame(frame04, width=400, height=40)
            frame041.pack(padx=2, pady=1,fill=X,expand=TRUE)

            frame042 = ctk.CTkFrame(frame04, width=400, height=40)
            frame042.pack(padx=2, pady=1,fill=X,expand=TRUE)

            labelAlpha = ctk.CTkLabel(frame041, text="Alpha Channel", font=c.mFont)
            labelAlpha.pack(pady=6, padx=16, side=LEFT)

                #### OUTPUT FILE ####
            buttonOutAlpha = ctk.CTkButton(frame041, text="Set Alpha",command=self.set_alpha_channel, width=100, font=c.sFont)
            buttonOutAlpha.pack(pady=2, padx=2, side=RIGHT)   
            
            mainDirectoryOutAlpha = ctk.CTkLabel(frame042, text="Output:", font=c.sFont)
            mainDirectoryOutAlpha.pack(pady=2, padx=6, side=LEFT)

            self.mainDirectoryPathOutAlpha = ctk.CTkLabel(frame042, text="Unset", text_color="red", font=c.sFont)
            self.mainDirectoryPathOutAlpha.pack(pady=2, padx=6,side=LEFT)   



        def set_red_channel(self):
            self.OutputFilePathRed = filedialog.asksaveasfilename(title="Output Red Channel")
            if (self.OutputFilePathRed != ""):
                self.OutputFilePathRed1 = self.OutputFilePathRed.split("/")[-1]
                self.mainDirectoryPathOutRed.configure(text=self.OutputFilePathRed1,text_color="white")

        def set_green_channel(self):
            self.OutputFilePathGreen = filedialog.asksaveasfilename(title="Output Green Channel")
            if (self.OutputFilePathGreen != ""):
                self.OutputFilePathGreen1 = self.OutputFilePathGreen.split("/")[-1]
                self.mainDirectoryPathOutGreen.configure(text=self.OutputFilePathGreen1,text_color="white")

        def set_blue_channel(self):
            self.OutputFilePathBlue = filedialog.asksaveasfilename(title="Output Blue Channel")
            if (self.OutputFilePathBlue != ""):
                self.OutputFilePathBlue1 = self.OutputFilePathBlue.split("/")[-1]
                self.mainDirectoryPathOutBlue.configure(text=self.OutputFilePathBlue1,text_color="white")

        def set_alpha_channel(self):
            self.OutputFilePathAlpha = filedialog.asksaveasfilename(title="Output Alpha Channel")
            if (self.OutputFilePathAlpha != ""):
                self.OutputFilePathAlpha1 = self.OutputFilePathAlpha.split("/")[-1]
                self.mainDirectoryPathOutAlpha.configure(text=self.OutputFilePathAlpha1,text_color="white")

        def set_input_dir(self):
            self.InputFilePath = filedialog.askopenfilename(title="Output File")
            if (self.InputFilePath != ""):
                #self.OutputStatus.configure(text="Ready", text_color="green")
                self.InputFilePath1 = self.InputFilePath.split("/")[-1]
                self.mainDirectoryPathIn.configure(text=self.InputFilePath1,text_color="white",font=c.sFont1)

        OutputFilePathRed = ""
        OutputFilePathGreen = ""
        OutputFilePathBlue = ""
        OutputFilePathAlpha = ""


        def generate(self):

            imgOutputRed = self.OutputFilePathRed  
            imgOutputGreen = self.OutputFilePathGreen
            imgOutputBlue = self.OutputFilePathBlue
            imgOutputAlpha = self.OutputFilePathAlpha

            
            Input = self.InputFilePath

            if ( Input != "" ):
                imgInput = Image.open(Input)
                maxsize = imgInput.size
                Width, Height = maxsize

                if(imgOutputRed != ""):
                    imgRed = Image.new(mode="L", size=(Width, Height))
                    
                if(imgOutputGreen != ""):
                    imgGreen = Image.new(mode="L", size=(Width, Height))

                if(imgOutputBlue != ""):
                    imgBlue = Image.new(mode="L", size=(Width, Height))

                if(imgOutputAlpha != ""):
                    imgAlpha = Image.new(mode="L",size=(Width, Height))

                R, G, B, A = 0,0,0,255
                
                for w in range(Width):
                    for h in range(Height):

                        Pixel = imgInput.getpixel((w,h))
                        R,G,B,A = Pixel

                        if(imgOutputRed != ""):
                            imgRed.putpixel((w, h), (R))

                        if(imgOutputGreen != ""):
                            imgGreen.putpixel((w, h), (G))

                        if(imgOutputBlue != ""):
                            imgBlue.putpixel((w, h), (B))

                        if(imgOutputAlpha != ""):
                            imgAlpha.putpixel((w, h), (A))


                if(imgOutputRed != ""):
                    imgRed.save(imgOutputRed)

                if(imgOutputGreen != ""):
                    imgGreen.save(imgOutputGreen)

                if(imgOutputBlue != ""):
                    imgBlue.save(imgOutputBlue)  

                if(imgOutputAlpha != ""):
                    imgAlpha.save(imgOutputAlpha)             

    class Mask:
        def __init__(self, master):

            frameMaster = ctk.CTkFrame(master,fg_color=c.fgColor)
            frameMaster.pack(fill=Y,expand=TRUE)

            frameTop = ctk.CTkFrame(frameMaster,height=50)
            frameTop.pack(padx=1,pady=1,side=TOP)

            frameScroll = ctk.CTkScrollableFrame(frameMaster,width=400)
            frameScroll.pack(padx=1,pady=1,fill=Y,expand=TRUE)  

            frameBottom = ctk.CTkFrame(frameMaster,height=50)
            frameBottom.pack(padx=1,pady=1,side=BOTTOM)
        
            #### Input ####
            frame1 = ctk.CTkFrame(frameScroll)
            frame1.pack()

            frame2 = ctk.CTkFrame(frameScroll)
            frame2.pack()

            frame3 = ctk.CTkFrame(frameScroll)
            frame3.pack()


            frame01 = ctk.CTkFrame(frame1, width=c.cellW2, height=c.cellH)
            frame01.pack(padx=2, pady=2, side=LEFT)
            frame01.propagate(False)

            frame02 = ctk.CTkFrame(frame2, width=c.cellW2, height=c.cellH)
            frame02.pack(padx=2, pady=2, side=LEFT)
            frame02.propagate(False)

            frame03 = ctk.CTkFrame(frame3, width=c.cellW2, height=c.cellH/2)
            frame03.pack(padx=2, pady=2, side=LEFT)
            frame03.propagate(False)


            
            frame09 = ctk.CTkFrame(frameTop, width=400, height=30)
            frame09.pack(padx=2, pady=1)
            frame09.propagate(False)



            #### OUTPUT DIRECTORY ####
            buttonOut = ctk.CTkButton(frame09, text="Set Output",command=self.set_output_dir, width=100, font=c.sFont)
            buttonOut.pack(pady=2, padx=2, side=RIGHT)

            mainDirectoryOut = ctk.CTkLabel(frame09, text="Output:",width=32, font=c.sFont)
            mainDirectoryOut.pack(pady=2, padx=6, side=LEFT)

            self.mainDirectoryPathOut = ctk.CTkLabel(frame09,  text="Unset", text_color="red", font=c.sFont)
            self.mainDirectoryPathOut.pack(pady=2, padx=6,side=LEFT)

            GenerateButton = ctk.CTkButton(frameBottom, text="Mask", width=c.appWidth, command=self.generate, height=40, font=c.bFont)
            GenerateButton.pack(pady=2, padx=2, side=LEFT)



            #### A #### 
            frame011 = ctk.CTkFrame(frame01, width=400, height=40)
            frame011.pack(padx=2, pady=1,fill=X,expand=TRUE)

            frame012 = ctk.CTkFrame(frame01, width=400, height=40)
            frame012.pack(padx=2, pady=1,fill=X,expand=TRUE)

            labelA = ctk.CTkLabel(frame011, text="Image A", font=c.mFont)
            labelA.pack(pady=6, padx=12, side=LEFT)

                #### INPUT FILE ####
            buttonInA = ctk.CTkButton(frame011, text="Set A",command=self.set_a_img, width=100, font=c.sFont)
            buttonInA.pack(pady=2, padx=2, side=RIGHT)

                #### EXTRACT ####
            self.var21 = ctk.IntVar()
            self.inputExtractA = ctk.CTkOptionMenu(frame011, variable=self.var21, values=c.ExtractColors, width=85, font=c.sFont)
            self.inputExtractA.set(c.ExtractColors[0])
            self.inputExtractA.pack(pady=2, padx=1,side=RIGHT)

            mainDirectoryInA = ctk.CTkLabel(frame012, text="Input:", font=c.sFont)
            mainDirectoryInA.pack(pady=2, padx=6, side=LEFT)

            self.mainDirectoryPathInA = ctk.CTkLabel(frame012, text="Unset", text_color="red", font=c.sFont)
            self.mainDirectoryPathInA.pack(pady=2, padx=6,side=LEFT)   

            #### B #### 
            frame021 = ctk.CTkFrame(frame02, width=400, height=40)
            frame021.pack(padx=2, pady=1,fill=X,expand=TRUE)

            frame022 = ctk.CTkFrame(frame02, width=400, height=40)
            frame022.pack(padx=2, pady=1,fill=X,expand=TRUE)

            labelB = ctk.CTkLabel(frame021, text="Image B", font=c.mFont)
            labelB.pack(pady=6, padx=12, side=LEFT)

                #### INPUT FILE ####
            buttonInB = ctk.CTkButton(frame021, text="Set B",command=self.set_b_img, width=100, font=c.sFont)
            buttonInB.pack(pady=2, padx=2, side=RIGHT)

                #### EXTRACT ####
            self.var22 = ctk.IntVar()
            self.inputExtractB = ctk.CTkOptionMenu(frame021, variable=self.var22, values=c.ExtractColors, width=85, font=c.sFont)
            self.inputExtractB.set(c.ExtractColors[0])
            self.inputExtractB.pack(pady=2, padx=1,side=RIGHT)
            
            mainDirectoryInB = ctk.CTkLabel(frame022, text="Input:", font=c.sFont)
            mainDirectoryInB.pack(pady=2, padx=6, side=LEFT)

            self.mainDirectoryPathInB = ctk.CTkLabel(frame022, text="Unset", text_color="red", font=c.sFont)
            self.mainDirectoryPathInB.pack(pady=2, padx=6,side=LEFT)   
            

            #### Mask #### 
            frame031 = ctk.CTkFrame(frame03, width=400, height=40)
            frame031.pack(padx=2, pady=1,fill=X,expand=TRUE)


            extractMethod = ["A * B","A + B","A - B","B - A"]
                #### EXTRACT ####
            self.var23 = ctk.IntVar()
            self.inputExtractMethod = ctk.CTkSegmentedButton(frame031, variable=self.var23, values=extractMethod, width=100, font=c.bFont)
            self.inputExtractMethod.set(extractMethod[0])
            self.inputExtractMethod.pack(pady=2, padx=1)



        def set_a_img(self):
            self.InputFilePathRed = filedialog.askopenfilename(title="Input A Image")
            if (self.InputFilePathRed != ""):
                self.InputFilePathRed1 = self.InputFilePathRed.split("/")[-1]
                self.mainDirectoryPathInRed.configure(text=self.InputFilePathRed1,text_color="white")

        def set_b_img(self):
            self.InputFilePathGreen = filedialog.askopenfilename(title="Input B Image")
            if (self.InputFilePathGreen != ""):
                self.InputFilePathGreen1 = self.InputFilePathGreen.split("/")[-1]
                self.mainDirectoryPathInGreen.configure(text=self.InputFilePathGreen1,text_color="white")



        def set_output_dir(self):
            self.OutputFilePath = filedialog.asksaveasfilename(title="Output File")
            if (self.OutputFilePath != ""):
                #self.OutputStatus.configure(text="Ready", text_color="green")
                self.OutputFilePath1 = self.OutputFilePath.split("/")[-1]
                self.mainDirectoryPathOut.configure(text=self.OutputFilePath1,text_color="white",font=c.sFont1)

        InputFilePathRed = ""
        InputFilePathGreen = ""
        InputFilePathBlue = ""
        InputFilePathAlpha = ""


        def generate(self):

            imgInputRed = self.InputFilePathRed  
            extInputRed  = self.inputExtractRed.get()

            imgInputGreen = self.InputFilePathGreen
            extInputGreen  = self.inputExtractGreen.get() 

            imgInputBlue = self.InputFilePathBlue
            extInputBlue = self.inputExtractBlue.get()

            imgInputAlpha = self.InputFilePathAlpha
            extInputAlpha = self.inputExtractAlpha.get()
            
            Output = self.OutputFilePath

            if ( Output != "" ):

                if(imgInputRed == ""):
                    imgRed = Image.new(mode="RGBA", size=(16, 16))
                else:
                    imgRed = Image.open(imgInputRed)
                    imgRed.convert("RGBA")
                    
                if(imgInputGreen == ""):
                    imgGreen = Image.new(mode="RGBA", size=(16, 16))
                else:
                    imgGreen = Image.open(imgInputGreen)
                    imgGreen.convert("RGBA")

                if(imgInputBlue == ""):
                    imgBlue = Image.new(mode="RGBA", size=(16, 16))
                else:
                    imgBlue = Image.open(imgInputBlue)
                    imgBlue.convert("RGBA")

                if(imgInputAlpha == ""):
                    imgAlpha = Image.new(mode="RGBA", size=(16, 16),color=(255,255,255))
                else:
                    imgAlpha = Image.open(imgInputAlpha)
                    imgAlpha.convert("RGBA")
                

                maxsize = max(imgRed.size,imgGreen.size,imgBlue.size,imgAlpha.size)
                Width, Height = maxsize

                imgNew= Image.new(mode="RGBA", size=(Width, Height))

                print(f"w={Width} , h={Height}")
                print(extInputRed)

                imgRed = imgRed.resize((Width,Height),resample=Image.LANCZOS)
                imgGreen = imgGreen.resize((Width,Height),resample=Image.LANCZOS)
                imgBlue = imgBlue.resize((Width,Height),resample=Image.LANCZOS)
                imgAlpha = imgAlpha.resize((Width,Height),resample=Image.LANCZOS)
                
                print(imgRed.size)
                print(imgGreen.size)
                print(imgBlue.size)
                print(imgAlpha.size)

                def pixel_color(imgRed,w,h,extInputRed):

                    Pixel = imgRed.getpixel((w, h))
                    if isinstance(Pixel, int):
                        pR = pG = pB = pA = Pixel
                    else:
                        pR, pG, pB, *pRest = Pixel
                        if(pRest):
                            pA = pRest[0] 
                        else:
                            pA = 255

                    Channels = {
                        "Red": pR,
                        "Green": pG,
                        "Blue": pB,
                        "Alpha": pA
                    }

                    return Channels.get(extInputRed)
                
                R, G, B, A = 0,0,0,255
                for w in range(Width):
                    for h in range(Height):

                        R = pixel_color(imgRed,w,h,extInputRed)
                        G = pixel_color(imgGreen,w,h,extInputGreen)
                        B = pixel_color(imgBlue,w,h,extInputBlue)               
                        A = pixel_color(imgAlpha,w,h,extInputAlpha)

                        #print(f"R={type(R)} G={type(G)} B={type(B)} A={type(A)}")
                        imgNew.putpixel((w, h), (R, G, B, A))

                imgNew.save(Output)