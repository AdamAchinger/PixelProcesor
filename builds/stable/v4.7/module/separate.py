import os
from tkinter import *
from tkinter import filedialog
from PIL import Image
import customtkinter as ctk
import constants as c 
import utils as u 

if __name__ != "__main__" : 
    class Separate:
        def __init__(self, master):
            self.img = Image.open(c.previewPath)     

            leftTabFrame, frameTop, frameScroll, frameBottom = u.tabFrame(master)

            #### Input ####
            frame08 = ctk.CTkFrame(frameTop, width=400, height=30)
            frame08.pack(padx=2, pady=1)
            frame08.propagate(False)

            frame1 = ctk.CTkFrame(frameScroll)
            frame1.pack()
            frame01 = ctk.CTkFrame(frame1, width=c.cellW2, height=c.cellH)
            frame01.pack(padx=2, pady=2, side=LEFT)
            frame01.propagate(False)

            frame2 = ctk.CTkFrame(frameScroll)
            frame2.pack()
            frame02 = ctk.CTkFrame(frame2, width=c.cellW2, height=c.cellH)
            frame02.pack(padx=2, pady=2, side=LEFT)
            frame02.propagate(False)

            frame3 = ctk.CTkFrame(frameScroll)
            frame3.pack()
            frame03 = ctk.CTkFrame(frame3, width=c.cellW2, height=c.cellH)
            frame03.pack(padx=2, pady=2, side=LEFT)
            frame03.propagate(False)

            frame4 = ctk.CTkFrame(frameScroll)
            frame4.pack()
            frame04 = ctk.CTkFrame(frame4, width=c.cellW2, height=c.cellH)
            frame04.pack(padx=2, pady=2, side=LEFT)
            frame04.propagate(False)

            
            u.previewImage4(self,leftTabFrame)



            #### Input DIRECTORY ####
            buttonIn = ctk.CTkButton(frame08, text="Set Input",command=lambda: [self.set_input_dir(),u.update_preview(self)], width=100, font=c.sFont)
            buttonIn.pack(pady=2, padx=2, side=RIGHT)

            mainDirectoryIn = ctk.CTkLabel(frame08, text="Input:",width=32, font=c.sFont)
            mainDirectoryIn.pack(pady=2, padx=6, side=LEFT)

            self.mainDirectoryPathIn = ctk.CTkLabel(frame08,  text="Unset", text_color="red", font=c.sFont)
            self.mainDirectoryPathIn.pack(pady=2, padx=6,side=LEFT)

            GenerateButton = ctk.CTkButton(frameBottom, text="Separate", width=400, command=lambda: [self.generate(),u.update_preview(self)], height=40, font=c.bFont)
            GenerateButton.pack(pady=2, padx=2, side=RIGHT)



            #### Red #### 
            frame011 = ctk.CTkFrame(frame01, width=400, height=40)
            frame011.pack(padx=2, pady=1,fill=X,expand=TRUE)

            frame012 = ctk.CTkFrame(frame01, width=400, height=40)
            frame012.pack(padx=2, pady=1,fill=X,expand=TRUE)

            labelRed = ctk.CTkLabel(frame011, text="Red Channel", font=c.mFont)
            labelRed.pack(pady=6, padx=12, side=LEFT)

                #### OUTPUT FILE ####
            buttonOutRed = ctk.CTkButton(frame011, text="Set Red",command=self.set_red_channel, width=100, font=c.sFont)
            buttonOutRed.pack(pady=2, padx=2, side=RIGHT)

            mainDirectoryOutRed = ctk.CTkLabel(frame012, text="Output:", font=c.sFont)
            mainDirectoryOutRed.pack(pady=2, padx=6, side=LEFT)

            self.mainDirectoryPathOutRed = ctk.CTkLabel(frame012, text="Unset", text_color="red", font=c.sFont)
            self.mainDirectoryPathOutRed.pack(pady=2, padx=6,side=LEFT)   

            #### Green #### 
            frame021 = ctk.CTkFrame(frame02, width=400, height=40)
            frame021.pack(padx=2, pady=1,fill=X,expand=TRUE)

            frame022 = ctk.CTkFrame(frame02, width=400, height=40)
            frame022.pack(padx=2, pady=1,fill=X,expand=TRUE)

            labelGreen = ctk.CTkLabel(frame021, text="Green Channel", font=c.mFont)
            labelGreen.pack(pady=6, padx=12, side=LEFT)

                #### OUTPUT FILE ####
            buttonOutGreen = ctk.CTkButton(frame021, text="Set Green",command=self.set_green_channel, width=100, font=c.sFont)
            buttonOutGreen.pack(pady=2, padx=2, side=RIGHT)

            
            mainDirectoryOutGreen = ctk.CTkLabel(frame022, text="Output:", font=c.sFont)
            mainDirectoryOutGreen.pack(pady=2, padx=6, side=LEFT)

            self.mainDirectoryPathOutGreen = ctk.CTkLabel(frame022, text="Unset", text_color="red", font=c.sFont)
            self.mainDirectoryPathOutGreen.pack(pady=2, padx=6,side=LEFT)   
            

            #### Blue #### 
            frame031 = ctk.CTkFrame(frame03, width=400, height=40)
            frame031.pack(padx=2, pady=1,fill=X,expand=TRUE)

            frame032 = ctk.CTkFrame(frame03, width=400, height=40)
            frame032.pack(padx=2, pady=1,fill=X,expand=TRUE)

            labelBlue = ctk.CTkLabel(frame031, text="Blue Channel", font=c.mFont)
            labelBlue.pack(pady=6, padx=12, side=LEFT)


                #### OUTPUT FILE ####
            buttonOutBlue = ctk.CTkButton(frame031, text="Set Blue",command=self.set_blue_channel, width=100, font=c.sFont)
            buttonOutBlue.pack(pady=2, padx=2, side=RIGHT)

            
            mainDirectoryOutBlue = ctk.CTkLabel(frame032, text="Output:", font=c.sFont)
            mainDirectoryOutBlue.pack(pady=2, padx=6, side=LEFT)
            
            self.mainDirectoryPathOutBlue = ctk.CTkLabel(frame032, text="Unset", text_color="red", font=c.sFont)
            self.mainDirectoryPathOutBlue.pack(pady=2, padx=6,side=LEFT)   

            #### Alpha #### 
            frame041 = ctk.CTkFrame(frame04, width=400, height=40)
            frame041.pack(padx=2, pady=1,fill=X,expand=TRUE)

            frame042 = ctk.CTkFrame(frame04, width=400, height=40)
            frame042.pack(padx=2, pady=1,fill=X,expand=TRUE)

            labelAlpha = ctk.CTkLabel(frame041, text="Alpha Channel", font=c.mFont)
            labelAlpha.pack(pady=6, padx=16, side=LEFT)

                #### OUTPUT FILE ####
            buttonOutAlpha = ctk.CTkButton(frame041, text="Set Alpha",command=self.set_alpha_channel, width=100, font=c.sFont)
            buttonOutAlpha.pack(pady=2, padx=2, side=RIGHT)   
            
            mainDirectoryOutAlpha = ctk.CTkLabel(frame042, text="Output:", font=c.sFont)
            mainDirectoryOutAlpha.pack(pady=2, padx=6, side=LEFT)

            self.mainDirectoryPathOutAlpha = ctk.CTkLabel(frame042, text="Unset", text_color="red", font=c.sFont)
            self.mainDirectoryPathOutAlpha.pack(pady=2, padx=6,side=LEFT)   



        def set_red_channel(self):
            self.OutputFilePathRed = filedialog.asksaveasfilename(title="Output Red Channel")
            if (self.OutputFilePathRed != ""):
                self.OutputFilePathRed1 = self.OutputFilePathRed.split("/")[-1]
                self.mainDirectoryPathOutRed.configure(text=self.OutputFilePathRed1,text_color="white")

        def set_green_channel(self):
            self.OutputFilePathGreen = filedialog.asksaveasfilename(title="Output Green Channel")
            if (self.OutputFilePathGreen != ""):
                self.OutputFilePathGreen1 = self.OutputFilePathGreen.split("/")[-1]
                self.mainDirectoryPathOutGreen.configure(text=self.OutputFilePathGreen1,text_color="white")

        def set_blue_channel(self):
            self.OutputFilePathBlue = filedialog.asksaveasfilename(title="Output Blue Channel")
            if (self.OutputFilePathBlue != ""):
                self.OutputFilePathBlue1 = self.OutputFilePathBlue.split("/")[-1]
                self.mainDirectoryPathOutBlue.configure(text=self.OutputFilePathBlue1,text_color="white")

        def set_alpha_channel(self):
            self.OutputFilePathAlpha = filedialog.asksaveasfilename(title="Output Alpha Channel")
            if (self.OutputFilePathAlpha != ""):
                self.OutputFilePathAlpha1 = self.OutputFilePathAlpha.split("/")[-1]
                self.mainDirectoryPathOutAlpha.configure(text=self.OutputFilePathAlpha1,text_color="white")

        def set_input_dir(self):
            self.InputFilePath = filedialog.askopenfilename(title="Output File")
            self.img = Image.open(self.InputFilePath)
            if (self.InputFilePath != ""):
                #self.OutputStatus.configure(text="Ready", text_color="green")
                self.InputFilePath1 = self.InputFilePath.split("/")[-1]
                self.mainDirectoryPathIn.configure(text=self.InputFilePath1,text_color="white",font=c.sFont1)
                

        OutputFilePathRed = ""
        OutputFilePathGreen = ""
        OutputFilePathBlue = ""
        OutputFilePathAlpha = ""


        def generate(self):

            imgOutputRed = self.OutputFilePathRed  
            imgOutputGreen = self.OutputFilePathGreen
            imgOutputBlue = self.OutputFilePathBlue
            imgOutputAlpha = self.OutputFilePathAlpha

            
            Input = self.InputFilePath
            
            if ( Input != "" ):
                imgInput = Image.open(Input)
                
                maxsize = imgInput.size
                Width, Height = maxsize

                if(imgOutputRed != ""):
                    imgRed = Image.new(mode="L", size=(Width, Height))
                    
                if(imgOutputGreen != ""):
                    imgGreen = Image.new(mode="L", size=(Width, Height))

                if(imgOutputBlue != ""):
                    imgBlue = Image.new(mode="L", size=(Width, Height))

                if(imgOutputAlpha != ""):
                    imgAlpha = Image.new(mode="L",size=(Width, Height))

                R, G, B, A = 0,0,0,255
                
                for w in range(Width):
                    for h in range(Height):

                        Pixel = imgInput.getpixel((w,h))
                        R,G,B,A = Pixel

                        if(imgOutputRed != ""):
                            imgRed.putpixel((w, h), (R))

                        if(imgOutputGreen != ""):
                            imgGreen.putpixel((w, h), (G))

                        if(imgOutputBlue != ""):
                            imgBlue.putpixel((w, h), (B))

                        if(imgOutputAlpha != ""):
                            imgAlpha.putpixel((w, h), (A))


                if(imgOutputRed != ""):
                    imgRed.save(imgOutputRed)

                if(imgOutputGreen != ""):
                    imgGreen.save(imgOutputGreen)

                if(imgOutputBlue != ""):
                    imgBlue.save(imgOutputBlue)  

                if(imgOutputAlpha != ""):
                    imgAlpha.save(imgOutputAlpha)             
