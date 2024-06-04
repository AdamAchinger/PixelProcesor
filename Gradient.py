import os
from tkinter import * 
from tkinter import messagebox 

### Version
toolVersion = 1.1
###

def Gradient(inputOutput1):
    Grad = Toplevel()

    root = Grad

    bgColor = "#353535"
    fgColor = "#C0C0C0"
    hlColor = "#777777"
    fontSizeSmall = 13


    root.configure(bg=bgColor)
    root.title("Create Gradient"+" v"+str(toolVersion))
    root.iconbitmap('S:\GitHub\PixelProcesor\AA_icon.ico')
    root.resizable(False,False)

    #####
    # application dimensions
    appWidth = 420
    appHeight = 470
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

        Flip = var.get()
        Color1 = inputColor1.get()
        Color2 = inputColor2.get()
        Size = inputSize.get()
        Orient = inputOrient.get()
        OutputDir = inputOutput.get()
        Filename = inputFilename.get()
        Filetype = inputFiletype.get()
        SizeNew = Size.lower()
        Width = int(SizeNew.split("x")[0])
        Height = int(SizeNew.split("x")[1])
        
        FiletypeNew = Filetype.lower().replace(".","")

        nOrient1 = Orient.upper()
        nOrient2 = str(nOrient1[0])

        img = Image.new(mode="RGB",size=(Width,Height))

        Color1.replace(" ","")
        Color2.replace(" ","")
        
        print(Color1,Color2)
        R1 = float(Color1.split(",")[0])
        R2 = float(Color2.split(",")[0])
        G1 = float(Color1.split(",")[1])
        G2 = float(Color2.split(",")[1])
        B1 = float(Color1.split(",")[2])
        B2 = float(Color2.split(",")[2])

        for w in range(Width):
            for h in range(Height):
                if (nOrient2=="V"):
                    v = int((h/Width)*255) 
                else:
                    v = int((w/Height)*255)
                if (Flip==1):
                    v = abs(v-255)

                R = (int(v*R2)+int(abs(v+255)*R1))
                G = (int(v*G2)+int(abs(v+255)*G1))
                B = (int(v*B2)+int(abs(v+255)*B1))

                img.putpixel((w,h),(R,G,B))
        print(Flip,var)
            


        name = str(f"{Filename}_{nOrient2}_{Width}x{Height}.{FiletypeNew}")
        imgOutput = os.path.join(OutputDir,name)

        img.save(imgOutput)

    #### Create Gradient #### 
    frame1 = Frame(root,width=100,bg=bgColor)
    frame1.grid(row=0,column=0,pady=6,padx=16)

    label_1 = Label(frame1,text="Create Gradient",font=("roboto",32),bg=bgColor,fg=fgColor)
    label_1.grid(row=0,column=0,pady=6,padx=16)

    #### Orientation #### 
    frame2 = Frame(root,width=100,bg=bgColor,highlightbackground=hlColor,highlightthickness=1)
    frame2.grid(row=1,column=0,pady=6,padx=12,sticky=W)

    labelOrient = Label(frame2,text="ORIENT (V/H)",font=("roboto",fontSizeSmall),bg=bgColor,fg=fgColor).grid(row=1,column=0,pady=2,padx=16)
    inputOrient = Entry(frame2,width=17,font=("roboto",fontSizeSmall),bg=bgColor,fg=fgColor)
    inputOrient.grid(row=2,column=0,sticky=E,pady=6,padx=16)
    inputOrient.insert(0,"VERTICAL")

    #### Flip #### 
    var = IntVar()
    inputFlip = Checkbutton(frame2,text="FLIP ?",variable=var,font=("roboto",fontSizeSmall-4),bg=bgColor,fg=fgColor)
    inputFlip.grid(row=2,column=0,sticky=E,pady=1,padx=6)
    inputFlip.deselect()  
    
    #### SIZE #### 
    frame3 = Frame(root,width=100,bg=bgColor,highlightbackground=hlColor,highlightthickness=1)
    frame3.grid(row=1,column=0,pady=6,padx=12,sticky=E)

    labelSize = Label(frame3,text="SIZE",font=("roboto",fontSizeSmall),bg=bgColor,fg=fgColor).grid(row=1,column=0,pady=6,padx=16)
    inputSize = Entry(frame3,width=17,font=("roboto",fontSizeSmall),bg=bgColor,fg=fgColor)
    inputSize.grid(row=2,column=0,sticky=E,pady=2,padx=16)
    inputSize.insert(0,"512x512")

    #### FILENAME #### 
    frame7 = Frame(root,width=100,bg=bgColor,highlightbackground=hlColor,highlightthickness=1)
    frame7.grid(row=2,column=0,pady=6,padx=12,sticky=W)

    labelFilename = Label(frame7,text="FILENAME",font=("roboto",fontSizeSmall),bg=bgColor,fg=fgColor).grid(row=1,column=0,pady=6,padx=16)
    inputFilename = Entry(frame7,width=17,font=("roboto",fontSizeSmall),bg=bgColor,fg=fgColor)
    inputFilename.grid(row=2,column=0,sticky=E,pady=2,padx=16)
    inputFilename.insert(0,"T_Gradient")

    #### FILETYPE #### 
    frame4 = Frame(root,width=100,bg=bgColor,highlightbackground=hlColor,highlightthickness=1)
    frame4.grid(row=2,column=0,pady=6,padx=12,sticky=E)

    labelFiletype = Label(frame4,text="FILETYPE",font=("roboto",fontSizeSmall),bg=bgColor,fg=fgColor).grid(row=1,column=0,pady=6,padx=16)
    inputFiletype = Entry(frame4,width=17,font=("roboto",fontSizeSmall),bg=bgColor,fg=fgColor)
    inputFiletype.grid(row=2,column=0,sticky=W,pady=2,padx=16)
    inputFiletype.insert(0,".PNG")


    #### Hex1 #### 
    frame21 = Frame(root,width=100,bg=bgColor,highlightbackground=hlColor,highlightthickness=1)
    frame21.grid(row=3,column=0,pady=6,padx=12,sticky=W)

    labelColor1 = Label(frame21,text="COLOR 1 (RGB)",font=("roboto",fontSizeSmall),bg=bgColor,fg=fgColor).grid(row=1,column=0,pady=6,padx=16)
    inputColor1 = Entry(frame21,width=17,text="Color1",font=("roboto",fontSizeSmall),bg=bgColor,fg=fgColor)
    inputColor1.grid(row=2,column=0,sticky=W,pady=2,padx=16)
    inputColor1.insert(0,"0,0,0")

    #### Hex2 #### 
    frame22 = Frame(root,width=100,bg=bgColor,highlightbackground=hlColor,highlightthickness=1)
    frame22.grid(row=3,column=0,pady=6,padx=12,sticky=E)

    labelColor2 = Label(frame22,text="COLOR 2 (RGB)",font=("roboto",fontSizeSmall),bg=bgColor,fg=fgColor).grid(row=1,column=0,pady=6,padx=16)
    inputColor2 = Entry(frame22,width=17,text="Color2",font=("roboto",fontSizeSmall),bg=bgColor,fg=fgColor)
    inputColor2.grid(row=2,column=0,sticky=E,pady=2,padx=16)
    inputColor2.insert(0,"1,1,1")

    #### OUTPUT DIRECTORY #### 
    frame5 = Frame(root,width=100,bg=bgColor,highlightbackground=hlColor,highlightthickness=1)
    frame5.grid(row=4,column=0,pady=6,padx=12,sticky=S)

    labelOutput = Label(frame5,text="OUTPUT DIRECTORY",font=("roboto",fontSizeSmall),bg=bgColor,fg=fgColor).grid(row=1,column=0,pady=6,padx=16)
    inputOutput = Entry(frame5,width=39,font=("roboto",fontSizeSmall),bg=bgColor,fg=fgColor)
    inputOutput.grid(row=2,column=0,sticky=W,pady=2,padx=16)
    inputOutput.insert(0,inputOutput1)


    #### Generate #### 
    frame6 = Frame(root,width=100,bg=bgColor)
    frame6.grid(row=5,column=0,pady=10,padx=60,sticky=S)

    hexButton = Button(frame6,text="Create Gradient",font=("roboto",18),bg=bgColor,fg=fgColor,pady=2,padx=25,command=Generate).grid(row=0,column=0,sticky=S,pady=2,padx=2)




    root.mainloop()
