import os
from tkinter import *
from tkinter import filedialog
from PIL import Image
import customtkinter as ctk
import constants as c 


toolVersion = c.toolVersion
cellH = c.cellH
cellW = c.cellW
cellW2 = c.cellW2
appWidth = c.appWidth
appHeight = c.appHeight
bgColor = c.bgColor
fgColor = c.fgColor
sFont1 = c.sFont1
sFont = c.sFont
mFont = c.mFont
bFont = c.bFont
exten = c.Extensions
extract = c.ExtractColors

#### Initialize Window ####
root = Tk()
root.configure(bg=bgColor)
root.title("Pixel Procesor" + str(toolVersion))
root.iconbitmap('S:\GitHub\PixelProcesor\img\AA_icon.ico')
root.resizable(FALSE, TRUE)
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
appXpos = int((screenWidth / 2) - (appWidth / 2))
appYpos = int((screenHeight / 2) - (appHeight / 2))
root.geometry(f'{appWidth}x{appHeight}+{appXpos}+{appYpos}')

# Create the tab view (this is the equivalent of a tabbed frame)
tab_view = ctk.CTkTabview(root)
tab_view.pack(expand=True, fill="both")

# Add tabs to the tab view
tab1 = tab_view.add("Solid")
tab2 = tab_view.add("Gradient")
tab3 = tab_view.add("Math")
tab4 = tab_view.add("Combine")
tab5 = tab_view.add("Separate")
tab6 = tab_view.add("Mask")
tab7 = tab_view.add("Misc")



my_font = ctk.CTkFont(size=15)  # Font object
for button in tab_view._segmented_button._buttons_dict.values():
    button.configure(height=32, font=my_font)  # Change font using font object


class Solid:
    def __init__(self, master):
        self.Path = ""

        frameMaster = ctk.CTkFrame(master,fg_color=fgColor)
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

        frame01 = ctk.CTkFrame(frame1, width=cellW, height=cellH)
        frame01.pack(padx=2, pady=2, side=LEFT)
        frame01.propagate(False)

        frame02 = ctk.CTkFrame(frame1, width=cellW, height=cellH)
        frame02.pack(padx=2, pady=2, side=LEFT)
        frame02.propagate(False)

        frame03 = ctk.CTkFrame(frame2, width=cellW, height=cellH)
        frame03.pack(padx=2, pady=2, side=LEFT)
        frame03.propagate(False)

        frame04 = ctk.CTkFrame(frame2, width=cellW, height=cellH)
        frame04.pack(padx=2, pady=2, side=LEFT)
        frame04.propagate(False)

        frame06 = ctk.CTkFrame(frameTop, width=400, height=30)
        frame06.pack(padx=2, pady=2)
        frame06.propagate(False)
        

        #### OUTPUT DIRECTORY ####
        button = ctk.CTkButton(frame06, text="Set Output", width=100, command=self.set_directory, font=sFont)
        button.pack(pady=2, padx=2,side=RIGHT)
        
        mainDirectory = ctk.CTkLabel(frame06, text="Output:", font=sFont)
        mainDirectory.pack(pady=2, padx=6, side=LEFT)

        #self.mainDirectoryStatus = ctk.CTkLabel(frame06, text="Unset", text_color="red", font=sFont)
        #self.mainDirectoryStatus.pack(pady=2, padx=6, side=LEFT)

        self.mainDirectoryPath = ctk.CTkLabel(frame06, text="Unset", text_color="red", font=sFont)
        self.mainDirectoryPath.pack(pady=2, padx=6, side=LEFT)


        generateButton = ctk.CTkButton(frameBottom, text="Export Solid Color", width=appWidth, height=40, command=self.generate, font=bFont)
        generateButton.pack(pady=2, padx=2,side=LEFT)


        #### HEX ####
        self.inputHex = StringVar()
        labelHex = ctk.CTkLabel(frame01, text="COLOR (RGBA)", font=mFont)
        labelHex.pack(pady=6, padx=16)

        self.inputHexEntry = ctk.CTkEntry(frame01, width=128, textvariable=self.inputHex, font=sFont)
        self.inputHexEntry.pack(pady=6, padx=16)
        self.inputHexEntry.insert(0, "1, 0.5, 1, 1")

        #### SIZE ####
        labelSize = ctk.CTkLabel(frame02, text="SIZE", font=mFont)
        labelSize.pack(pady=6, padx=16)

        self.inputSize = ctk.CTkEntry(frame02, width=128, font=sFont)
        self.inputSize.pack(pady=6, padx=16)
        self.inputSize.insert(0, "512x512")

        #### FILENAME ####
        labelFilename = ctk.CTkLabel(frame03, text="FILENAME", font=mFont)
        labelFilename.pack(pady=6, padx=16)

        self.inputFilename = ctk.CTkEntry(frame03, width=128, font=sFont)
        self.inputFilename.pack(pady=6, padx=16)
        self.inputFilename.insert(0, "T_SolidColor")

        #### FILETYPE ####
        labelFiletype = ctk.CTkLabel(frame04, text="FILETYPE", font=mFont)
        labelFiletype.pack(pady=6, padx=16)


        self.var2 = ctk.IntVar()
        self.inputFiletype = ctk.CTkOptionMenu(frame04, variable=self.var2, values=exten, width=128, font=sFont)
        self.inputFiletype.set(exten[0])
        self.inputFiletype.pack(pady=6, padx=16)


    def set_directory(self):
        self.Path = filedialog.askdirectory(title="Directory")
        if self.Path:
            #self.mainDirectoryStatus.configure(text="Ready", text_color="green")
            self.mainDirectoryPath.configure(text=self.Path,text_color="white")

    def generate(self):
        Color = self.inputHexEntry.get()
        Size = self.inputSize.get()
        OutputDir = self.Path
        Filename = self.inputFilename.get()
        Filetype = self.inputFiletype.get()

        if not OutputDir:
            print("No output directory selected!")
            return
        Filetype = Filetype.lower()
        Width, Height = map(int, Size.split('x'))
        Color.replace(" ","")
        img = Image.new(mode="RGBA", size=(Width, Height))
        R1, G1, B1, A1 = map(float, Color.split(","))

        for w in range(Width):
            for h in range(Height):
                R = int(R1 * 255 )
                G = int(G1 * 255 )
                B = int(B1 * 255 )
                A = int(A1 * 255)
                img.putpixel((w, h), (R, G, B))
        img.putalpha(A)
                
        full_path = os.path.join(OutputDir, Filename + "."+Filetype)

        img.save(full_path)

class Gradient:
    def __init__(self, master):
        self.Path = ""
        
        frameMaster = ctk.CTkFrame(master,fg_color=fgColor)
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

        frame01 = ctk.CTkFrame(frame1, width=cellW, height=cellH)
        frame01.pack(padx=2, pady=2, side=LEFT)
        frame01.propagate(False)

        frame02 = ctk.CTkFrame(frame1, width=cellW, height=cellH)
        frame02.pack(padx=2, pady=2, side=LEFT)
        frame02.propagate(False)

        frame03 = ctk.CTkFrame(frame2, width=cellW, height=cellH)
        frame03.pack(padx=2, pady=2, side=LEFT)
        frame03.propagate(False)

        frame04 = ctk.CTkFrame(frame2, width=cellW, height=cellH)
        frame04.pack(padx=2, pady=2, side=LEFT)
        frame04.propagate(False)

        frame05 = ctk.CTkFrame(frame3, width=cellW, height=cellH)
        frame05.pack(padx=2, pady=2, side=LEFT)
        frame05.propagate(False)

        frame06 = ctk.CTkFrame(frame3, width=cellW, height=cellH)
        frame06.pack(padx=2, pady=2, side=LEFT)
        frame06.propagate(False)

        frame07 = ctk.CTkFrame(frameTop, width=400, height=30)
        frame07.pack(padx=2, pady=2)
        frame07.propagate(False)


        #### OUTPUT DIRECTORY ####
        button = ctk.CTkButton(frame07, text="Set Output", width=100, command=self.set_output_dir, font=sFont)
        button.pack(pady=2, padx=2, side=RIGHT)

        mainDirectory = ctk.CTkLabel(frame07, text="Output:", font=sFont)
        mainDirectory.pack(pady=2, padx=6, side=LEFT)

        #self.mainDirectoryStatus = ctk.CTkLabel(frame08, text="Unset", font=sFont, text_color="red")
        #self.mainDirectoryStatus.pack(pady=2, padx=6, side=LEFT)

        self.mainDirectoryPath = ctk.CTkLabel(frame07, text="Unset", text_color="red", font=sFont)
        self.mainDirectoryPath.pack(pady=2, padx=6,side=LEFT)


        GenerateButton = ctk.CTkButton(frameBottom, text="Export Gradient", width=appWidth, height=40, command=self.generate, font=bFont)
        GenerateButton.pack(pady=2, padx=2, side=LEFT)



        #### COLOR 1 ####
        labelColor1 = ctk.CTkLabel(frame01, text="COLOR 1 (RGB)", font=mFont)
        labelColor1.pack(pady=6, padx=16)

        self.inputColor1 = ctk.CTkEntry(frame01, width=128, font=sFont)
        self.inputColor1.pack(pady=6, padx=16)
        self.inputColor1.insert(0, "0,0,0")

        #### COLOR 2 ####
        labelColor2 = ctk.CTkLabel(frame02, text="COLOR 2 (RGB)", font=mFont)
        labelColor2.pack(pady=6, padx=16)

        self.inputColor2 = ctk.CTkEntry(frame02, width=128, font=sFont)
        self.inputColor2.pack(pady=6, padx=16)
        self.inputColor2.insert(0, "1,1,1")

        #### FILENAME ####
        labelFilename = ctk.CTkLabel(frame03, text="FILENAME", font=mFont)
        labelFilename.pack(pady=6, padx=16)

        self.inputFilename = ctk.CTkEntry(frame03, width=128, font=sFont)
        self.inputFilename.pack(pady=6, padx=16)
        self.inputFilename.insert(0, "T_Gradient")

        #### SIZE ####
        labelSize = ctk.CTkLabel(frame04, text="SIZE", font=mFont)
        labelSize.pack(pady=6, padx=16)

        self.inputSize = ctk.CTkEntry(frame04, width=128, font=sFont)
        self.inputSize.pack(pady=6, padx=16)
        self.inputSize.insert(0, "512x512")

        #### Orientation ####
        labelOrient = ctk.CTkLabel(frame05, text="ORIENTATION", font=mFont)
        labelOrient.pack(pady=6, padx=16)
        
        orient = ["HORIZ","HORIZ FLIP","VERTI","VERTI FLIP"]
        
        self.var1 = ctk.IntVar()
        self.inputFlip = ctk.CTkOptionMenu(frame05, variable=self.var1, values=orient, width=128, font=sFont)
        self.inputFlip.set(orient[0])
        self.inputFlip.pack(pady=6, padx=16)

        #### FILETYPE ####
        labelFiletype = ctk.CTkLabel(frame06, text="FILETYPE", font=mFont)
        labelFiletype.pack(pady=6, padx=16)

        self.var2 = ctk.IntVar()
        self.inputFiletype = ctk.CTkOptionMenu(frame06, variable=self.var2, values=exten, width=128, font=sFont)
        self.inputFiletype.set(exten[0])
        self.inputFiletype.pack(pady=6, padx=16)

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

        frameMaster = ctk.CTkFrame(master,fg_color=fgColor)
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

        frame01 = ctk.CTkFrame(frame1, width=cellW, height=cellH)
        frame01.pack(padx=2, pady=2, side=LEFT)
        frame01.propagate(False)

        frame02 = ctk.CTkFrame(frame1, width=cellW, height=cellH)
        frame02.pack(padx=2, pady=2, side=LEFT)
        frame02.propagate(False)

        frame03 = ctk.CTkFrame(frame2, width=cellW, height=cellH)
        frame03.pack(padx=2, pady=2, side=LEFT)
        frame03.propagate(False)

        frame04 = ctk.CTkFrame(frame2, width=cellW, height=cellH)
        frame04.pack(padx=2, pady=2, side=LEFT)
        frame04.propagate(False)

        frame05 = ctk.CTkFrame(frame3, width=cellW, height=cellH)
        frame05.pack(padx=2, pady=2, side=LEFT)
        frame05.propagate(False)

        frame06 = ctk.CTkFrame(frame3, width=cellW, height=cellH)
        frame06.pack(padx=2, pady=2, side=LEFT)
        frame06.propagate(False)

        frame08 = ctk.CTkFrame(frameTop, width=400, height=30)
        frame08.pack(padx=2, pady=1)
        frame08.propagate(False)
        
        frame09 = ctk.CTkFrame(frameTop, width=400, height=30)
        frame09.pack(padx=2, pady=1)
        frame09.propagate(False)



        #### INPUT FILE ####
        buttonIn = ctk.CTkButton(frame08, text="Set Input",command=self.set_input_dir, width=100, font=sFont)
        buttonIn.pack(pady=2, padx=2, side=RIGHT)
        
        mainDirectoryIn = ctk.CTkLabel(frame08, text="Input:", font=sFont)
        mainDirectoryIn.pack(pady=2, padx=6, side=LEFT)

        #self.mainDirectoryStatus = ctk.CTkLabel(frame09, text="Unset", font=sFont, text_color="red")
        #self.mainDirectoryStatus.pack(pady=2, padx=6, side=LEFT)

        self.mainDirectoryPathIn = ctk.CTkLabel(frame08, text="Unset", text_color="red", font=sFont)
        self.mainDirectoryPathIn.pack(pady=2, padx=6,side=LEFT)   


        #### OUTPUT DIRECTORY ####
        buttonOut = ctk.CTkButton(frame09, text="Set Output",command=self.set_output_dir, width=100, font=sFont)
        buttonOut.pack(pady=2, padx=2, side=RIGHT)

        mainDirectoryOut = ctk.CTkLabel(frame09, text="Output:",width=32, font=sFont)
        mainDirectoryOut.pack(pady=2, padx=6, side=LEFT)

        #self.mainDirectoryStatus = ctk.CTkLabel(frame08, text="Unset", font=sFont, text_color="red")
        #self.mainDirectoryStatus.pack(pady=2, padx=6, side=LEFT)

        self.mainDirectoryPathOut = ctk.CTkLabel(frame09,  text="Unset", text_color="red", font=sFont)
        self.mainDirectoryPathOut.pack(pady=2, padx=6,side=LEFT)

        GenerateButton = ctk.CTkButton(frameBottom, text="Export", width=appWidth, command=self.generate, height=40, font=bFont)
        GenerateButton.pack(pady=2, padx=2, side=LEFT)



        #### Multiply #### 
        labelMultiply = ctk.CTkLabel(frame01, text="MULTIPLY", font=mFont)
        labelMultiply.pack(pady=6, padx=16)
        self.inputMultiply = ctk.CTkEntry(frame01, width=128, font=sFont)
        self.inputMultiply.pack(pady=6, padx=16)
        self.inputMultiply.insert(0, "1,1,1,1")


        #### Power #### 
        labelPower = ctk.CTkLabel(frame02, text="POWER", font=mFont)
        labelPower.pack(pady=6, padx=16)
        self.inputPower = ctk.CTkEntry(frame02, width=128, font=sFont)
        self.inputPower.pack(pady=6, padx=16)
        self.inputPower.insert(0, "1,1,1,1")

        #### Add #### 
        labelAdd = ctk.CTkLabel(frame03, text="ADD", font=mFont)
        labelAdd.pack(pady=6, padx=16)
        self.inputAdd = ctk.CTkEntry(frame03, width=128, font=sFont)
        self.inputAdd.pack(pady=6, padx=16)
        self.inputAdd.insert(0, "0,0,0,0")



        #### Subtract #### 
        labelSubtract = ctk.CTkLabel(frame04, text="SUBTRACT", font=mFont)
        labelSubtract.pack(pady=6, padx=16)
        self.inputSubtract = ctk.CTkEntry(frame04, width=128, font=sFont)
        self.inputSubtract.pack(pady=6, padx=16)
        self.inputSubtract.insert(0, "0,0,0,0")



        #### Max #### 
        labelMax = ctk.CTkLabel(frame05, text="MAX", font=mFont)
        labelMax.pack(pady=6, padx=16)
        self.inputMax = ctk.CTkEntry(frame05, width=128, font=sFont)
        self.inputMax.pack(pady=6, padx=16)
        self.inputMax.insert(0, "1,1,1,1")


        #### Min #### 
        labelMin = ctk.CTkLabel(frame06, text="MIN", font=mFont)
        labelMin.pack(pady=6, padx=16)
        self.inputMin = ctk.CTkEntry(frame06, width=128, font=sFont)
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

        frameMaster = ctk.CTkFrame(master,fg_color=fgColor)
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

        frame01 = ctk.CTkFrame(frame1, width=cellW2, height=cellH)
        frame01.pack(padx=2, pady=2, side=LEFT)
        frame01.propagate(False)

        frame02 = ctk.CTkFrame(frame2, width=cellW2, height=cellH)
        frame02.pack(padx=2, pady=2, side=LEFT)
        frame02.propagate(False)

        frame03 = ctk.CTkFrame(frame3, width=cellW2, height=cellH)
        frame03.pack(padx=2, pady=2, side=LEFT)
        frame03.propagate(False)

        frame04 = ctk.CTkFrame(frame4, width=cellW2, height=cellH)
        frame04.pack(padx=2, pady=2, side=LEFT)
        frame04.propagate(False)

        
        frame09 = ctk.CTkFrame(frameTop, width=400, height=30)
        frame09.pack(padx=2, pady=1)
        frame09.propagate(False)



        #### OUTPUT DIRECTORY ####
        buttonOut = ctk.CTkButton(frame09, text="Set Output",command=self.set_output_dir, width=100, font=sFont)
        buttonOut.pack(pady=2, padx=2, side=RIGHT)

        mainDirectoryOut = ctk.CTkLabel(frame09, text="Output:",width=32, font=sFont)
        mainDirectoryOut.pack(pady=2, padx=6, side=LEFT)

        self.mainDirectoryPathOut = ctk.CTkLabel(frame09,  text="Unset", text_color="red", font=sFont)
        self.mainDirectoryPathOut.pack(pady=2, padx=6,side=LEFT)

        GenerateButton = ctk.CTkButton(frameBottom, text="Combine", width=appWidth, command=self.generate, height=40, font=bFont)
        GenerateButton.pack(pady=2, padx=2, side=LEFT)



        #### Red #### 
        frame011 = ctk.CTkFrame(frame01, width=400, height=40)
        frame011.pack(padx=2, pady=1,fill=X,expand=TRUE)

        frame012 = ctk.CTkFrame(frame01, width=400, height=40)
        frame012.pack(padx=2, pady=1,fill=X,expand=TRUE)

        labelRed = ctk.CTkLabel(frame011, text="Red Channel", font=mFont)
        labelRed.pack(pady=6, padx=12, side=LEFT)

            #### INPUT FILE ####
        buttonInRed = ctk.CTkButton(frame011, text="Set Red",command=self.set_red_channel, width=100, font=sFont)
        buttonInRed.pack(pady=2, padx=2, side=RIGHT)

            #### EXTRACT ####
        self.var21 = ctk.IntVar()
        self.inputExtractRed = ctk.CTkOptionMenu(frame011, variable=self.var21, values=extract, width=85, font=sFont)
        self.inputExtractRed.set(extract[0])
        self.inputExtractRed.pack(pady=2, padx=1,side=RIGHT)

        mainDirectoryInRed = ctk.CTkLabel(frame012, text="Input:", font=sFont)
        mainDirectoryInRed.pack(pady=2, padx=6, side=LEFT)

        self.mainDirectoryPathInRed = ctk.CTkLabel(frame012, text="Unset", text_color="red", font=sFont)
        self.mainDirectoryPathInRed.pack(pady=2, padx=6,side=LEFT)   

        #### Green #### 
        frame021 = ctk.CTkFrame(frame02, width=400, height=40)
        frame021.pack(padx=2, pady=1,fill=X,expand=TRUE)

        frame022 = ctk.CTkFrame(frame02, width=400, height=40)
        frame022.pack(padx=2, pady=1,fill=X,expand=TRUE)

        labelGreen = ctk.CTkLabel(frame021, text="Green Channel", font=mFont)
        labelGreen.pack(pady=6, padx=12, side=LEFT)

            #### INPUT FILE ####
        buttonInGreen = ctk.CTkButton(frame021, text="Set Green",command=self.set_green_channel, width=100, font=sFont)
        buttonInGreen.pack(pady=2, padx=2, side=RIGHT)

            #### EXTRACT ####
        self.var22 = ctk.IntVar()
        self.inputExtractGreen = ctk.CTkOptionMenu(frame021, variable=self.var22, values=extract, width=85, font=sFont)
        self.inputExtractGreen.set(extract[0])
        self.inputExtractGreen.pack(pady=2, padx=1,side=RIGHT)
        
        mainDirectoryInGreen = ctk.CTkLabel(frame022, text="Input:", font=sFont)
        mainDirectoryInGreen.pack(pady=2, padx=6, side=LEFT)

        self.mainDirectoryPathInGreen = ctk.CTkLabel(frame022, text="Unset", text_color="red", font=sFont)
        self.mainDirectoryPathInGreen.pack(pady=2, padx=6,side=LEFT)   
        

        #### Blue #### 
        frame031 = ctk.CTkFrame(frame03, width=400, height=40)
        frame031.pack(padx=2, pady=1,fill=X,expand=TRUE)

        frame032 = ctk.CTkFrame(frame03, width=400, height=40)
        frame032.pack(padx=2, pady=1,fill=X,expand=TRUE)

        labelBlue = ctk.CTkLabel(frame031, text="Blue Channel", font=mFont)
        labelBlue.pack(pady=6, padx=12, side=LEFT)



            #### INPUT FILE ####
        buttonInBlue = ctk.CTkButton(frame031, text="Set Blue",command=self.set_blue_channel, width=100, font=sFont)
        buttonInBlue.pack(pady=2, padx=2, side=RIGHT)

            #### EXTRACT ####
        self.var23 = ctk.IntVar()
        self.inputExtractBlue= ctk.CTkOptionMenu(frame031, variable=self.var23, values=extract, width=85, font=sFont)
        self.inputExtractBlue.set(extract[0])
        self.inputExtractBlue.pack(pady=2, padx=1,side=RIGHT)
        
        mainDirectoryInBlue = ctk.CTkLabel(frame032, text="Input:", font=sFont)
        mainDirectoryInBlue.pack(pady=2, padx=6, side=LEFT)
        
        self.mainDirectoryPathInBlue = ctk.CTkLabel(frame032, text="Unset", text_color="red", font=sFont)
        self.mainDirectoryPathInBlue.pack(pady=2, padx=6,side=LEFT)   

        #### Alpha #### 
        frame041 = ctk.CTkFrame(frame04, width=400, height=40)
        frame041.pack(padx=2, pady=1,fill=X,expand=TRUE)

        frame042 = ctk.CTkFrame(frame04, width=400, height=40)
        frame042.pack(padx=2, pady=1,fill=X,expand=TRUE)

        labelAlpha = ctk.CTkLabel(frame041, text="Alpha Channel", font=mFont)
        labelAlpha.pack(pady=6, padx=16, side=LEFT)

            #### INPUT FILE ####
        buttonInAlpha = ctk.CTkButton(frame041, text="Set Alpha",command=self.set_alpha_channel, width=100, font=sFont)
        buttonInAlpha.pack(pady=2, padx=2, side=RIGHT)   

            #### EXTRACT ####
        self.var24 = ctk.IntVar()
        self.inputExtractAlpha= ctk.CTkOptionMenu(frame041, variable=self.var24, values=extract, width=85, font=sFont)
        self.inputExtractAlpha.set(extract[0])
        self.inputExtractAlpha.pack(pady=2, padx=1,side=RIGHT)

        
        mainDirectoryInAlpha = ctk.CTkLabel(frame042, text="Input:", font=sFont)
        mainDirectoryInAlpha.pack(pady=2, padx=6, side=LEFT)

        self.mainDirectoryPathInAlpha = ctk.CTkLabel(frame042, text="Unset", text_color="red", font=sFont)
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
            self.mainDirectoryPathOut.configure(text=self.OutputFilePath1,text_color="white",font=sFont1)

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

        frameMaster = ctk.CTkFrame(master,fg_color=fgColor)
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

        frame01 = ctk.CTkFrame(frame1, width=cellW2, height=cellH)
        frame01.pack(padx=2, pady=2, side=LEFT)
        frame01.propagate(False)

        frame02 = ctk.CTkFrame(frame2, width=cellW2, height=cellH)
        frame02.pack(padx=2, pady=2, side=LEFT)
        frame02.propagate(False)

        frame03 = ctk.CTkFrame(frame3, width=cellW2, height=cellH)
        frame03.pack(padx=2, pady=2, side=LEFT)
        frame03.propagate(False)

        frame04 = ctk.CTkFrame(frame4, width=cellW2, height=cellH)
        frame04.pack(padx=2, pady=2, side=LEFT)
        frame04.propagate(False)

        
        frame09 = ctk.CTkFrame(frameTop, width=400, height=30)
        frame09.pack(padx=2, pady=1)
        frame09.propagate(False)



        #### Input DIRECTORY ####
        buttonIn = ctk.CTkButton(frame09, text="Set Input",command=self.set_input_dir, width=100, font=sFont)
        buttonIn.pack(pady=2, padx=2, side=RIGHT)

        mainDirectoryIn = ctk.CTkLabel(frame09, text="Input:",width=32, font=sFont)
        mainDirectoryIn.pack(pady=2, padx=6, side=LEFT)

        self.mainDirectoryPathIn = ctk.CTkLabel(frame09,  text="Unset", text_color="red", font=sFont)
        self.mainDirectoryPathIn.pack(pady=2, padx=6,side=LEFT)

        GenerateButton = ctk.CTkButton(frameBottom, text="Separate", width=appWidth, command=self.generate, height=40, font=bFont)
        GenerateButton.pack(pady=2, padx=2, side=LEFT)



        #### Red #### 
        frame011 = ctk.CTkFrame(frame01, width=400, height=40)
        frame011.pack(padx=2, pady=1,fill=X,expand=TRUE)

        frame012 = ctk.CTkFrame(frame01, width=400, height=40)
        frame012.pack(padx=2, pady=1,fill=X,expand=TRUE)

        labelRed = ctk.CTkLabel(frame011, text="Red Channel", font=mFont)
        labelRed.pack(pady=6, padx=12, side=LEFT)

            #### OUTPUT FILE ####
        buttonOutRed = ctk.CTkButton(frame011, text="Set Red",command=self.set_red_channel, width=100, font=sFont)
        buttonOutRed.pack(pady=2, padx=2, side=RIGHT)

        mainDirectoryOutRed = ctk.CTkLabel(frame012, text="Output:", font=sFont)
        mainDirectoryOutRed.pack(pady=2, padx=6, side=LEFT)

        self.mainDirectoryPathOutRed = ctk.CTkLabel(frame012, text="Unset", text_color="red", font=sFont)
        self.mainDirectoryPathOutRed.pack(pady=2, padx=6,side=LEFT)   

        #### Green #### 
        frame021 = ctk.CTkFrame(frame02, width=400, height=40)
        frame021.pack(padx=2, pady=1,fill=X,expand=TRUE)

        frame022 = ctk.CTkFrame(frame02, width=400, height=40)
        frame022.pack(padx=2, pady=1,fill=X,expand=TRUE)

        labelGreen = ctk.CTkLabel(frame021, text="Green Channel", font=mFont)
        labelGreen.pack(pady=6, padx=12, side=LEFT)

            #### OUTPUT FILE ####
        buttonOutGreen = ctk.CTkButton(frame021, text="Set Green",command=self.set_green_channel, width=100, font=sFont)
        buttonOutGreen.pack(pady=2, padx=2, side=RIGHT)

        
        mainDirectoryOutGreen = ctk.CTkLabel(frame022, text="Output:", font=sFont)
        mainDirectoryOutGreen.pack(pady=2, padx=6, side=LEFT)

        self.mainDirectoryPathOutGreen = ctk.CTkLabel(frame022, text="Unset", text_color="red", font=sFont)
        self.mainDirectoryPathOutGreen.pack(pady=2, padx=6,side=LEFT)   
        

        #### Blue #### 
        frame031 = ctk.CTkFrame(frame03, width=400, height=40)
        frame031.pack(padx=2, pady=1,fill=X,expand=TRUE)

        frame032 = ctk.CTkFrame(frame03, width=400, height=40)
        frame032.pack(padx=2, pady=1,fill=X,expand=TRUE)

        labelBlue = ctk.CTkLabel(frame031, text="Blue Channel", font=mFont)
        labelBlue.pack(pady=6, padx=12, side=LEFT)


            #### OUTPUT FILE ####
        buttonOutBlue = ctk.CTkButton(frame031, text="Set Blue",command=self.set_blue_channel, width=100, font=sFont)
        buttonOutBlue.pack(pady=2, padx=2, side=RIGHT)

        
        mainDirectoryOutBlue = ctk.CTkLabel(frame032, text="Output:", font=sFont)
        mainDirectoryOutBlue.pack(pady=2, padx=6, side=LEFT)
        
        self.mainDirectoryPathOutBlue = ctk.CTkLabel(frame032, text="Unset", text_color="red", font=sFont)
        self.mainDirectoryPathOutBlue.pack(pady=2, padx=6,side=LEFT)   

        #### Alpha #### 
        frame041 = ctk.CTkFrame(frame04, width=400, height=40)
        frame041.pack(padx=2, pady=1,fill=X,expand=TRUE)

        frame042 = ctk.CTkFrame(frame04, width=400, height=40)
        frame042.pack(padx=2, pady=1,fill=X,expand=TRUE)

        labelAlpha = ctk.CTkLabel(frame041, text="Alpha Channel", font=mFont)
        labelAlpha.pack(pady=6, padx=16, side=LEFT)

            #### OUTPUT FILE ####
        buttonOutAlpha = ctk.CTkButton(frame041, text="Set Alpha",command=self.set_alpha_channel, width=100, font=sFont)
        buttonOutAlpha.pack(pady=2, padx=2, side=RIGHT)   
        
        mainDirectoryOutAlpha = ctk.CTkLabel(frame042, text="Output:", font=sFont)
        mainDirectoryOutAlpha.pack(pady=2, padx=6, side=LEFT)

        self.mainDirectoryPathOutAlpha = ctk.CTkLabel(frame042, text="Unset", text_color="red", font=sFont)
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
            self.mainDirectoryPathIn.configure(text=self.InputFilePath1,text_color="white",font=sFont1)

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

        frameMaster = ctk.CTkFrame(master,fg_color=fgColor)
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


        frame01 = ctk.CTkFrame(frame1, width=cellW2, height=cellH)
        frame01.pack(padx=2, pady=2, side=LEFT)
        frame01.propagate(False)

        frame02 = ctk.CTkFrame(frame2, width=cellW2, height=cellH)
        frame02.pack(padx=2, pady=2, side=LEFT)
        frame02.propagate(False)

        frame03 = ctk.CTkFrame(frame3, width=cellW2, height=cellH/2)
        frame03.pack(padx=2, pady=2, side=LEFT)
        frame03.propagate(False)


        
        frame09 = ctk.CTkFrame(frameTop, width=400, height=30)
        frame09.pack(padx=2, pady=1)
        frame09.propagate(False)



        #### OUTPUT DIRECTORY ####
        buttonOut = ctk.CTkButton(frame09, text="Set Output",command=self.set_output_dir, width=100, font=sFont)
        buttonOut.pack(pady=2, padx=2, side=RIGHT)

        mainDirectoryOut = ctk.CTkLabel(frame09, text="Output:",width=32, font=sFont)
        mainDirectoryOut.pack(pady=2, padx=6, side=LEFT)

        self.mainDirectoryPathOut = ctk.CTkLabel(frame09,  text="Unset", text_color="red", font=sFont)
        self.mainDirectoryPathOut.pack(pady=2, padx=6,side=LEFT)

        GenerateButton = ctk.CTkButton(frameBottom, text="Mask", width=appWidth, command=self.generate, height=40, font=bFont)
        GenerateButton.pack(pady=2, padx=2, side=LEFT)



        #### A #### 
        frame011 = ctk.CTkFrame(frame01, width=400, height=40)
        frame011.pack(padx=2, pady=1,fill=X,expand=TRUE)

        frame012 = ctk.CTkFrame(frame01, width=400, height=40)
        frame012.pack(padx=2, pady=1,fill=X,expand=TRUE)

        labelA = ctk.CTkLabel(frame011, text="Image A", font=mFont)
        labelA.pack(pady=6, padx=12, side=LEFT)

            #### INPUT FILE ####
        buttonInA = ctk.CTkButton(frame011, text="Set A",command=self.set_a_img, width=100, font=sFont)
        buttonInA.pack(pady=2, padx=2, side=RIGHT)

            #### EXTRACT ####
        self.var21 = ctk.IntVar()
        self.inputExtractA = ctk.CTkOptionMenu(frame011, variable=self.var21, values=extract, width=85, font=sFont)
        self.inputExtractA.set(extract[0])
        self.inputExtractA.pack(pady=2, padx=1,side=RIGHT)

        mainDirectoryInA = ctk.CTkLabel(frame012, text="Input:", font=sFont)
        mainDirectoryInA.pack(pady=2, padx=6, side=LEFT)

        self.mainDirectoryPathInA = ctk.CTkLabel(frame012, text="Unset", text_color="red", font=sFont)
        self.mainDirectoryPathInA.pack(pady=2, padx=6,side=LEFT)   

        #### B #### 
        frame021 = ctk.CTkFrame(frame02, width=400, height=40)
        frame021.pack(padx=2, pady=1,fill=X,expand=TRUE)

        frame022 = ctk.CTkFrame(frame02, width=400, height=40)
        frame022.pack(padx=2, pady=1,fill=X,expand=TRUE)

        labelB = ctk.CTkLabel(frame021, text="Image B", font=mFont)
        labelB.pack(pady=6, padx=12, side=LEFT)

            #### INPUT FILE ####
        buttonInB = ctk.CTkButton(frame021, text="Set B",command=self.set_b_img, width=100, font=sFont)
        buttonInB.pack(pady=2, padx=2, side=RIGHT)

            #### EXTRACT ####
        self.var22 = ctk.IntVar()
        self.inputExtractB = ctk.CTkOptionMenu(frame021, variable=self.var22, values=extract, width=85, font=sFont)
        self.inputExtractB.set(extract[0])
        self.inputExtractB.pack(pady=2, padx=1,side=RIGHT)
        
        mainDirectoryInB = ctk.CTkLabel(frame022, text="Input:", font=sFont)
        mainDirectoryInB.pack(pady=2, padx=6, side=LEFT)

        self.mainDirectoryPathInB = ctk.CTkLabel(frame022, text="Unset", text_color="red", font=sFont)
        self.mainDirectoryPathInB.pack(pady=2, padx=6,side=LEFT)   
        

        #### Mask #### 
        frame031 = ctk.CTkFrame(frame03, width=400, height=40)
        frame031.pack(padx=2, pady=1,fill=X,expand=TRUE)


        extractMethod = ["A * B","A + B","A - B","B - A"]
            #### EXTRACT ####
        self.var23 = ctk.IntVar()
        self.inputExtractMethod = ctk.CTkSegmentedButton(frame031, variable=self.var23, values=extractMethod, width=100, font=bFont)
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
            self.mainDirectoryPathOut.configure(text=self.OutputFilePath1,text_color="white",font=sFont1)

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
        
# Initialize classes within the appropriate tabs
solid_tab = Solid(tab1)
gradient_tab = Gradient(tab2)
math_tab = Math(tab3)
combine_tab = Combine(tab4)
separate_tab = Separate(tab5)
mask_tab = Mask(tab6)

root.mainloop()