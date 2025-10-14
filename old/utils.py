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


    def slider(master, label, isAlpha,default=0.5):
        frame = ctk.CTkFrame(master)
        frame.pack(padx=2, pady=1, fill=X)

        labelColor = ctk.CTkLabel(frame, text=label, font=c.mFont)
        labelColor.pack(padx=8, side=LEFT)

        sliderVar = ctk.DoubleVar()
        sliderVar.set(1 if isAlpha else default)

        slider = ctk.CTkSlider(frame, variable=sliderVar, from_=0, to=1, width=200)
        slider.pack(padx=4, side=RIGHT)
        
        sliderEntry = ctk.CTkEntry(frame, textvariable=sliderVar, width=60,font=c.mFont)
        sliderEntry.pack(padx=4, side=RIGHT)

        return slider


    def export(self):
        #self.exportButton.configure(state=DISABLED)
        self.img.save(self.full_path)

    def previewMethod(self,master,state):
        #self.varA = ctk.IntVar()
        #self.previewMethod = ctk.CTkSegmentedButton(master, state=state,variable=self.varA,width=250, values=c.extractMethod,  font=c.bFont)
        #self.previewMethod.set(c.extractMethod[1])
        #self.previewMethod.pack(pady=2, padx=4, side=LEFT)
        return self
    
    def update_preview(self):
        """Aktualizuje podgląd obrazu (pojedynczy lub 4 kanały)"""
        if hasattr(self, 'preview_labels') and self.preview_labels:
            # Aktualizacja 4 kanałów
            channels = self.img.split()
            size = (240, 240)
            # Uzupełnij do 4 kanałów, jeśli mniej
            while len(channels) < 4:
                channels += (Image.new("L", self.img.size, 0),)
            
            for i, label in enumerate(self.preview_labels):
                img = ctk.CTkImage(light_image=channels[i], size=size)
                label.configure(image=img)
                label.image = img
        elif hasattr(self, 'previewLabel') and self.previewLabel:
            # Aktualizacja pojedynczego podglądu
            img_preview = ctk.CTkImage(light_image=self.img, size=(480, 480))
            self.previewLabel.configure(image=img_preview)
            self.previewLabel.image = img_preview

    def previewImage(self, master):
        """Tworzy pojedynczy podgląd obrazu"""
        previewImage = ctk.CTkImage(light_image=self.img, size=(480, 480))
        self.previewLabel = ctk.CTkLabel(master, image=previewImage, text='')
        self.previewLabel.pack(pady=c.previewBorderWidth, padx=c.previewBorderWidth)
        self.preview_labels = None  # Oznacz, że to pojedynczy podgląd
        return self

    def previewImage4(self, master):
        """Tworzy podgląd 4 kanałów"""
        channels = list(self.img.split())
        size = (236, 236)
        
        # Uzupełnij brakujące kanały pustymi obrazami
        original_channel_count = len(channels)
        while len(channels) < 4:
            channels.append(Image.new("L", self.img.size, 0))
        
        # Główna ramka
        frame = ctk.CTkFrame(master)
        frame.pack(pady=c.previewBorderWidth, padx=c.previewBorderWidth)
        
        # Lista do przechowania referencji do labeli
        self.preview_labels = []
        self.previewLabel = None  # Oznacz, że to podgląd 4-kanałowy
        
        # Wiersz 1
        row1 = ctk.CTkFrame(frame)
        row1.pack(side="top")
        
        for i in range(2):
            img = ctk.CTkImage(light_image=channels[i], size=size)
            lbl = ctk.CTkLabel(row1, image=img, text='')
            lbl.image = img
            lbl.pack(side="left", padx=2, pady=2)
            self.preview_labels.append(lbl)
        
        # Wiersz 2
        row2 = ctk.CTkFrame(frame)
        row2.pack(side="top")
        
        for i in range(2, 4):
            # Jeśli kanał nie istniał w oryginalnym obrazie, nie aktualizuj go
            if i < original_channel_count:
                img = ctk.CTkImage(light_image=channels[i], size=size)
            else:
                # Pozostaw czarny/pusty dla nieistniejących kanałów
                img = ctk.CTkImage(light_image=channels[i], size=size)
            lbl = ctk.CTkLabel(row2, image=img, text='')
            lbl.image = img
            lbl.pack(side="left", padx=2, pady=2)
            self.preview_labels.append(lbl)
        
        # Zapisz liczbę oryginalnych kanałów
        self.original_channel_count = original_channel_count


    

    def outputDir(self,master):
        self.Path = c.basePath
        self.mainDirectoryOut = ctk.CTkLabel(master, text="Output:", font=c.sFont).pack(pady=2, padx=6, side=LEFT)
        self.mainDirectoryPath = ctk.CTkLabel(master, text=self.Path, font=c.sFont)
        self.mainDirectoryPath.pack(pady=2, padx=6, side=LEFT)

        def get_directory(self):
            self.Path = filedialog.askdirectory(title="Directory")
            if self.Path == "":
               self.Path = c.basePath
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
            if self.FilePathIn == "":
               self.FilePathIn = c.baseFileIn
            self.InputFilePath1 = self.FilePathIn.split("\\")[-1]
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
            if self.FilePathOut == "":
               self.FilePathOut = c.baseFileOut
            self.OutputFilePath1 = self.FilePathOut.split("\\")[-1]
            self.mainFileO.configure(text=self.OutputFilePath1)
            return self
        
        button = ctk.CTkButton(master, text="Set Output", width=100, command=lambda:[set_file(self)], font=c.sFont)
        button.pack(pady=2, padx=2,side=RIGHT)
        return self
    


    
    

