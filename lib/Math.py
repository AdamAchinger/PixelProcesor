import os
import customtkinter as ctk  # Import customtkinter instead of tkinter
from tkinter import filedialog
from PIL import Image

### Version
toolVersion = 2.4
###

def Math():

    root = Tk()

    bgColor = "#353535"
    fgColor = "#C0C0C0"
    hlColor = "#777777"
    fontSizeSmall = 13

    root.configure(fg_color=bgColor)  # Set background color
    root.title("Math" + " v" + str(toolVersion))
    root.iconbitmap('S:\GitHub\PixelProcesor\img\AA_icon.ico')
    root.resizable(False, False)

    #####
    # application dimensions
    appWidth = 420
    appHeight = 425
    # get windows screen width and height
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()
    # center position 
    appXpos = int((screenWidth / 2) - (appWidth / 2))
    appYpos = int((screenHeight / 2) - (appHeight / 2))
    # create app window 
    root.geometry(f'{appWidth}x{appHeight}+{appXpos}+{appYpos}')
    #####

    def Generate():
        Multiply3 = inputMultiply.get()
        Power3 = inputPower.get()
        Add3 = inputAdd.get()
        Subtract3 = inputSubtract.get()
        Min3 = inputMin.get()
        Max3 = inputMax.get()
        InputFile = InputFilePath
        Output = OutputFilePath

        img = Image.open(InputFile)
        Width, Height = img.size

        for w in range(Width):
            for h in range(Height):
                ### Multiply ###
                if (Multiply3 != "1,1,1"):
                    R1, G1, B1 = img.getpixel((w, h))
                    R = int(R1 * float(Multiply3.split(",")[0]))
                    G = int(G1 * float(Multiply3.split(",")[1]))
                    B = int(B1 * float(Multiply3.split(",")[2]))
                    img.putpixel((w, h), (R, G, B))
                ### Power ###
                if (Power3 != "1,1,1"):
                    R1, G1, B1 = img.getpixel((w, h))
                    R = int(pow(R1, float(Power3.split(",")[0])))
                    G = int(pow(G1, float(Power3.split(",")[1])))
                    B = int(pow(B1, float(Power3.split(",")[2])))
                    img.putpixel((w, h), (R, G, B))

                ### Add ###
                if (Add3 != "0,0,0"):
                    R1, G1, B1 = img.getpixel((w, h))
                    R = int(R1 + (float(Add3.split(",")[0]) * 255))
                    G = int(G1 + (float(Add3.split(",")[1]) * 255))
                    B = int(B1 + (float(Add3.split(",")[2]) * 255))

                    img.putpixel((w, h), (R, G, B))

                ### Subtract ###
                if (Subtract3 != "0,0,0"):
                    R1, G1, B1 = img.getpixel((w, h))
                    R = int(R1 - (float(Subtract3.split(",")[0]) * 255))
                    G = int(G1 - (float(Subtract3.split(",")[1]) * 255))
                    B = int(B1 - (float(Subtract3.split(",")[2]) * 255))
                    img.putpixel((w, h), (R, G, B))

                ### Clamp ###
                rMin = float(Min3.split(",")[0]) * 255
                gMin = float(Min3.split(",")[1]) * 255
                bMin = float(Min3.split(",")[2]) * 255

                rMax = float(Max3.split(",")[0]) * 255
                gMax = float(Max3.split(",")[1]) * 255
                bMax = float(Max3.split(",")[2]) * 255

                R1, G1, B1 = img.getpixel((w, h))

                R = int(min(max(R1, rMin), rMax))
                G = int(min(max(G1, gMin), gMax))
                B = int(min(max(B1, bMin), bMax))

                img.putpixel((w, h), (R, G, B))

        img.save(Output)

    #### Math #### 
    frame1 = ctk.CTkFrame(root, width=100, fg_color=bgColor)
    frame1.grid(row=0, column=0, pady=10, padx=60, sticky="s")

    label_1 = ctk.CTkLabel(frame1, text="Math", font=("Roboto", 32), text_color=fgColor)
    label_1.grid(row=0, column=0, pady=3, padx=60, sticky="s")

    #### Multiply #### 
    frame21 = ctk.CTkFrame(root, width=25, fg_color=bgColor, border_color=hlColor, border_width=1)
    frame21.grid(row=3, column=0, pady=6, padx=12, sticky="w")

    labelMultiply = ctk.CTkLabel(frame21, text="MULTIPLY", font=("Roboto", fontSizeSmall), text_color=fgColor)
    labelMultiply.grid(row=1, column=0, pady=6, padx=16)
    inputMultiply = ctk.CTkEntry(frame21, width=10, font=("Roboto", fontSizeSmall), fg_color=bgColor, text_color=fgColor)
    inputMultiply.grid(row=2, column=0, pady=2, padx=16)
    inputMultiply.insert(0, "1,1,1")

    #### Power #### 
    frame22 = ctk.CTkFrame(root, width=25, fg_color=bgColor, border_color=hlColor, border_width=1)
    frame22.grid(row=4, column=0, pady=6, padx=12, sticky="w")

    labelPower = ctk.CTkLabel(frame22, text="POWER", font=("Roboto", fontSizeSmall), text_color=fgColor)
    labelPower.grid(row=1, column=0, pady=6, padx=16)
    inputPower = ctk.CTkEntry(frame22, width=10, font=("Roboto", fontSizeSmall), fg_color=bgColor, text_color=fgColor)
    inputPower.grid(row=2, column=0, pady=2, padx=16)
    inputPower.insert(0, "1,1,1")

    #### Add #### 
    frame24 = ctk.CTkFrame(root, width=25, fg_color=bgColor, border_color=hlColor, border_width=1)
    frame24.grid(row=3, column=0, pady=6, padx=147, sticky="w")

    labelAdd = ctk.CTkLabel(frame24, text="ADD", font=("Roboto", fontSizeSmall), text_color=fgColor)
    labelAdd.grid(row=1, column=0, pady=6, padx=16)
    inputAdd = ctk.CTkEntry(frame24, width=10, font=("Roboto", fontSizeSmall), fg_color=bgColor, text_color=fgColor)
    inputAdd.grid(row=2, column=0, pady=2, padx=16)
    inputAdd.insert(0, "0,0,0")

    #### Subtract #### 
    frame25 = ctk.CTkFrame(root, width=25, fg_color=bgColor, border_color=hlColor, border_width=1)
    frame25.grid(row=4, column=0, pady=6, padx=147, sticky="w")

    labelSubtract = ctk.CTkLabel(frame25, text="SUBTRACT", font=("Roboto", fontSizeSmall), text_color=fgColor)
    labelSubtract.grid(row=1, column=0, pady=6, padx=16)
    inputSubtract = ctk.CTkEntry(frame25, width=10, font=("Roboto", fontSizeSmall), fg_color=bgColor, text_color=fgColor)
    inputSubtract.grid(row=2, column=0, pady=2, padx=16)
    inputSubtract.insert(0, "0,0,0")

    #### Max #### 
    frame26 = ctk.CTkFrame(root, width=25, fg_color=bgColor, border_color=hlColor, border_width=1)
    frame26.grid(row=3, column=0, pady=6, padx=12, sticky="e")

    labelMax = ctk.CTkLabel(frame26, text="MAX", font=("Roboto", fontSizeSmall), text_color=fgColor)
    labelMax.grid(row=1, column=0, pady=6, padx=16)
    inputMax = ctk.CTkEntry(frame26, width=10, font=("Roboto", fontSizeSmall), fg_color=bgColor, text_color=fgColor)
    inputMax.grid(row=2, column=0, pady=2, padx=16)
    inputMax.insert(0, "1,1,1")

    #### Min #### 
    frame27 = ctk.CTkFrame(root, width=25, fg_color=bgColor, border_color=hlColor, border_width=1)
    frame27.grid(row=4, column=0, pady=6, padx=12, sticky="e")

    labelMin = ctk.CTkLabel(frame27, text="MIN", font=("Roboto", fontSizeSmall), text_color=fgColor)
    labelMin.grid(row=1, column=0, pady=6, padx=16)
    inputMin = ctk.CTkEntry(frame27, width=10, font=("Roboto", fontSizeSmall), fg_color=bgColor, text_color=fgColor)
    inputMin.grid(row=2, column=0, pady=2, padx=16)
    inputMin.insert(0, "0,0,0")

    #### OUTPUT PATH #### 
    frame5 = ctk.CTkFrame(root, width=400, fg_color=bgColor, border_color=hlColor, border_width=0)
    frame5.grid(row=6, column=0, pady=6, padx=6, sticky="w")

    InputFile = ctk.CTkLabel(frame5, text="Input File:", font=("Roboto", 12), text_color=fgColor)
    InputFile.grid(row=2, column=0, pady=2, padx=6, sticky="w")

    InputStatus = ctk.CTkLabel(frame5, text="Unset", font=("Roboto", 13), text_color="red")
    InputStatus.grid(row=2, column=0, pady=2, padx=100, sticky="w")

    InputFileEntry = ctk.CTkLabel(frame5, text="------------", font=("Roboto", 12), text_color=fgColor)
    InputFileEntry.grid(row=3, column=0, pady=2, padx=6, sticky="w")

    OutputFile = ctk.CTkLabel(frame5, text="Output File:", font=("Roboto", 12), text_color=fgColor)
    OutputFile.grid(row=4, column=0, pady=2, padx=6, sticky="w")

    OutputStatus = ctk.CTkLabel(frame5, text="Unset", font=("Roboto", 13), text_color="red")
    OutputStatus.grid(row=4, column=0, pady=2, padx=100, sticky="w")

    OutputFileEntry = ctk.CTkLabel(frame5, text="------------", font=("Roboto", 12), text_color=fgColor)
    OutputFileEntry.grid(row=5, column=0, pady=2, padx=6, sticky="w")

    def InputPath():
        global InputFilePath
        InputFilePath = filedialog.askopenfilename(title="Input File")
        if (InputFilePath != ""):
            InputStatus.config(text="Ready", text_color="green")
            InputFileEntry.config(text=InputFilePath)

    def OutputPath():
        global OutputFilePath
        OutputFilePath = filedialog.asksaveasfilename(title="Output File")
        if (OutputFilePath != ""):
            OutputStatus.config(text="Ready", text_color="green")
            OutputFileEntry.config(text=OutputFilePath)

    framePanel = ctk.CTkFrame(root, width=400, fg_color=bgColor, border_color=hlColor, border_width=1)
    framePanel.grid(row=5, column=0, pady=6, padx=2, sticky="s")

    button = ctk.CTkButton(framePanel, text="Set Input File ", command=InputPath, font=("Roboto", fontSizeSmall), fg_color=bgColor, text_color=fgColor)
    button.grid(row=0, column=0, sticky="w", pady=2, padx=2)

    button1 = ctk.CTkButton(framePanel, text="Set Output File", command=OutputPath, font=("Roboto", fontSizeSmall), fg_color=bgColor, text_color=fgColor)
    button1.grid(row=0, column=1, sticky="w", pady=2, padx=2)

    #### Generate #### 
    GenerateButton = ctk.CTkButton(framePanel, text="Export", font=("Roboto", fontSizeSmall), fg_color=bgColor, text_color=fgColor, command=Generate)
    GenerateButton.grid(row=0, column=2, sticky="w", pady=2, padx=2)

    root.mainloop()
