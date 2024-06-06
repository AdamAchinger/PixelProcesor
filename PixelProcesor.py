import os
from lib import SolidColor
from lib import Gradient
from lib import Math
from tkinter import * 
from tkinter import messagebox 
from tkinter import filedialog
import subprocess

### Version
toolVersion = 4.1
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
appWidth = 343
appHeight = 170
# get windows screan width and height
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
# center position 
appXpos = int((screenWidth/2)-(appWidth/2))
appYpos = int((screenHeight/2)-(appHeight/2)-250)
# create app window 
root.geometry(f'{appWidth}x{appHeight}+{appXpos}+{appYpos}')
#####

#### Pixel Procesor #### 
frame1 = Frame(root,width=100,bg=bgColor)
frame1.grid(row=0,column=0,pady=6,padx=12)

label_1 = Label(frame1,text="Pixel Procesor",font=("roboto",32),bg=bgColor,fg=fgColor).grid(row=0,column=0,pady=2,padx=16)

#### Functions ####

def execute1():
    SolidColor.SolidColor()

def execute2():
    Gradient.Gradient()

def execute3():
    Math.Math()


#### Menu #### 

frame0 = Frame(root,width=100,bg=bgColor,highlightbackground=hlColor,highlightthickness=1)
frame0.grid(row=1,column=0,pady=6,padx=12)


solidColorButton = Button(frame0,text="Solid Color",font=("roboto",14),bg=bgColor,fg=fgColor,command=execute1)
solidColorButton.pack(side = LEFT,pady=5,padx=5)

gradientButton = Button(frame0,text="Gradient",font=("roboto",14),bg=bgColor,fg=fgColor,command=execute2)
gradientButton.pack(side = LEFT,pady=5,padx=5)

mathButton = Button(frame0,text="Math",font=("roboto",14),bg=bgColor,fg=fgColor,command=execute3)
mathButton.pack(side = LEFT,pady=5,padx=5)

'''
#### GLOBAL OUTPUT DIRECTORY #### 

frame5 = Frame(root,width=400,bg=bgColor,highlightbackground=hlColor,highlightthickness=0)
frame5.grid(row=6,column=0,pady=6,padx=6,sticky=W)

mainDirectory = Label(frame5,text="Directory:",font=("roboto",12),bg=bgColor,fg=fgColor)
mainDirectory.grid(row=2,column=0,pady=2,padx=6,sticky=W)

mainDirectoryStatus = Label(frame5,text="Unset",font=("roboto",13),bg=bgColor,fg="red")
mainDirectoryStatus.grid(row=2,column=0,pady=2,padx=80,sticky=W)

mainDirectoryPath = Label(frame5,text="----",font=("roboto",12),bg=bgColor,fg=fgColor)
mainDirectoryPath.grid(row=3,column=0,pady=2,padx=6,sticky=W)

Path = ""

def Directory():
    global Path
    Path = filedialog.askdirectory(title="Main Directory")
    mainDirectoryStatus.config(text="Ready",fg="green")
    mainDirectoryPath.config(text=Path)

framePanel = Frame(root,width=400,bg=bgColor,highlightbackground=hlColor,highlightthickness=1)
framePanel.grid(row=5,column=0,pady=6,padx=6,sticky=S)

button = Button(framePanel,text="Default Directory",command=Directory,font=("roboto",fontSizeSmall-2),bg=bgColor,fg=fgColor)
button.grid(row=0,column=0,sticky=W,pady=2,padx=6)
'''


root.mainloop()
