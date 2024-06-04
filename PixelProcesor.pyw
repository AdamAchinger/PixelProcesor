import os
from lib import SolidColor
from lib import Gradient
from lib import Math
from tkinter import * 
from tkinter import messagebox 

### Version
toolVersion = 3.1
###


root = Tk()

bgColor = "#353535"
fgColor = "#C0C0C0"
hlColor = "#777777"
fontSizeSmall = 13


root.configure(bg=bgColor)
root.title("Pixel Procesor"+" v"+str(toolVersion))
root.iconbitmap('S:\GitHub\PixelProcesor\img\AA_icon.ico')
root.resizable(False,False)

#####
# application dimensions
appWidth = 340
appHeight = 280
# get windows screan width and height
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
# center position 
appXpos = int((screenWidth/2)-(appWidth/2))
appYpos = int((screenHeight/2)-(appHeight/2))
# create app window 
root.geometry(f'{appWidth}x{appHeight}+{appXpos}+{appYpos}')
#####

#### Pixel Procesor #### 
frame1 = Frame(root,width=100,bg=bgColor)
frame1.grid(row=0,column=0,pady=6,padx=12)

label_1 = Label(frame1,text="Pixel Procesor",font=("roboto",32),bg=bgColor,fg=fgColor).grid(row=0,column=0,pady=2,padx=16)

#### Functions ####

def execute1():
    SolidColor.SolidColor(inputOutput.get())

def execute2():
    Gradient.Gradient(inputOutput.get())

def execute3():
    Math.Math(inputOutput.get())


#### Menu #### 

frame0 = Frame(root,width=100,bg=bgColor,highlightbackground=hlColor,highlightthickness=1)
frame0.grid(row=1,column=0,pady=6,padx=12)


solidColorButton = Button(frame0,text="Solid Color",font=("roboto",14),bg=bgColor,fg=fgColor,command=execute1)
solidColorButton.pack(side = LEFT,pady=5,padx=5)

gradientButton = Button(frame0,text="Gradient",font=("roboto",14),bg=bgColor,fg=fgColor,command=execute2)
gradientButton.pack(side = LEFT,pady=5,padx=5)

frame1 = Frame(root,width=100,bg=bgColor,highlightbackground=hlColor,highlightthickness=1)
frame1.grid(row=2,column=0,pady=6,padx=12)

mathButton = Button(frame1,text="Math",font=("roboto",14),bg=bgColor,fg=fgColor,command=execute3)
mathButton.pack(side = LEFT,pady=5,padx=5)


#### GLOBAL OUTPUT DIRECTORY #### 
frame5 = Frame(root,width=100,bg=bgColor,highlightbackground=hlColor,highlightthickness=1)
frame5.grid(row=4,column=0,pady=6,padx=12,sticky=N)

labelOutput = Label(frame5,text="GLOBAL OUTPUT DIRECTORY",font=("roboto",fontSizeSmall),bg=bgColor,fg=fgColor).grid(row=1,column=0,sticky=W,pady=2,padx=16)
inputOutput = Entry(frame5,width=30,font=("roboto",fontSizeSmall),bg=bgColor,fg=fgColor)
inputOutput.grid(row=2,column=0,sticky=W,pady=2,padx=15)
inputOutput.insert(0,"E:\.Temp")



root.mainloop()
