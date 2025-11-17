import os
import threading
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image
import numpy as np
import customtkinter as ctk
from datetime import datetime

import webbrowser
import sys
import json
from pathlib import Path

from config import *
import utils as u 

import class_Logger as L

# ============================================================================
# SEPARATE CHANNELS CLASS
# ============================================================================

class SeparateTab:
    def __init__(self, master):
        self.img = u.load_preview_image()
        self.input_file = ""
        self.output_red = ""
        self.output_green = ""
        self.output_blue = ""
        self.output_alpha = ""

        left_tab_frame, frame_top, frame_scroll, frame_bottom = u.create_tab_frame(master)

        # Input frame
        frame08 = ctk.CTkFrame(frame_top, width=400, height=30)
        frame08.pack(padx=2, pady=1)
        frame08.propagate(False)

        # Channel frames
        frame1 = ctk.CTkFrame(frame_scroll)
        frame1.pack()
        frame01 = ctk.CTkFrame(frame1, width=CELL_W2, height=CELL_H)
        frame01.pack(padx=2, pady=2, side=LEFT)
        frame01.propagate(False)

        frame2 = ctk.CTkFrame(frame_scroll)
        frame2.pack()
        frame02 = ctk.CTkFrame(frame2, width=CELL_W2, height=CELL_H)
        frame02.pack(padx=2, pady=2, side=LEFT)
        frame02.propagate(False)

        frame3 = ctk.CTkFrame(frame_scroll)
        frame3.pack()
        frame03 = ctk.CTkFrame(frame3, width=CELL_W2, height=CELL_H)
        frame03.pack(padx=2, pady=2, side=LEFT)
        frame03.propagate(False)

        frame4 = ctk.CTkFrame(frame_scroll)
        frame4.pack()
        frame04 = ctk.CTkFrame(frame4, width=CELL_W2, height=CELL_H)
        frame04.pack(padx=2, pady=2, side=LEFT)
        frame04.propagate(False)

        # Preview (4 channels)
        self.create_preview_4(left_tab_frame)

        # Input file selector
        label_in = ctk.CTkLabel(frame08, text="Input:", width=32, font=S_FONT)
        label_in.pack(pady=2, padx=6, side=LEFT)

        button_in = ctk.CTkButton(frame08, text="Set Input", width=100,
                                 command=self.set_input_file, font=S_FONT)
        button_in.pack(pady=2, padx=2, side=RIGHT)

        self.label_input = ctk.CTkLabel(frame08, text="(Not set)",  text_color=NOTSET_COLOR, font=S_FONT)
        self.label_input.pack(pady=2, padx=6, side=LEFT)



        # Generate button
        generate_button = ctk.CTkButton(frame_bottom, text="Separate", width=400, height=40,
                                       command=self.generate, font=B_FONT)
        generate_button.pack(pady=2, padx=2, side=RIGHT)

        # Red channel
        frame011 = ctk.CTkFrame(frame01, width=400, height=40)
        frame011.pack(padx=2, pady=1, fill=X, expand=TRUE)
        frame012 = ctk.CTkFrame(frame01, width=400, height=40)
        frame012.pack(padx=2, pady=1, fill=X, expand=TRUE)

        label_red = ctk.CTkLabel(frame011, text="Red Channel", font=M_FONT)
        label_red.pack(pady=6, padx=12, side=LEFT)

        button_red = ctk.CTkButton(frame011, text="Set Output", width=100,
                                  command=self.set_red_channel, font=S_FONT)
        button_red.pack(pady=2, padx=2, side=RIGHT)

        label_out_red = ctk.CTkLabel(frame012, text="Output:", font=S_FONT)
        label_out_red.pack(pady=2, padx=6, side=LEFT)

        self.label_red = ctk.CTkLabel(frame012, text="(Not set)",  text_color=NOTSET_COLOR, font=S_FONT)
        self.label_red.pack(pady=2, padx=6, side=LEFT)

        # Green channel
        frame021 = ctk.CTkFrame(frame02, width=400, height=40)
        frame021.pack(padx=2, pady=1, fill=X, expand=TRUE)
        frame022 = ctk.CTkFrame(frame02, width=400, height=40)
        frame022.pack(padx=2, pady=1, fill=X, expand=TRUE)

        label_green = ctk.CTkLabel(frame021, text="Green Channel", font=M_FONT)
        label_green.pack(pady=6, padx=12, side=LEFT)

        button_green = ctk.CTkButton(frame021, text="Set Output", width=100,
                                    command=self.set_green_channel, font=S_FONT)
        button_green.pack(pady=2, padx=2, side=RIGHT)

        label_out_green = ctk.CTkLabel(frame022, text="Output:", font=S_FONT)
        label_out_green.pack(pady=2, padx=6, side=LEFT)

        self.label_green = ctk.CTkLabel(frame022, text="(Not set)",  text_color=NOTSET_COLOR, font=S_FONT)
        self.label_green.pack(pady=2, padx=6, side=LEFT)

        # Blue channel
        frame031 = ctk.CTkFrame(frame03, width=400, height=40)
        frame031.pack(padx=2, pady=1, fill=X, expand=TRUE)
        frame032 = ctk.CTkFrame(frame03, width=400, height=40)
        frame032.pack(padx=2, pady=1, fill=X, expand=TRUE)

        label_blue = ctk.CTkLabel(frame031, text="Blue Channel", font=M_FONT)
        label_blue.pack(pady=6, padx=12, side=LEFT)

        button_blue = ctk.CTkButton(frame031, text="Set Output", width=100,
                                   command=self.set_blue_channel, font=S_FONT)
        button_blue.pack(pady=2, padx=2, side=RIGHT)

        label_out_blue = ctk.CTkLabel(frame032, text="Output:", font=S_FONT)
        label_out_blue.pack(pady=2, padx=6, side=LEFT)

        self.label_blue = ctk.CTkLabel(frame032, text="(Not set)",  text_color=NOTSET_COLOR, font=S_FONT)
        self.label_blue.pack(pady=2, padx=6, side=LEFT)

        # Alpha channel
        frame041 = ctk.CTkFrame(frame04, width=400, height=40)
        frame041.pack(padx=2, pady=1, fill=X, expand=TRUE)
        frame042 = ctk.CTkFrame(frame04, width=400, height=40)
        frame042.pack(padx=2, pady=1, fill=X, expand=TRUE)

        label_alpha = ctk.CTkLabel(frame041, text="Alpha Channel", font=M_FONT)
        label_alpha.pack(pady=6, padx=16, side=LEFT)

        button_alpha = ctk.CTkButton(frame041, text="Set Output", width=100,
                                    command=self.set_alpha_channel, font=S_FONT)
        button_alpha.pack(pady=2, padx=2, side=RIGHT)

        label_out_alpha = ctk.CTkLabel(frame042, text="Output:", font=S_FONT)
        label_out_alpha.pack(pady=2, padx=6, side=LEFT)

        self.label_alpha = ctk.CTkLabel(frame042, text="(Not set)",  text_color=NOTSET_COLOR, font=S_FONT)
        self.label_alpha.pack(pady=2, padx=6, side=LEFT)

    def create_preview_4(self, master):
        # Load preview image or create gray channels
        try:
            if os.path.exists(PREVIEW_PATH):
                preview_img = Image.open(PREVIEW_PATH).convert("RGBA")
                channels = list(preview_img.split())
            else:
                channels = [Image.new("L", (238, 238), 128) for _ in range(4)]
        except:
            channels = [Image.new("L", (238, 238), 128) for _ in range(4)]
        
        size = (238, 238)

        frame = ctk.CTkFrame(master)
        frame.pack(pady=PREVIEW_BORDER_WIDTH, padx=PREVIEW_BORDER_WIDTH)

        self.preview_labels = []

        # Row 1
        row1 = ctk.CTkFrame(frame)
        row1.pack(side="top")

        for i in range(2):
            img = ctk.CTkImage(light_image=channels[i], size=size)
            lbl = ctk.CTkLabel(row1, image=img, text='')
            lbl.image = img
            lbl.pack(side="left", padx=1, pady=1)
            self.preview_labels.append(lbl)

        # Row 2
        row2 = ctk.CTkFrame(frame)
        row2.pack(side="top")

        for i in range(2, 4):
            img = ctk.CTkImage(light_image=channels[i], size=size)
            lbl = ctk.CTkLabel(row2, image=img, text='')
            lbl.image = img
            lbl.pack(side="left", padx=1, pady=1)
            self.preview_labels.append(lbl)

    def update_preview(self):
        if hasattr(self, 'img') and self.img:
            channels = list(self.img.split())
            size = (238, 238)

            # Fill missing channels with black
            while len(channels) < 4:
                channels.append(Image.new("L", self.img.size, 0))

            for i, label in enumerate(self.preview_labels):
                img = ctk.CTkImage(light_image=channels[i], size=size)
                label.configure(image=img)
                label.image = img

    def set_input_file(self):
        file = filedialog.askopenfilename(title="Select Input File")
        if file:
            self.input_file = file
            filename = os.path.basename(file)
            self.label_input.configure(text=filename, text_color="white")
            try:
                self.img = Image.open(file).convert("RGBA")
                self.update_preview()
                L.Logger().log(f"Input file loaded: {filename}", "INFO")
            except Exception as e:
                L.Logger().log(f"Failed to open: {str(e)}", "ERROR")

    def set_red_channel(self):
        file = filedialog.asksaveasfilename(
            title="Output Red Channel",
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("TIFF files", "*.tiff"), ("All files", "*.*")]
        )
        if file:
            self.output_red = file
            self.label_red.configure(text=os.path.basename(file), text_color="white")

    def set_green_channel(self):
        file = filedialog.asksaveasfilename(
            title="Output Green Channel",
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("TIFF files", "*.tiff"), ("All files", "*.*")]
        )
        if file:
            self.output_green = file
            self.label_green.configure(text=os.path.basename(file), text_color="white")

    def set_blue_channel(self):
        file = filedialog.asksaveasfilename(
            title="Output Blue Channel",
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("TIFF files", "*.tiff"), ("All files", "*.*")]
        )
        if file:
            self.output_blue = file
            self.label_blue.configure(text=os.path.basename(file), text_color="white")

    def set_alpha_channel(self):
        file = filedialog.asksaveasfilename(
            title="Output Alpha Channel",
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("TIFF files", "*.tiff"), ("All files", "*.*")]
        )
        if file:
            self.output_alpha = file
            self.label_alpha.configure(text=os.path.basename(file), text_color="white")
    
    def generate(self):
        def generate_thr():
            try:
                if not self.input_file or not os.path.exists(self.input_file):
                    L.Logger().log("Please select an input file", "WARNING")
                    return

                img_input = Image.open(self.input_file)
                if img_input.mode != 'RGBA':
                    img_input = img_input.convert('RGBA')

                r, g, b, a = img_input.split()

                saved_count = 0
                if self.output_red:
                    r.save(self.output_red)
                    saved_count += 1

                if self.output_green:
                    g.save(self.output_green)
                    saved_count += 1

                if self.output_blue:
                    b.save(self.output_blue)
                    saved_count += 1

                if self.output_alpha:
                    a.save(self.output_alpha)
                    saved_count += 1

                if saved_count > 0:
                    L.Logger().log(f"Saved {saved_count} channel(s) successfully!", "SUCCESS")
                else:
                    L.Logger().log("No output files selected", "WARNING")

            except Exception as e:
                L.Logger().log(f"Failed to separate: {str(e)}", "ERROR")

        threading.Thread(target=generate_thr, daemon=True).start()
