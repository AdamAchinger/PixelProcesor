import os
from tkinter import *
from tkinter import filedialog
from PIL import Image
import customtkinter as ctk
import constants as c 


if __name__ != "__main__" : 

    def tabFrame(master):
        frameMaster = ctk.CTkFrame(master,fg_color=c.fgColor)
        frameMaster.pack(fill=Y,expand=TRUE)

        frameTop = ctk.CTkFrame(frameMaster)
        frameTop.pack(padx=2,pady=2)

        leftTabFrame = ctk.CTkFrame(frameTop,width=500,fg_color=c.previewBorderColor)
        leftTabFrame.pack(padx=5,pady=5,side=LEFT) 

        rightTabFrame = ctk.CTkFrame(frameTop,width=400)
        rightTabFrame.pack(fill=Y,side=LEFT)
        
        frameTop = ctk.CTkFrame(rightTabFrame,height=50)
        frameTop.pack(padx=1,pady=1,side=TOP)

        frameScroll = ctk.CTkScrollableFrame(rightTabFrame,width=400)
        frameScroll.pack(padx=1,pady=1,fill=Y,expand=TRUE)  

        frameBottom = ctk.CTkFrame(frameMaster,height=50)
        frameBottom.pack(padx=1,pady=1,side=TOP,fill=X)

        return leftTabFrame,  frameTop, frameScroll, frameBottom


    def slider(master, label, isAlpha):
        frame = ctk.CTkFrame(master)
        frame.pack(padx=2, pady=1, fill=X)

        labelColor = ctk.CTkLabel(frame, text=label, font=c.mFont)
        labelColor.pack(padx=8, side=LEFT)

        sliderVar = ctk.DoubleVar()
        sliderVar.set(1 if isAlpha else 0.5)

        slider = ctk.CTkSlider(frame, variable=sliderVar, from_=0, to=1, width=200)
        slider.pack(padx=4, side=RIGHT)
        
        sliderEntry = ctk.CTkEntry(frame, textvariable=sliderVar, width=60,font=c.mFont)
        sliderEntry.pack(padx=4, side=RIGHT)

        return slider


    def export(self):
        self.exportButton.configure(state=DISABLED)
        self.img.save(self.full_path)


    def update_preview(self):        
        img_preview = ctk.CTkImage(light_image=self.img, size=(480, 480))
        self.previewLabel.configure(image=img_preview)
        self.previewLabel.image = img_preview

    def previewMethod(self,master,state):
        #self.varA = ctk.IntVar()
        #self.previewMethod = ctk.CTkSegmentedButton(master, state=state,variable=self.varA,width=250, values=c.extractMethod,  font=c.bFont)
        #self.previewMethod.set(c.extractMethod[1])
        #self.previewMethod.pack(pady=2, padx=4, side=LEFT)
        return self
    
    def previewImage(self,master):
        previewImage = ctk.CTkImage(light_image=self.img, size=(480, 480))
        self.previewLabel = ctk.CTkLabel(master, image=previewImage, text='')
        self.previewLabel.pack(pady=c.previewBorderWidth,padx=c.previewBorderWidth)
        return self
    




    def outputDir(self,master):
        self.Path = c.basePath
        self.mainDirectoryOut = ctk.CTkLabel(master, text="Output:", font=c.sFont).pack(pady=2, padx=6, side=LEFT)
        self.mainDirectoryPath = ctk.CTkLabel(master, text=self.Path, font=c.sFont)
        self.mainDirectoryPath.pack(pady=2, padx=6, side=LEFT)

        def get_directory(self):
            self.Path = filedialog.askdirectory(title="Directory")
            self.mainDirectoryPath.configure(text=self.Path)
            return self
            
        button = ctk.CTkButton(master, text="Set Output", width=100, command=lambda:[get_directory(self)], font=c.sFont)
        button.pack(pady=2, padx=2,side=RIGHT)
        return self
    
    
    def inputFile(self,master):
        self.FilePathIn = c.baseFileIn
        self.mainFileIn = ctk.CTkLabel(master, text="Input:", font=c.sFont).pack(pady=2, padx=6, side=LEFT)
        self.mainFileI = ctk.CTkLabel(master, text=self.FilePathIn.split("\\")[-1], font=c.sFont)
        self.mainFileI.pack(pady=2, padx=6, side=LEFT)

        def get_file(self):
            self.FilePathIn = filedialog.askopenfilename(title="Input File")
            self.InputFilePath1 = self.FilePathIn.split("/")[-1]
            self.mainFileI.configure(text=self.InputFilePath1)
            return self

        button = ctk.CTkButton(master, text="Set Input", width=100, command=lambda:[get_file(self)], font=c.sFont)
        button.pack(pady=2, padx=2,side=RIGHT)
        return self
    
    
    def outputFile(self,master):
        self.FilePathOut = c.baseFileOut
        self.mainFileOut = ctk.CTkLabel(master, text="Output:", font=c.sFont).pack(pady=2, padx=6, side=LEFT)
        self.mainFileO = ctk.CTkLabel(master, text=self.FilePathOut.split("\\")[-1], font=c.sFont)
        self.mainFileO.pack(pady=2, padx=6, side=LEFT)

        def set_file(self):
            self.FilePathOut = filedialog.asksaveasfilename(title="Output File")
            self.OutputFilePath1 = self.FilePathOut.split("/")[-1]
            self.mainFileO.configure(text=self.OutputFilePath1)
            return self
        
        button = ctk.CTkButton(master, text="Set Output", width=100, command=lambda:[set_file(self)], font=c.sFont)
        button.pack(pady=2, padx=2,side=RIGHT)
        return self
    


    
    

