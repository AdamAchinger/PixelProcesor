import os
from tkinter import * 
from tkinter import messagebox 

### Version
toolVersion = 1.1
###

def Math(inputOutput1):
    Grad = Toplevel()

    root = Grad

    bgColor = "#353535"
    fgColor = "#C0C0C0"
    hlColor = "#777777"
    fontSizeSmall = 13


    root.configure(bg=bgColor)
    root.title("Math"+" v"+str(toolVersion))
    root.iconbitmap('S:\GitHub\PixelProcesor\img\AA_icon.ico')
    root.resizable(False,False)

    #####
    # application dimensions
    appWidth = 420
    appHeight = 490
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


            


    #### Math #### 
    frame1 = Frame(root,width=100,bg=bgColor)
    frame1.grid(row=0,column=0,pady=10,padx=60,sticky=S)

    label_1 = Label(frame1,text="Math",font=("roboto",32),bg=bgColor,fg=fgColor)
    label_1.grid(row=0,column=0,pady=10,padx=60,sticky=S)


    #### Input File #### 
    frame51 = Frame(root,width=100,bg=bgColor,highlightbackground=hlColor,highlightthickness=1)
    frame51.grid(row=1,column=0,pady=6,padx=12,sticky=S)

    labelInputFile = Label(frame51,text="INPUT FILE",font=("roboto",fontSizeSmall),bg=bgColor,fg=fgColor)
    labelInputFile.grid(row=1,column=0,sticky=S,pady=6,padx=16)

    inputInputFile = Entry(frame51,width=40,font=("roboto",fontSizeSmall),bg=bgColor,fg=fgColor)
    inputInputFile.grid(row=2,column=0,sticky=S,pady=2,padx=16)
    inputInputFile.insert(0,"Import File")



    #### Multiply #### 
    frame21 = Frame(root,width=25,bg=bgColor,highlightbackground=hlColor,highlightthickness=1)
    frame21.grid(row=3,column=0,pady=6,padx=12,sticky=W)

    labelMultiply = Label(frame21,text="MULTIPLY",font=("roboto",fontSizeSmall),bg=bgColor,fg=fgColor).grid(row=1,column=0,pady=6,padx=16)
    inputMultiply = Entry(frame21,width=10,font=("roboto",fontSizeSmall),bg=bgColor,fg=fgColor)
    inputMultiply.grid(row=2,column=0,pady=2,padx=16)
    inputMultiply.insert(0,"1")

    #### Power #### 
    frame22 = Frame(root,width=25,bg=bgColor,highlightbackground=hlColor,highlightthickness=1)
    frame22.grid(row=3,column=0,pady=6,padx=147,sticky=W)

    labelPower = Label(frame22,text="POWER",font=("roboto",fontSizeSmall),bg=bgColor,fg=fgColor).grid(row=1,column=0,pady=6,padx=16)
    inputPower = Entry(frame22,width=10,font=("roboto",fontSizeSmall),bg=bgColor,fg=fgColor)
    inputPower.grid(row=2,column=0,pady=2,padx=16)
    inputPower.insert(0,"1")

    #### Divide #### 
    frame23 = Frame(root,width=25,bg=bgColor,highlightbackground=hlColor,highlightthickness=1)
    frame23.grid(row=3,column=0,pady=6,padx=12,sticky=E)

    labelDivide = Label(frame23,text="DIVIDE",font=("roboto",fontSizeSmall),bg=bgColor,fg=fgColor).grid(row=1,column=0,pady=6,padx=16)
    inputDivide = Entry(frame23,width=10,font=("roboto",fontSizeSmall),bg=bgColor,fg=fgColor)
    inputDivide.grid(row=2,column=0,pady=2,padx=16)
    inputDivide.insert(0,"1")


    #### Add #### 
    frame24 = Frame(root,width=25,bg=bgColor,highlightbackground=hlColor,highlightthickness=1)
    frame24.grid(row=4,column=0,pady=6,padx=12,sticky=W)

    labelAdd = Label(frame24,text="ADD",font=("roboto",fontSizeSmall),bg=bgColor,fg=fgColor).grid(row=1,column=0,pady=6,padx=16)
    inputAdd = Entry(frame24,width=10,font=("roboto",fontSizeSmall),bg=bgColor,fg=fgColor)
    inputAdd.grid(row=2,column=0,pady=2,padx=16)
    inputAdd.insert(0,"0")

    #### Subtract #### 
    frame25 = Frame(root,width=25,bg=bgColor,highlightbackground=hlColor,highlightthickness=1)
    frame25.grid(row=4,column=0,pady=6,padx=147,sticky=W)

    labelSubtract = Label(frame25,text="SUBTRACT",font=("roboto",fontSizeSmall),bg=bgColor,fg=fgColor).grid(row=1,column=0,pady=6,padx=16)
    inputSubtract = Entry(frame25,width=10,font=("roboto",fontSizeSmall),bg=bgColor,fg=fgColor)
    inputSubtract.grid(row=2,column=0,pady=2,padx=16)
    inputSubtract.insert(0,"0")

    #### Clamp #### 
    frame26 = Frame(root,width=25,bg=bgColor,highlightbackground=hlColor,highlightthickness=1)
    frame26.grid(row=4,column=0,pady=6,padx=12,sticky=E)

    labelClamp = Label(frame26,text="(MIN/MAX)",font=("roboto",fontSizeSmall),bg=bgColor,fg=fgColor).grid(row=1,column=0,pady=6,padx=16)
    inputClamp = Entry(frame26,width=10,font=("roboto",fontSizeSmall),bg=bgColor,fg=fgColor)
    inputClamp.grid(row=2,column=0,pady=2,padx=16)
    inputClamp.insert(0,"1,1")


    #### OUTPUT DIRECTORY #### 
    frame52 = Frame(root,width=100,bg=bgColor,highlightbackground=hlColor,highlightthickness=1)
    frame52.grid(row=5,column=0,pady=6,padx=12,sticky=S)

    labelOutput = Label(frame52,text="OUTPUT DIRECTORY",font=("roboto",fontSizeSmall),bg=bgColor,fg=fgColor)
    labelOutput.grid(row=1,column=0,sticky=S,pady=6,padx=16)

    inputOutput = Entry(frame52,width=40,font=("roboto",fontSizeSmall),bg=bgColor,fg=fgColor)
    inputOutput.grid(row=2,column=0,sticky=S,pady=2,padx=16)
    inputOutput.insert(0,inputOutput1)

    #### Generate #### 
    frame6 = Frame(root,width=100,bg=bgColor)
    frame6.grid(row=7,column=0,pady=10,padx=60,sticky=S)

    saveButton = Button(frame6,text="Save",font=("roboto",18),bg=bgColor,fg=fgColor,pady=2,padx=25,command=Generate)
    saveButton.grid(row=0,column=0,sticky=S,pady=2,padx=2)



    root.mainloop()
