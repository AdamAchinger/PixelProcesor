def SolidColor(tab1):

    root = tab1
    def Generate():

        from PIL import Image

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

    frame5 = Frame(root,width=400,bg=bgColor,highlightbackground=hlColor,highlightthickness=0)
    frame5.grid(row=4,column=0,pady=6,padx=6,sticky=W)

    mainDirectory = Label(frame5,text="Directory:",font=("roboto",12),bg=bgColor,fg=fgColor)
    mainDirectory.grid(row=2,column=0,pady=2,padx=6,sticky=W)

    mainDirectoryStatus = Label(frame5,text="Unset",font=("roboto",13),bg=bgColor,fg="red")
    mainDirectoryStatus.grid(row=2,column=0,pady=2,padx=80,sticky=W)

    mainDirectoryPath = Label(frame5,text="------------",font=("roboto",12),bg=bgColor,fg=fgColor)
    mainDirectoryPath.grid(row=3,column=0,pady=2,padx=6,sticky=W)


    def Directory():
        global Path
        Path = filedialog.askdirectory(title="Main Directory")
        if (Path!=""):
            mainDirectoryStatus.config(text="Ready",fg="green")
            mainDirectoryPath.config(text=Path)



    framePanel = Frame(root,width=400,bg=bgColor,highlightbackground=hlColor,highlightthickness=1)
    framePanel.grid(row=3,column=0,pady=6,padx=2,sticky=S)

    button = Button(framePanel,text="Set Output Directory",command=Directory,font=("roboto",fontSizeSmall),bg=bgColor,fg=fgColor)
    button.grid(row=0,column=0,sticky=W,pady=2,padx=2)

    #### Generate #### 
    GenerateButton = Button(framePanel,text="Export Solid Color",font=("roboto",fontSizeSmall),bg=bgColor,fg=fgColor,command=Generate)
    GenerateButton.grid(row=0,column=1,sticky=W,pady=2,padx=2)



    root.mainloop()
