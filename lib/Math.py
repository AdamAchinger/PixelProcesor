import os
from tkinter import * 
from tkinter import messagebox 

### Version
toolVersion = 2.3
###

def Math(inputOutput1):
    Math = Toplevel()

    root = Math

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
        from tkinter import messagebox 


        Multiply3 = inputMultiply.get()
        Power3 = inputPower.get()
        Add3 = inputAdd.get()
        Subtract3 = inputSubtract.get()
        Min3 = inputMin.get()
        Max3 = inputMax.get()
        InputFile = inputInputFile.get()    
        Output = inputOutput.get()    


        #### Warning Message ####
        empty = InputFile.replace(" ","")
        empty2 = Output.replace(" ","")
        
        if(InputFile==inputOutput1 or empty==""):
            messagebox.showwarning(title="Empty Directory",message="Input File Does Not Exist")

        if(Output==inputOutput1 or empty2==""):
            messagebox.showwarning(title="Empty Directory",message="Output File Does Not Exist")



        
        img = Image.open(InputFile)
        Width, Height = img.size

        for w in range(Width):
            for h in range(Height):

                ### Multiply ###
                if(Multiply3!="1,1,1"):
                    R1,G1,B1, = img.getpixel((w,h))
                    R = int(R1 * float(Multiply3.split(",")[0]))
                    G = int(G1 * float(Multiply3.split(",")[1]))
                    B = int(B1 * float(Multiply3.split(",")[2]))
                    img.putpixel((w,h),(R,G,B))
                ### Power ###
                if(Power3!="1,1,1"):
                    R1,G1,B1 = img.getpixel((w,h))
                    R = int(pow(R1,float(Power3.split(",")[0])))
                    G = int(pow(G1,float(Power3.split(",")[1])))
                    B = int(pow(B1,float(Power3.split(",")[2])))
                    img.putpixel((w,h),(R,G,B))

                ### Add ###
                if(Add3!="0,0,0"):
                    R1,G1,B1 = img.getpixel((w,h))
                    R = int(R1+(float(Add3.split(",")[0])*255))
                    G = int(G1+(float(Add3.split(",")[1])*255))
                    B = int(B1+(float(Add3.split(",")[2])*255))

                    img.putpixel((w,h),(R,G,B))

                ### Subtract ###
                if(Subtract3!="0,0,0"):
                    R1,G1,B1 = img.getpixel((w,h))
                    R = int(R1-(float(Subtract3.split(",")[0])*255))
                    G = int(G1-(float(Subtract3.split(",")[1])*255))
                    B = int(B1-(float(Subtract3.split(",")[2])*255))
                    img.putpixel((w,h),(R,G,B))

                ### Clamp ###

                rMin = float(Min3.split(",")[0])*255
                gMin = float(Min3.split(",")[1])*255
                bMin = float(Min3.split(",")[2])*255

                rMax = float(Max3.split(",")[0])*255
                gMax = float(Max3.split(",")[1])*255
                bMax = float(Max3.split(",")[2])*255
            
                R1,G1,B1 = img.getpixel((w,h))

                R = int(min(max(R1, rMin), rMax))
                G = int(min(max(G1, gMin), gMax))
                B = int(min(max(B1, bMin), bMax))

                img.putpixel((w,h),(R,G,B))

        img.save(Output)

    #### Math #### 
    frame1 = Frame(root,width=100,bg=bgColor)
    frame1.grid(row=0,column=0,pady=10,padx=60,sticky=S)

    label_1 = Label(frame1,text="Math",font=("roboto",32),bg=bgColor,fg=fgColor)
    label_1.grid(row=0,column=0,pady=3,padx=60,sticky=S)

    label_2 = Label(frame1,text="R,G,B",font=("roboto",12),bg=bgColor,fg=fgColor)
    label_2.grid(row=1,column=0,pady=1,padx=5,sticky=S)



    #### Multiply #### 
    frame21 = Frame(root,width=25,bg=bgColor,highlightbackground=hlColor,highlightthickness=1)
    frame21.grid(row=3,column=0,pady=6,padx=12,sticky=W)

    labelMultiply = Label(frame21,text="MULTIPLY",font=("roboto",fontSizeSmall),bg=bgColor,fg=fgColor).grid(row=1,column=0,pady=6,padx=16)
    inputMultiply = Entry(frame21,width=10,font=("roboto",fontSizeSmall),bg=bgColor,fg=fgColor)
    inputMultiply.grid(row=2,column=0,pady=2,padx=16)
    inputMultiply.insert(0,"1,1,1")

    #### Power #### 
    frame22 = Frame(root,width=25,bg=bgColor,highlightbackground=hlColor,highlightthickness=1)
    frame22.grid(row=4,column=0,pady=6,padx=12,sticky=W)

    labelPower = Label(frame22,text="POWER",font=("roboto",fontSizeSmall),bg=bgColor,fg=fgColor).grid(row=1,column=0,pady=6,padx=16)
    inputPower = Entry(frame22,width=10,font=("roboto",fontSizeSmall),bg=bgColor,fg=fgColor)
    inputPower.grid(row=2,column=0,pady=2,padx=16)
    inputPower.insert(0,"1,1,1")



    #### Add #### 
    frame24 = Frame(root,width=25,bg=bgColor,highlightbackground=hlColor,highlightthickness=1)
    frame24.grid(row=3,column=0,pady=6,padx=147,sticky=W)

    labelAdd = Label(frame24,text="ADD",font=("roboto",fontSizeSmall),bg=bgColor,fg=fgColor).grid(row=1,column=0,pady=6,padx=16)
    inputAdd = Entry(frame24,width=10,font=("roboto",fontSizeSmall),bg=bgColor,fg=fgColor)
    inputAdd.grid(row=2,column=0,pady=2,padx=16)
    inputAdd.insert(0,"0,0,0")

    #### Subtract #### 
    frame25 = Frame(root,width=25,bg=bgColor,highlightbackground=hlColor,highlightthickness=1)
    frame25.grid(row=4,column=0,pady=6,padx=147,sticky=W)

    labelSubtract = Label(frame25,text="SUBTRACT",font=("roboto",fontSizeSmall),bg=bgColor,fg=fgColor).grid(row=1,column=0,pady=6,padx=16)
    inputSubtract = Entry(frame25,width=10,font=("roboto",fontSizeSmall),bg=bgColor,fg=fgColor)
    inputSubtract.grid(row=2,column=0,pady=2,padx=16)
    inputSubtract.insert(0,"0,0,0")

    #### Max #### 
    frame26 = Frame(root,width=25,bg=bgColor,highlightbackground=hlColor,highlightthickness=1)
    frame26.grid(row=3,column=0,pady=6,padx=12,sticky=E)

    labelMax = Label(frame26,text="MAX",font=("roboto",fontSizeSmall),bg=bgColor,fg=fgColor).grid(row=1,column=0,pady=6,padx=16)
    inputMax = Entry(frame26,width=10,font=("roboto",fontSizeSmall),bg=bgColor,fg=fgColor)
    inputMax.grid(row=2,column=0,pady=2,padx=16)
    inputMax.insert(0,"1,1,1")

    #### Min #### 
    frame27 = Frame(root,width=25,bg=bgColor,highlightbackground=hlColor,highlightthickness=1)
    frame27.grid(row=4,column=0,pady=6,padx=12,sticky=E)

    labelMin = Label(frame27,text="MIN",font=("roboto",fontSizeSmall),bg=bgColor,fg=fgColor).grid(row=1,column=0,pady=6,padx=16)
    inputMin = Entry(frame27,width=10,font=("roboto",fontSizeSmall),bg=bgColor,fg=fgColor)
    inputMin.grid(row=2,column=0,pady=2,padx=16)
    inputMin.insert(0,"0,0,0")




    #### INPUT PATH #### 
    frame51 = Frame(root,width=100,bg=bgColor,highlightbackground=hlColor,highlightthickness=1)
    frame51.grid(row=5,column=0,pady=6,padx=12,sticky=S)

    labelInputFile = Label(frame51,text="INPUT FILE",font=("roboto",fontSizeSmall),bg=bgColor,fg=fgColor)
    labelInputFile.grid(row=1,column=0,sticky=S,pady=6,padx=16)

    inputInputFile = Entry(frame51,width=40,font=("roboto",fontSizeSmall),bg=bgColor,fg=fgColor)
    inputInputFile.grid(row=2,column=0,sticky=S,pady=2,padx=16)
    inputInputFile.insert(0,inputOutput1)

    #### OUTPUT PATH #### 
    frame52 = Frame(root,width=100,bg=bgColor,highlightbackground=hlColor,highlightthickness=1)
    frame52.grid(row=6,column=0,pady=6,padx=12,sticky=S)

    labelOutput = Label(frame52,text="OUTPUT FILE RGB",font=("roboto",fontSizeSmall),bg=bgColor,fg=fgColor)
    labelOutput.grid(row=1,column=0,sticky=S,pady=6,padx=16)

    inputOutput = Entry(frame52,width=40,font=("roboto",fontSizeSmall),bg=bgColor,fg=fgColor)
    inputOutput.grid(row=2,column=0,sticky=S,pady=2,padx=16)
    inputOutput.insert(0,inputOutput1)

    #### Generate #### 
    frame61 = Frame(root,width=100,bg=bgColor)
    frame61.grid(row=7,column=0,pady=10,padx=60,sticky=S)

    saveButton = Button(frame61,text="Save",font=("roboto",18),bg=bgColor,fg=fgColor,pady=2,padx=25,command=Generate)
    saveButton.grid(row=0,column=0,sticky=S,pady=2,padx=2)



    root.mainloop()
