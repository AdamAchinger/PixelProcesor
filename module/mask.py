import os
from tkinter import *
from tkinter import filedialog
from PIL import Image
import customtkinter as ctk
import constants as c 
import utils as u 

if __name__ != "__main__" : 
    class Mask:
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


            frame01 = ctk.CTkFrame(frame1, width=c.cellW2, height=c.cellH)
            frame01.pack(padx=2, pady=2, side=LEFT)
            frame01.propagate(False)

            frame02 = ctk.CTkFrame(frame2, width=c.cellW2, height=c.cellH)
            frame02.pack(padx=2, pady=2, side=LEFT)
            frame02.propagate(False)

            frame03 = ctk.CTkFrame(frame3, width=c.cellW2, height=c.cellH/2)
            frame03.pack(padx=2, pady=2, side=LEFT)
            frame03.propagate(False)


            
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

            GenerateButton = ctk.CTkButton(frameBottom, text="Mask", width=c.appWidth, command=self.generate, height=40, font=c.bFont)
            GenerateButton.pack(pady=2, padx=2, side=LEFT)



            #### A #### 
            frame011 = ctk.CTkFrame(frame01, width=400, height=40)
            frame011.pack(padx=2, pady=1,fill=X,expand=TRUE)

            frame012 = ctk.CTkFrame(frame01, width=400, height=40)
            frame012.pack(padx=2, pady=1,fill=X,expand=TRUE)

            labelA = ctk.CTkLabel(frame011, text="Image A", font=c.mFont)
            labelA.pack(pady=6, padx=12, side=LEFT)

                #### INPUT FILE ####
            buttonInA = ctk.CTkButton(frame011, text="Set A",command=self.set_a_img, width=100, font=c.sFont)
            buttonInA.pack(pady=2, padx=2, side=RIGHT)

                #### EXTRACT ####
            self.var21 = ctk.IntVar()
            self.inputExtractA = ctk.CTkOptionMenu(frame011, variable=self.var21, values=c.ExtractColors, width=85, font=c.sFont)
            self.inputExtractA.set(c.ExtractColors[0])
            self.inputExtractA.pack(pady=2, padx=1,side=RIGHT)

            mainDirectoryInA = ctk.CTkLabel(frame012, text="Input:", font=c.sFont)
            mainDirectoryInA.pack(pady=2, padx=6, side=LEFT)

            self.mainDirectoryPathInA = ctk.CTkLabel(frame012, text="Unset", text_color="red", font=c.sFont)
            self.mainDirectoryPathInA.pack(pady=2, padx=6,side=LEFT)   

            #### B #### 
            frame021 = ctk.CTkFrame(frame02, width=400, height=40)
            frame021.pack(padx=2, pady=1,fill=X,expand=TRUE)

            frame022 = ctk.CTkFrame(frame02, width=400, height=40)
            frame022.pack(padx=2, pady=1,fill=X,expand=TRUE)

            labelB = ctk.CTkLabel(frame021, text="Image B", font=c.mFont)
            labelB.pack(pady=6, padx=12, side=LEFT)

                #### INPUT FILE ####
            buttonInB = ctk.CTkButton(frame021, text="Set B",command=self.set_b_img, width=100, font=c.sFont)
            buttonInB.pack(pady=2, padx=2, side=RIGHT)

                #### EXTRACT ####
            self.var22 = ctk.IntVar()
            self.inputExtractB = ctk.CTkOptionMenu(frame021, variable=self.var22, values=c.ExtractColors, width=85, font=c.sFont)
            self.inputExtractB.set(c.ExtractColors[0])
            self.inputExtractB.pack(pady=2, padx=1,side=RIGHT)
            
            mainDirectoryInB = ctk.CTkLabel(frame022, text="Input:", font=c.sFont)
            mainDirectoryInB.pack(pady=2, padx=6, side=LEFT)

            self.mainDirectoryPathInB = ctk.CTkLabel(frame022, text="Unset", text_color="red", font=c.sFont)
            self.mainDirectoryPathInB.pack(pady=2, padx=6,side=LEFT)   
            

            #### Mask #### 
            frame031 = ctk.CTkFrame(frame03, width=400, height=40)
            frame031.pack(padx=2, pady=1,fill=X,expand=TRUE)


            extractMethod = ["A * B","A + B","A - B","B - A"]
                #### EXTRACT ####
            self.var23 = ctk.IntVar()
            self.inputExtractMethod = ctk.CTkSegmentedButton(frame031, variable=self.var23, values=extractMethod, width=100, font=c.bFont)
            self.inputExtractMethod.set(extractMethod[0])
            self.inputExtractMethod.pack(pady=2, padx=1)



        def set_a_img(self):
            self.InputFilePathRed = filedialog.askopenfilename(title="Input A Image")
            if (self.InputFilePathRed != ""):
                self.InputFilePathRed1 = self.InputFilePathRed.split("/")[-1]
                self.mainDirectoryPathInRed.configure(text=self.InputFilePathRed1,text_color="white")

        def set_b_img(self):
            self.InputFilePathGreen = filedialog.askopenfilename(title="Input B Image")
            if (self.InputFilePathGreen != ""):
                self.InputFilePathGreen1 = self.InputFilePathGreen.split("/")[-1]
                self.mainDirectoryPathInGreen.configure(text=self.InputFilePathGreen1,text_color="white")



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