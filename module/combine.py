import os
from tkinter import *
from tkinter import filedialog
from PIL import Image
import customtkinter as ctk
import constants as c 
import utils as u 

if __name__ != "__main__" : 
    class Combine:
        def __init__(self, master):

            frameMaster = ctk.CTkFrame(master,fg_color=c.fgColor)
            frameMaster.pack(fill=Y,expand=TRUE)

            frameTop = ctk.CTkFrame(frameMaster,height=50)
            frameTop.pack(padx=1,pady=1,side=TOP)

            frameScroll = ctk.CTkScrollableFrame(frameMaster,width=400)
            frameScroll.pack(padx=1,pady=1,fill=Y,expand=TRUE)  

            frameBottom = ctk.CTkFrame(frameMaster,height=50)
            frameBottom.pack(padx=1,pady=1,side=BOTTOM)
        
            #### Input ####
            frame1 = ctk.CTkFrame(frameScroll)
            frame1.pack()

            frame2 = ctk.CTkFrame(frameScroll)
            frame2.pack()

            frame3 = ctk.CTkFrame(frameScroll)
            frame3.pack()

            frame4 = ctk.CTkFrame(frameScroll)
            frame4.pack()

            frame01 = ctk.CTkFrame(frame1, width=c.cellW2, height=c.cellH)
            frame01.pack(padx=2, pady=2, side=LEFT)
            frame01.propagate(False)

            frame02 = ctk.CTkFrame(frame2, width=c.cellW2, height=c.cellH)
            frame02.pack(padx=2, pady=2, side=LEFT)
            frame02.propagate(False)

            frame03 = ctk.CTkFrame(frame3, width=c.cellW2, height=c.cellH)
            frame03.pack(padx=2, pady=2, side=LEFT)
            frame03.propagate(False)

            frame04 = ctk.CTkFrame(frame4, width=c.cellW2, height=c.cellH)
            frame04.pack(padx=2, pady=2, side=LEFT)
            frame04.propagate(False)

            
            frame09 = ctk.CTkFrame(frameTop, width=400, height=30)
            frame09.pack(padx=2, pady=1)
            frame09.propagate(False)



            #### OUTPUT DIRECTORY ####
            buttonOut = ctk.CTkButton(frame09, text="Set Output",command=self.set_output_dir, width=100, font=c.sFont)
            buttonOut.pack(pady=2, padx=2, side=RIGHT)

            mainDirectoryOut = ctk.CTkLabel(frame09, text="Output:",width=32, font=c.sFont)
            mainDirectoryOut.pack(pady=2, padx=6, side=LEFT)

            self.mainDirectoryPathOut = ctk.CTkLabel(frame09,  text="Unset", text_color="red", font=c.sFont)
            self.mainDirectoryPathOut.pack(pady=2, padx=6,side=LEFT)

            GenerateButton = ctk.CTkButton(frameBottom, text="Combine", width=c.appWidth, command=self.generate, height=40, font=c.bFont)
            GenerateButton.pack(pady=2, padx=2, side=LEFT)



            #### Red #### 
            frame011 = ctk.CTkFrame(frame01, width=400, height=40)
            frame011.pack(padx=2, pady=1,fill=X,expand=TRUE)

            frame012 = ctk.CTkFrame(frame01, width=400, height=40)
            frame012.pack(padx=2, pady=1,fill=X,expand=TRUE)

            labelRed = ctk.CTkLabel(frame011, text="Red Channel", font=c.mFont)
            labelRed.pack(pady=6, padx=12, side=LEFT)

                #### INPUT FILE ####
            buttonInRed = ctk.CTkButton(frame011, text="Set Red",command=self.set_red_channel, width=100, font=c.sFont)
            buttonInRed.pack(pady=2, padx=2, side=RIGHT)

                #### EXTRACT ####
            self.var21 = ctk.IntVar()
            self.inputExtractRed = ctk.CTkOptionMenu(frame011, variable=self.var21, values=c.ExtractColors, width=85, font=c.sFont)
            self.inputExtractRed.set(c.ExtractColors[0])
            self.inputExtractRed.pack(pady=2, padx=1,side=RIGHT)

            mainDirectoryInRed = ctk.CTkLabel(frame012, text="Input:", font=c.sFont)
            mainDirectoryInRed.pack(pady=2, padx=6, side=LEFT)

            self.mainDirectoryPathInRed = ctk.CTkLabel(frame012, text="Unset", text_color="red", font=c.sFont)
            self.mainDirectoryPathInRed.pack(pady=2, padx=6,side=LEFT)   

            #### Green #### 
            frame021 = ctk.CTkFrame(frame02, width=400, height=40)
            frame021.pack(padx=2, pady=1,fill=X,expand=TRUE)

            frame022 = ctk.CTkFrame(frame02, width=400, height=40)
            frame022.pack(padx=2, pady=1,fill=X,expand=TRUE)

            labelGreen = ctk.CTkLabel(frame021, text="Green Channel", font=c.mFont)
            labelGreen.pack(pady=6, padx=12, side=LEFT)

                #### INPUT FILE ####
            buttonInGreen = ctk.CTkButton(frame021, text="Set Green",command=self.set_green_channel, width=100, font=c.sFont)
            buttonInGreen.pack(pady=2, padx=2, side=RIGHT)

                #### EXTRACT ####
            self.var22 = ctk.IntVar()
            self.inputExtractGreen = ctk.CTkOptionMenu(frame021, variable=self.var22, values=c.ExtractColors, width=85, font=c.sFont)
            self.inputExtractGreen.set(c.ExtractColors[0])
            self.inputExtractGreen.pack(pady=2, padx=1,side=RIGHT)
            
            mainDirectoryInGreen = ctk.CTkLabel(frame022, text="Input:", font=c.sFont)
            mainDirectoryInGreen.pack(pady=2, padx=6, side=LEFT)

            self.mainDirectoryPathInGreen = ctk.CTkLabel(frame022, text="Unset", text_color="red", font=c.sFont)
            self.mainDirectoryPathInGreen.pack(pady=2, padx=6,side=LEFT)   
            

            #### Blue #### 
            frame031 = ctk.CTkFrame(frame03, width=400, height=40)
            frame031.pack(padx=2, pady=1,fill=X,expand=TRUE)

            frame032 = ctk.CTkFrame(frame03, width=400, height=40)
            frame032.pack(padx=2, pady=1,fill=X,expand=TRUE)

            labelBlue = ctk.CTkLabel(frame031, text="Blue Channel", font=c.mFont)
            labelBlue.pack(pady=6, padx=12, side=LEFT)



                #### INPUT FILE ####
            buttonInBlue = ctk.CTkButton(frame031, text="Set Blue",command=self.set_blue_channel, width=100, font=c.sFont)
            buttonInBlue.pack(pady=2, padx=2, side=RIGHT)

                #### EXTRACT ####
            self.var23 = ctk.IntVar()
            self.inputExtractBlue= ctk.CTkOptionMenu(frame031, variable=self.var23, values=c.ExtractColors, width=85, font=c.sFont)
            self.inputExtractBlue.set(c.ExtractColors[0])
            self.inputExtractBlue.pack(pady=2, padx=1,side=RIGHT)
            
            mainDirectoryInBlue = ctk.CTkLabel(frame032, text="Input:", font=c.sFont)
            mainDirectoryInBlue.pack(pady=2, padx=6, side=LEFT)
            
            self.mainDirectoryPathInBlue = ctk.CTkLabel(frame032, text="Unset", text_color="red", font=c.sFont)
            self.mainDirectoryPathInBlue.pack(pady=2, padx=6,side=LEFT)   

            #### Alpha #### 
            frame041 = ctk.CTkFrame(frame04, width=400, height=40)
            frame041.pack(padx=2, pady=1,fill=X,expand=TRUE)

            frame042 = ctk.CTkFrame(frame04, width=400, height=40)
            frame042.pack(padx=2, pady=1,fill=X,expand=TRUE)

            labelAlpha = ctk.CTkLabel(frame041, text="Alpha Channel", font=c.mFont)
            labelAlpha.pack(pady=6, padx=16, side=LEFT)

                #### INPUT FILE ####
            buttonInAlpha = ctk.CTkButton(frame041, text="Set Alpha",command=self.set_alpha_channel, width=100, font=c.sFont)
            buttonInAlpha.pack(pady=2, padx=2, side=RIGHT)   

                #### EXTRACT ####
            self.var24 = ctk.IntVar()
            self.inputExtractAlpha= ctk.CTkOptionMenu(frame041, variable=self.var24, values=c.ExtractColors, width=85, font=c.sFont)
            self.inputExtractAlpha.set(c.ExtractColors[0])
            self.inputExtractAlpha.pack(pady=2, padx=1,side=RIGHT)

            
            mainDirectoryInAlpha = ctk.CTkLabel(frame042, text="Input:", font=c.sFont)
            mainDirectoryInAlpha.pack(pady=2, padx=6, side=LEFT)

            self.mainDirectoryPathInAlpha = ctk.CTkLabel(frame042, text="Unset", text_color="red", font=c.sFont)
            self.mainDirectoryPathInAlpha.pack(pady=2, padx=6,side=LEFT)   



        def set_red_channel(self):
            self.InputFilePathRed = filedialog.askopenfilename(title="Input Red Channel")
            if (self.InputFilePathRed != ""):
                self.InputFilePathRed1 = self.InputFilePathRed.split("/")[-1]
                self.mainDirectoryPathInRed.configure(text=self.InputFilePathRed1,text_color="white")

        def set_green_channel(self):
            self.InputFilePathGreen = filedialog.askopenfilename(title="Input Green Channel")
            if (self.InputFilePathGreen != ""):
                self.InputFilePathGreen1 = self.InputFilePathGreen.split("/")[-1]
                self.mainDirectoryPathInGreen.configure(text=self.InputFilePathGreen1,text_color="white")

        def set_blue_channel(self):
            self.InputFilePathBlue = filedialog.askopenfilename(title="Input Blue Channel")
            if (self.InputFilePathBlue != ""):
                self.InputFilePathBlue1 = self.InputFilePathBlue.split("/")[-1]
                self.mainDirectoryPathInBlue.configure(text=self.InputFilePathBlue1,text_color="white")

        def set_alpha_channel(self):
            self.InputFilePathAlpha = filedialog.askopenfilename(title="Input Alpha Channel")
            if (self.InputFilePathAlpha != ""):
                self.InputFilePathAlpha1 = self.InputFilePathAlpha.split("/")[-1]
                self.mainDirectoryPathInAlpha.configure(text=self.InputFilePathAlpha1,text_color="white")

        def set_output_dir(self):
            self.OutputFilePath = filedialog.asksaveasfilename(title="Output File")
            if (self.OutputFilePath != ""):
                #self.OutputStatus.configure(text="Ready", text_color="green")
                self.OutputFilePath1 = self.OutputFilePath.split("/")[-1]
                self.mainDirectoryPathOut.configure(text=self.OutputFilePath1,text_color="white",font=c.sFont1)

        InputFilePathRed = ""
        InputFilePathGreen = ""
        InputFilePathBlue = ""
        InputFilePathAlpha = ""


        def generate(self):

            imgInputRed = self.InputFilePathRed  
            extInputRed  = self.inputExtractRed.get()

            imgInputGreen = self.InputFilePathGreen
            extInputGreen  = self.inputExtractGreen.get() 

            imgInputBlue = self.InputFilePathBlue
            extInputBlue = self.inputExtractBlue.get()

            imgInputAlpha = self.InputFilePathAlpha
            extInputAlpha = self.inputExtractAlpha.get()
            
            Output = self.OutputFilePath

            if ( Output != "" ):

                if(imgInputRed == ""):
                    imgRed = Image.new(mode="RGBA", size=(16, 16))
                else:
                    imgRed = Image.open(imgInputRed)
                    imgRed.convert("RGBA")
                    
                if(imgInputGreen == ""):
                    imgGreen = Image.new(mode="RGBA", size=(16, 16))
                else:
                    imgGreen = Image.open(imgInputGreen)
                    imgGreen.convert("RGBA")

                if(imgInputBlue == ""):
                    imgBlue = Image.new(mode="RGBA", size=(16, 16))
                else:
                    imgBlue = Image.open(imgInputBlue)
                    imgBlue.convert("RGBA")

                if(imgInputAlpha == ""):
                    imgAlpha = Image.new(mode="RGBA", size=(16, 16),color=(255,255,255))
                else:
                    imgAlpha = Image.open(imgInputAlpha)
                    imgAlpha.convert("RGBA")
                

                maxsize = max(imgRed.size,imgGreen.size,imgBlue.size,imgAlpha.size)
                Width, Height = maxsize

                imgNew= Image.new(mode="RGBA", size=(Width, Height))

                print(f"w={Width} , h={Height}")
                print(extInputRed)

                imgRed = imgRed.resize((Width,Height),resample=Image.LANCZOS)
                imgGreen = imgGreen.resize((Width,Height),resample=Image.LANCZOS)
                imgBlue = imgBlue.resize((Width,Height),resample=Image.LANCZOS)
                imgAlpha = imgAlpha.resize((Width,Height),resample=Image.LANCZOS)
                
                print(imgRed.size)
                print(imgGreen.size)
                print(imgBlue.size)
                print(imgAlpha.size)

                def pixel_color(imgRed,w,h,extInputRed):

                    Pixel = imgRed.getpixel((w, h))
                    if isinstance(Pixel, int):
                        pR = pG = pB = pA = Pixel
                    else:
                        pR, pG, pB, *pRest = Pixel
                        if(pRest):
                            pA = pRest[0] 
                        else:
                            pA = 255

                    Channels = {
                        "Red": pR,
                        "Green": pG,
                        "Blue": pB,
                        "Alpha": pA
                    }

                    return Channels.get(extInputRed)
                
                R, G, B, A = 0,0,0,255
                for w in range(Width):
                    for h in range(Height):

                        R = pixel_color(imgRed,w,h,extInputRed)
                        G = pixel_color(imgGreen,w,h,extInputGreen)
                        B = pixel_color(imgBlue,w,h,extInputBlue)               
                        A = pixel_color(imgAlpha,w,h,extInputAlpha)

                        #print(f"R={type(R)} G={type(G)} B={type(B)} A={type(A)}")
                        imgNew.putpixel((w, h), (R, G, B, A))

                imgNew.save(Output)
