import os
from tkinter import *
from tkinter import filedialog
from PIL import Image
import customtkinter as ctk

### Version
toolVersion = 6.1
###

root = Tk()

bgColor = "#353535"
fgColor = "#C0C0C0"
hlColor = "#777777"

sFont = ("roboto", 16)
mFont = ("roboto", 20)
bFont = ("roboto", 22)

cellH = 85
cellW = 180
exten = ["PNG", "JPEG", "PPM", "GIF", "TIFF","BMP"]

appWidth = 400
appHeight = 380

root.configure(bg=bgColor)
root.title("Pixel Procesor" + " v" + str(toolVersion))
root.iconbitmap('S:\GitHub\PixelProcesor\img\AA_icon.ico')
root.resizable(False, False)

# get windows screan width and height
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
# center position 
appXpos = int((screenWidth / 2) - (appWidth / 2))
appYpos = int((screenHeight / 2) - (appHeight / 2))
# create app window 
root.geometry(f'{appWidth}x{appHeight}+{appXpos}+{appYpos}')
#####

# Create the tab view (this is the equivalent of a tabbed frame)
tab_view = ctk.CTkTabview(root)
tab_view.pack(expand=True, fill="both")

my_font = ctk.CTkFont(size=14)  # Font object

# Add tabs to the tab view
tab1 = tab_view.add("Solid Color")
tab2 = tab_view.add("Gradient")
tab3 = tab_view.add("Math")
tab4 = tab_view.add("Combine")
tab5 = tab_view.add("Color Pick")

for button in tab_view._segmented_button._buttons_dict.values():
    button.configure(height=32, font=my_font)  # Change font using font object


class SolidColor:
    def __init__(self, master):
        self.Path = ""

        frameTop = ctk.CTkFrame(master)
        frameTop.pack()

        frameBottom = ctk.CTkFrame(master)
        frameBottom.pack(side=BOTTOM)

        scrolFrame = ctk.CTkScrollableFrame(frameTop,width=400,height=225)
        scrolFrame.pack()

        #### Input ####
        frame1T = ctk.CTkFrame(scrolFrame)
        frame1T.pack()

        frame1M = ctk.CTkFrame(scrolFrame)
        frame1M.pack()

        frame1B = ctk.CTkFrame(frameBottom)
        frame1B.pack(fill=Y,expand=True)

        frame01 = ctk.CTkFrame(frame1T, width=cellW, height=cellH)
        frame01.pack(padx=2, pady=2, side=LEFT)
        frame01.propagate(False)

        frame02 = ctk.CTkFrame(frame1T, width=cellW, height=cellH)
        frame02.pack(padx=2, pady=2, side=LEFT)
        frame02.propagate(False)

        frame03 = ctk.CTkFrame(frame1M, width=cellW, height=cellH)
        frame03.pack(padx=2, pady=2, side=LEFT)
        frame03.propagate(False)

        frame04 = ctk.CTkFrame(frame1M, width=cellW, height=cellH)
        frame04.pack(padx=2, pady=2, side=LEFT)
        frame04.propagate(False)

        frame05 = ctk.CTkFrame(frame1B, width=400, height=50)
        frame05.pack(padx=2, pady=2,side=BOTTOM)
        frame05.propagate(False)

        frame06 = ctk.CTkFrame(frame1B, width=400, height=30)
        frame06.pack(padx=2, pady=2,side=BOTTOM)
        frame06.propagate(False)

        #### HEX ####
        self.inputHex = StringVar()
        labelHex = ctk.CTkLabel(frame01, text="COLOR (HEX)", font=mFont)
        labelHex.pack(pady=6, padx=16)

        self.inputHexEntry = ctk.CTkEntry(frame01, width=128, textvariable=self.inputHex, font=sFont)
        self.inputHexEntry.pack(pady=6, padx=16)
        self.inputHexEntry.insert(0, "#F67070")

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

        #### OUTPUT DIRECTORY ####
        mainDirectory = ctk.CTkLabel(frame06, text="Directory:", font=sFont)
        mainDirectory.pack(pady=2, padx=6, side=LEFT)

        self.mainDirectoryStatus = ctk.CTkLabel(frame06, text="Unset", text_color="red", font=sFont)
        self.mainDirectoryStatus.pack(pady=2, padx=6, side=LEFT)

        self.mainDirectoryPath = ctk.CTkLabel(frame06, text="------------", font=sFont)
        self.mainDirectoryPath.pack(pady=2, padx=6, side=LEFT)

        button = ctk.CTkButton(frame05, text="Output Directory", width=190, height=40, command=self.set_directory, font=bFont)
        button.pack(pady=2, padx=2,side=LEFT)

        generateButton = ctk.CTkButton(frame05, text="Export Solid", width=190, height=40, command=self.generate, font=bFont)
        generateButton.pack(pady=2, padx=2,side=LEFT)

    def set_directory(self):
        self.Path = filedialog.askdirectory(title="Directory")
        if self.Path:
            self.mainDirectoryStatus.configure(text="Ready", text_color="green")
            self.mainDirectoryPath.configure(text=self.Path)

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
        width, height = map(int, Size.split('x'))
        image = Image.new("RGB", (width, height), Color)
        full_path = os.path.join(OutputDir, Filename + "."+Filetype)
        image.save(full_path)
        print(f"Image saved to {full_path}")


class Gradient:
    def __init__(self, master):
        self.Path = ""

        frameTop = ctk.CTkFrame(master)
        frameTop.pack()

        frameBottom = ctk.CTkFrame(master)
        frameBottom.pack(side=BOTTOM)

        scrolFrame = ctk.CTkScrollableFrame(frameTop,width=400,height=225)
        scrolFrame.pack()
     
        #### Input ####
        frame1T = ctk.CTkFrame(scrolFrame)
        frame1T.pack()

        frame1M = ctk.CTkFrame(scrolFrame)
        frame1M.pack()

        frame1B = ctk.CTkFrame(scrolFrame)
        frame1B.pack()

        frame1B2 = ctk.CTkFrame(frameBottom)
        frame1B2.pack(fill=Y,expand=True)

        frame01 = ctk.CTkFrame(frame1T, width=cellW, height=cellH)
        frame01.pack(padx=2, pady=2, side=LEFT)
        frame01.propagate(False)

        frame02 = ctk.CTkFrame(frame1T, width=cellW, height=cellH)
        frame02.pack(padx=2, pady=2, side=LEFT)
        frame02.propagate(False)

        frame03 = ctk.CTkFrame(frame1M, width=cellW, height=cellH)
        frame03.pack(padx=2, pady=2, side=LEFT)
        frame03.propagate(False)

        frame04 = ctk.CTkFrame(frame1M, width=cellW, height=cellH)
        frame04.pack(padx=2, pady=2, side=LEFT)
        frame04.propagate(False)

        frame05 = ctk.CTkFrame(frame1B, width=cellW, height=cellH)
        frame05.pack(padx=2, pady=2, side=LEFT)
        frame05.propagate(False)

        frame06 = ctk.CTkFrame(frame1B, width=cellW, height=cellH)
        frame06.pack(padx=2, pady=2, side=LEFT)
        frame06.propagate(False)

        frame07 = ctk.CTkFrame(frame1B2, width=400, height=50)
        frame07.pack(padx=2, pady=2,side=BOTTOM)
        frame07.propagate(False)

        frame08 = ctk.CTkFrame(frame1B2, width=400, height=30)
        frame08.pack(padx=2, pady=2,side=BOTTOM)
        frame08.propagate(False)

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
        self.inputFilename.pack(pady=2, padx=16)
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



        #### OUTPUT DIRECTORY ####

        mainDirectory = ctk.CTkLabel(frame08, text="Directory:", font=sFont)
        mainDirectory.pack(pady=2, padx=6, side=LEFT)

        self.mainDirectoryStatus = ctk.CTkLabel(frame08, text="Unset", font=sFont, text_color="red")
        self.mainDirectoryStatus.pack(pady=2, padx=6, side=LEFT)

        self.mainDirectoryPath = ctk.CTkLabel(frame08, text="------------", font=sFont)
        self.mainDirectoryPath.pack(pady=2, padx=6,side=LEFT)


        button = ctk.CTkButton(frame07, text="Output Directory", width=190, height=40, command=self.set_directory, font=bFont)
        button.pack(pady=2, padx=2, side=LEFT)

        GenerateButton = ctk.CTkButton(frame07, text="Export Gradient", width=190, height=40, command=self.generate, font=bFont)
        GenerateButton.pack(pady=2, padx=2, side=LEFT)

    def set_directory(self):
        self.Path = filedialog.askdirectory(title="Directory")
        if self.Path:
            self.mainDirectoryStatus.configure(text="Ready", text_color="green")
            self.mainDirectoryPath.configure(text=self.Path)
        

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
        

        
# Initialize classes within the appropriate tabs
solid_color_tab = SolidColor(tab1)
gradient_tab = Gradient(tab2)

root.mainloop()
