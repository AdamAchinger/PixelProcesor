import os
from tkinter import * 
from tkinter import messagebox 

### Version
toolVersion = 1.1
###

def SolidColor(inputOutput1):
    CSC = Toplevel()

    root = CSC

    bgColor = "#353535"
    fgColor = "#C0C0C0"
    hlColor = "#777777"
    fontSizeSmall = 13


    root.configure(bg=bgColor)
    root.title("Create Solid Color "+" v"+str(toolVersion))
    root.iconbitmap('S:\GitHub\PixelProcesor\img\AA_icon.ico')
    root.resizable(False,False)

    #####
    # application dimensions
    appWidth = 420
    appHeight = 390
    # get windows screan width and height
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()
    # center position 
    appXpos = int((screenWidth/2)-(appWidth/2))
    appYpos = int((screenHeight/2)-(appHeight/2))
    # create app window 
    root.geometry(f'{appWidth}x{appHeight}+{appXpos}+{appYpos}')
    #####



    def Generate():

        from PIL import Image

        Color = inputHex.get()
        Size = inputSize.get()
        OutputDir = inputOutput.get()
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

        ## log 
        print(str(f'{inputHex.get()} {inputSize.get()} {inputOutput.get()} {inputFilename.get()} {inputFiletype.get()}'))
        print(str(f'{Color} {Size} {OutputDir} {Filename} {Filetype} {Width} {Height}'))



    #### Create Solid Color #### 
    frame1 = Frame(root,width=100,bg=bgColor)
    frame1.grid(row=0,column=0,pady=6,padx=12)

    label_1 = Label(frame1,text="Create Solid Color",font=("roboto",32),bg=bgColor,fg=fgColor)
    label_1.grid(row=0,column=0,pady=2,padx=16)



    #### HEX #### 


    frame2 = Frame(root,width=100,bg=bgColor,highlightbackground=hlColor,highlightthickness=1)
    frame2.grid(row=1,column=0,pady=6,padx=12,sticky=W)
    inputHex = StringVar()

    labelHex = Label(frame2,text="COLOR (HEX)",font=("roboto",fontSizeSmall),bg=bgColor,fg=fgColor).grid(row=1,column=0,pady=6,padx=16)
    inputHex = StringVar()
    inputHex = Entry(frame2,width=17,textvariable=inputHex,font=("roboto",fontSizeSmall),bg=bgColor,fg=fgColor)
    inputHex.grid(row=2,column=0,sticky=W,pady=2,padx=16)
    inputHex.insert(0,"#F67070")



    #### SIZE #### 
    frame3 = Frame(root,width=100,bg=bgColor,highlightbackground=hlColor,highlightthickness=1)
    frame3.grid(row=1,column=0,pady=6,padx=12,sticky=E)

    labelSize = Label(frame3,text="SIZE",font=("roboto",fontSizeSmall),bg=bgColor,fg=fgColor).grid(row=1,column=0,pady=6,padx=16)
    inputSize = Entry(frame3,width=17,font=("roboto",fontSizeSmall),bg=bgColor,fg=fgColor)
    inputSize.grid(row=2,column=0,sticky=E,pady=2,padx=16)
    inputSize.insert(0,"512x512",)

    #### FILENAME #### 
    frame7 = Frame(root,width=100,bg=bgColor,highlightbackground=hlColor,highlightthickness=1)
    frame7.grid(row=2,column=0,pady=6,padx=12,sticky=W)

    labelFilename = Label(frame7,text="FILENAME",font=("roboto",fontSizeSmall),bg=bgColor,fg=fgColor).grid(row=1,column=0,pady=6,padx=16)
    inputFilename = Entry(frame7,width=17,font=("roboto",fontSizeSmall),bg=bgColor,fg=fgColor)
    inputFilename.grid(row=2,column=0,sticky=E,pady=2,padx=16)
    inputFilename.insert(0,"T_SolidColor")

    #### FILETYPE #### 
    frame4 = Frame(root,width=100,bg=bgColor,highlightbackground=hlColor,highlightthickness=1)
    frame4.grid(row=2,column=0,pady=6,padx=12,sticky=E)

    labelFiletype = Label(frame4,text="FILETYPE",font=("roboto",fontSizeSmall),bg=bgColor,fg=fgColor).grid(row=1,column=0,pady=6,padx=16)
    inputFiletype = Entry(frame4,width=17,font=("roboto",fontSizeSmall),bg=bgColor,fg=fgColor)
    inputFiletype.grid(row=2,column=0,sticky=W,pady=2,padx=16)
    inputFiletype.insert(0,".PNG")

    #### OUTPUT DIRECTORY #### 
    frame5 = Frame(root,width=100,bg=bgColor,highlightbackground=hlColor,highlightthickness=1)
    frame5.grid(row=3,column=0,pady=6,padx=12,sticky=W)

    labelOutput = Label(frame5,text="OUTPUT DIRECTORY",font=("roboto",fontSizeSmall),bg=bgColor,fg=fgColor).grid(row=1,column=0,pady=6,padx=16)
    inputOutput = Entry(frame5,width=40,font=("roboto",fontSizeSmall),bg=bgColor,fg=fgColor)
    inputOutput.grid(row=2,column=0,sticky=S,pady=2,padx=16)
    inputOutput.insert(0,inputOutput1)

    #### Generate #### 
    frame6 = Frame(root,width=100,bg=bgColor)
    frame6.grid(row=4,column=0,pady=10,padx=60,sticky=S)

    hexButton = Button(frame6,text="Create Solid Color",font=("roboto",18),bg=bgColor,fg=fgColor,pady=2,padx=25,command=Generate).grid(row=0,column=0,sticky=S,pady=2,padx=2)




    root.mainloop()
