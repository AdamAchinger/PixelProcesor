
def Directory():
    global Path
    Path = filedialog.askdirectory(title="Main Directory")
    if (Path!=""):
        mainDirectoryStatus.config(text="Ready",fg="green")
        mainDirectoryPath.config(text=Path)


def gSolidColor():

    Color = inputHex.get()
    Size = inputSize.get()
    OutputDir = Path
    Filename = inputFilename.get()
    Filetype = inputFiletype.get()
    
    SizeNew = Size.lower()
    Width=int(SizeNew.split("x")[0])
    Height=int(SizeNew.split("x")[1])
    
    FiletypeNew = Filetype.lower().replace(".","")

    name = str(f"{Filename}_{Color}_{Width}x{Height}.{FiletypeNew}")
    imgOutput = os.path.join(OutputDir,name)

    img = Image.new(mode="RGB",size=(Width,Height),color=Color)
    img.save(imgOutput)
    
#    messagebox.showinfo(title="Output File",message=imgOutput)

    print(str(f'{Color} {Size} {OutputDir} {Filename} {Filetype} {Width} {Height}'))