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
# COMBINE CHANNELS CLASS
# ============================================================================

class CombineTab:
    def __init__(self, master):
        self.img = u.load_preview_image()
        self.input_red = ""
        self.input_green = ""
        self.input_blue = ""
        self.input_alpha = ""
        self.output_file = ""
        
        # Channel source selections
        self.red_source = ctk.StringVar(value="R")
        self.green_source = ctk.StringVar(value="G")
        self.blue_source = ctk.StringVar(value="B")
        self.alpha_source = ctk.StringVar(value="A")

        left_tab_frame, frame_top, frame_scroll, frame_bottom = u.create_tab_frame(master)

        # Preview (4 channels) - FIRST
        self.create_preview_4(left_tab_frame)

        # Channel frames
        frame1 = ctk.CTkFrame(frame_scroll)
        frame1.pack()
        frame01 = ctk.CTkFrame(frame1, width=CELL_W2, height=CELL_H*1.25)
        frame01.pack(padx=2, pady=2, side=LEFT)
        frame01.propagate(False)

        frame2 = ctk.CTkFrame(frame_scroll)
        frame2.pack()
        frame02 = ctk.CTkFrame(frame2, width=CELL_W2, height=CELL_H*1.25)
        frame02.pack(padx=2, pady=2, side=LEFT)
        frame02.propagate(False)

        frame3 = ctk.CTkFrame(frame_scroll)
        frame3.pack()
        frame03 = ctk.CTkFrame(frame3, width=CELL_W2, height=CELL_H*1.25)
        frame03.pack(padx=2, pady=2, side=LEFT)
        frame03.propagate(False)

        frame4 = ctk.CTkFrame(frame_scroll)
        frame4.pack()
        frame04 = ctk.CTkFrame(frame4, width=CELL_W2, height=CELL_H*1.25)
        frame04.pack(padx=2, pady=2, side=LEFT)
        frame04.propagate(False)

        # Output frame
        frame08 = ctk.CTkFrame(frame_top, width=400, height=30)
        frame08.pack(padx=2, pady=1)
        frame08.propagate(False)

        # Output file selector
        label_out = ctk.CTkLabel(frame08, text="Output:", width=32, font=S_FONT)
        label_out.pack(pady=2, padx=6, side=LEFT)

        button_out = ctk.CTkButton(frame08, text="Set Output", width=100,
                                  command=self.set_output_file, font=S_FONT)
        button_out.pack(pady=2, padx=2, side=RIGHT)

        self.label_output = ctk.CTkLabel(frame08, text="(Not set)", text_color=NOTSET_COLOR, font=S_FONT)
        self.label_output.pack(pady=2, padx=6, side=LEFT)

        # Generate button
        generate_button = ctk.CTkButton(frame_bottom, text="Combine", width=400, height=40,
                                       command=self.generate, font=B_FONT)
        generate_button.pack(pady=2, padx=2, side=RIGHT)

        # Red channel
        frame011 = ctk.CTkFrame(frame01, width=400, height=40)
        frame011.pack(padx=2, pady=1, fill=X, expand=TRUE)
        frame012 = ctk.CTkFrame(frame01, width=400, height=40)
        frame012.pack(padx=2, pady=1, fill=X, expand=TRUE)
        frame013 = ctk.CTkFrame(frame01, width=400, height=40)
        frame013.pack(padx=2, pady=1, fill=X, expand=TRUE)

        label_red = ctk.CTkLabel(frame011, text="Red Channel", font=M_FONT)
        label_red.pack(pady=6, padx=12, side=LEFT)

        button_red = ctk.CTkButton(frame011, text="Set Input", width=100,
                                  command=self.set_red_channel, font=S_FONT)
        button_red.pack(pady=2, padx=2, side=RIGHT)

        label_in_red = ctk.CTkLabel(frame013, text="Input:", font=S_FONT)
        label_in_red.pack(pady=2, padx=6, side=LEFT)

        self.label_red = ctk.CTkLabel(frame013, text="(Not set)", text_color=NOTSET_COLOR, font=S_FONT)
        self.label_red.pack(pady=2, padx=6, side=LEFT)

        self.red_r = ctk.CTkCheckBox(frame012, text="R", width=30, font=M_FONT, checkbox_width=16, checkbox_height=16,
                                     command=lambda: self.update_channel_source(self.red_source, "R"))
        self.red_r.pack(pady=2, padx=(80,10), side=LEFT)
        
        self.red_g = ctk.CTkCheckBox(frame012, text="G", width=30, font=M_FONT, checkbox_width=16, checkbox_height=16,
                                     command=lambda: self.update_channel_source(self.red_source, "G"))
        self.red_g.pack(pady=2, padx=10, side=LEFT)
        
        self.red_b = ctk.CTkCheckBox(frame012, text="B", width=30, font=M_FONT, checkbox_width=16, checkbox_height=16,
                                     command=lambda: self.update_channel_source(self.red_source, "B"))
        self.red_b.pack(pady=2, padx=10, side=LEFT)
        
        self.red_a = ctk.CTkCheckBox(frame012, text="A", width=30, font=M_FONT, checkbox_width=16, checkbox_height=16,
                                     command=lambda: self.update_channel_source(self.red_source, "A"))
        self.red_a.pack(pady=2, padx=10, side=LEFT)

        self.red_checkboxes = [self.red_r, self.red_g, self.red_b, self.red_a]
        self.red_r.select()

        # Green channel
        frame021 = ctk.CTkFrame(frame02, width=400, height=40)
        frame021.pack(padx=2, pady=1, fill=X, expand=TRUE)
        frame022 = ctk.CTkFrame(frame02, width=400, height=40)
        frame022.pack(padx=2, pady=1, fill=X, expand=TRUE)
        frame023 = ctk.CTkFrame(frame02, width=400, height=40)
        frame023.pack(padx=2, pady=1, fill=X, expand=TRUE)

        label_green = ctk.CTkLabel(frame021, text="Green Channel", font=M_FONT)
        label_green.pack(pady=6, padx=12, side=LEFT)

        button_green = ctk.CTkButton(frame021, text="Set Input", width=100,
                                    command=self.set_green_channel, font=S_FONT)
        button_green.pack(pady=2, padx=2, side=RIGHT)

        label_in_green = ctk.CTkLabel(frame023, text="Input:", font=S_FONT)
        label_in_green.pack(pady=2, padx=6, side=LEFT)

        self.label_green = ctk.CTkLabel(frame023, text="(Not set)", text_color=NOTSET_COLOR, font=S_FONT)
        self.label_green.pack(pady=2, padx=6, side=LEFT)

        self.green_r = ctk.CTkCheckBox(frame022, text="R", width=30, font=M_FONT, checkbox_width=16, checkbox_height=16,
                                       command=lambda: self.update_channel_source(self.green_source, "R"))
        self.green_r.pack(pady=2, padx=(80,10), side=LEFT)
        
        self.green_g = ctk.CTkCheckBox(frame022, text="G", width=30, font=M_FONT, checkbox_width=16, checkbox_height=16,
                                       command=lambda: self.update_channel_source(self.green_source, "G"))
        self.green_g.pack(pady=2, padx=10, side=LEFT)
        
        self.green_b = ctk.CTkCheckBox(frame022, text="B", width=30, font=M_FONT, checkbox_width=16, checkbox_height=16,
                                       command=lambda: self.update_channel_source(self.green_source, "B"))
        self.green_b.pack(pady=2, padx=10, side=LEFT)
        
        self.green_a = ctk.CTkCheckBox(frame022, text="A", width=30, font=M_FONT, checkbox_width=16, checkbox_height=16,
                                       command=lambda: self.update_channel_source(self.green_source, "A"))
        self.green_a.pack(pady=2, padx=10, side=LEFT)

        self.green_checkboxes = [self.green_r, self.green_g, self.green_b, self.green_a]
        self.green_g.select()

        # Blue channel
        frame031 = ctk.CTkFrame(frame03, width=400, height=40)
        frame031.pack(padx=2, pady=1, fill=X, expand=TRUE)
        frame032 = ctk.CTkFrame(frame03, width=400, height=40)
        frame032.pack(padx=2, pady=1, fill=X, expand=TRUE)
        frame033 = ctk.CTkFrame(frame03, width=400, height=40)
        frame033.pack(padx=2, pady=1, fill=X, expand=TRUE)

        label_blue = ctk.CTkLabel(frame031, text="Blue Channel", font=M_FONT)
        label_blue.pack(pady=6, padx=12, side=LEFT)

        button_blue = ctk.CTkButton(frame031, text="Set Input", width=100,
                                   command=self.set_blue_channel, font=S_FONT)
        button_blue.pack(pady=2, padx=2, side=RIGHT)

        label_in_blue = ctk.CTkLabel(frame033, text="Input:", font=S_FONT)
        label_in_blue.pack(pady=2, padx=6, side=LEFT)

        self.label_blue = ctk.CTkLabel(frame033, text="(Not set)", text_color=NOTSET_COLOR, font=S_FONT)
        self.label_blue.pack(pady=2, padx=6, side=LEFT)

        self.blue_r = ctk.CTkCheckBox(frame032, text="R", width=30, font=M_FONT, checkbox_width=16, checkbox_height=16,
                                      command=lambda: self.update_channel_source(self.blue_source, "R"))
        self.blue_r.pack(pady=2, padx=(80,10), side=LEFT)
        
        self.blue_g = ctk.CTkCheckBox(frame032, text="G", width=30, font=M_FONT, checkbox_width=16, checkbox_height=16,
                                      command=lambda: self.update_channel_source(self.blue_source, "G"))
        self.blue_g.pack(pady=2, padx=10, side=LEFT)
        
        self.blue_b = ctk.CTkCheckBox(frame032, text="B", width=30, font=M_FONT, checkbox_width=16, checkbox_height=16,
                                      command=lambda: self.update_channel_source(self.blue_source, "B"))
        self.blue_b.pack(pady=2, padx=10, side=LEFT)
        
        self.blue_a = ctk.CTkCheckBox(frame032, text="A", width=30, font=M_FONT, checkbox_width=16, checkbox_height=16,
                                      command=lambda: self.update_channel_source(self.blue_source, "A"))
        self.blue_a.pack(pady=2, padx=10, side=LEFT)

        self.blue_checkboxes = [self.blue_r, self.blue_g, self.blue_b, self.blue_a]
        self.blue_b.select()

        # Alpha channel
        frame041 = ctk.CTkFrame(frame04, width=400, height=40)
        frame041.pack(padx=2, pady=1, fill=X, expand=TRUE)
        frame042 = ctk.CTkFrame(frame04, width=400, height=40)
        frame042.pack(padx=2, pady=1, fill=X, expand=TRUE)
        frame043 = ctk.CTkFrame(frame04, width=400, height=40)
        frame043.pack(padx=2, pady=1, fill=X, expand=TRUE)

        label_alpha = ctk.CTkLabel(frame041, text="Alpha Channel", font=M_FONT)
        label_alpha.pack(pady=6, padx=16, side=LEFT)

        button_alpha = ctk.CTkButton(frame041, text="Set Input", width=100,
                                    command=self.set_alpha_channel, font=S_FONT)
        button_alpha.pack(pady=2, padx=2, side=RIGHT)

        label_in_alpha = ctk.CTkLabel(frame043, text="Input:", font=S_FONT)
        label_in_alpha.pack(pady=2, padx=6, side=LEFT)

        self.label_alpha = ctk.CTkLabel(frame043, text="(Not set)", text_color=NOTSET_COLOR, font=S_FONT)
        self.label_alpha.pack(pady=2, padx=6, side=LEFT)

        self.alpha_r = ctk.CTkCheckBox(frame042, text="R", width=30, font=M_FONT, checkbox_width=16, checkbox_height=16,
                                       command=lambda: self.update_channel_source(self.alpha_source, "R"))
        self.alpha_r.pack(pady=2, padx=(80,10), side=LEFT)
        
        self.alpha_g = ctk.CTkCheckBox(frame042, text="G", width=30, font=M_FONT, checkbox_width=16, checkbox_height=16,
                                       command=lambda: self.update_channel_source(self.alpha_source, "G"))
        self.alpha_g.pack(pady=2, padx=10, side=LEFT)
        
        self.alpha_b = ctk.CTkCheckBox(frame042, text="B", width=30, font=M_FONT, checkbox_width=16, checkbox_height=16,
                                       command=lambda: self.update_channel_source(self.alpha_source, "B"))
        self.alpha_b.pack(pady=2, padx=10, side=LEFT)
        
        self.alpha_a = ctk.CTkCheckBox(frame042, text="A", width=30, font=M_FONT, checkbox_width=16, checkbox_height=16,
                                       command=lambda: self.update_channel_source(self.alpha_source, "A"))
        self.alpha_a.pack(pady=2, padx=10, side=LEFT)

        self.alpha_checkboxes = [self.alpha_r, self.alpha_g, self.alpha_b, self.alpha_a]
        self.alpha_a.select()

    def update_channel_source(self, source_var, channel):
        """Update channel source and ensure only one checkbox is selected"""
        source_var.set(channel)
        
        # Determine which set of checkboxes to update
        if source_var == self.red_source:
            checkboxes = self.red_checkboxes
        elif source_var == self.green_source:
            checkboxes = self.green_checkboxes
        elif source_var == self.blue_source:
            checkboxes = self.blue_checkboxes
        else:
            checkboxes = self.alpha_checkboxes
        
        # Deselect all checkboxes
        for cb in checkboxes:
            cb.deselect()
        
        # Select the clicked one
        channel_map = {"R": 0, "G": 1, "B": 2, "A": 3}
        if channel in channel_map:
            checkboxes[channel_map[channel]].select()
        
        self.update_preview()

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

    def get_channel_from_image(self, img_path, channel_letter):
        """Extract specific channel from image based on letter (R, G, B, A)"""
        try:
            img = Image.open(img_path).convert("RGBA")
            r, g, b, a = img.split()
            
            channel_map = {
                "R": r,
                "G": g,
                "B": b,
                "A": a
            }
            
            return channel_map.get(channel_letter, r)
        except:
            return None

    def update_preview(self):
        channels = []
        
        # Map of input files and their source channels
        channel_configs = [
            (self.input_red, self.red_source.get()),
            (self.input_green, self.green_source.get()),
            (self.input_blue, self.blue_source.get()),
            (self.input_alpha, self.alpha_source.get())
        ]
        
        # Load each channel from specified source
        for i, (input_path, source_channel) in enumerate(channel_configs):
            if input_path and os.path.exists(input_path):
                channel = self.get_channel_from_image(input_path, source_channel)
                if channel:
                    channels.append(channel)
                else:
                    # Default fill: white for alpha, black for RGB
                    fill_value = 255 if i == 3 else 0
                    channels.append(Image.new("L", (238, 238), fill_value))
            else:
                # Default fill: white for alpha, black for RGB
                fill_value = 255 if i == 3 else 0
                channels.append(Image.new("L", (238, 238), fill_value))
        
        size = (238, 238)
        
        for i, label in enumerate(self.preview_labels):
            img = ctk.CTkImage(light_image=channels[i], size=size)
            label.configure(image=img)
            label.image = img

    def set_red_channel(self):
        file = filedialog.askopenfilename(
            title="Select Red Channel Input",
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.tiff *.bmp"), ("All files", "*.*")]
        )
        if file:
            self.input_red = file
            self.label_red.configure(text=os.path.basename(file), text_color="white")
            self.update_preview()
            L.Logger().log(f"Red channel input loaded: {os.path.basename(file)}", "INFO")

    def set_green_channel(self):
        file = filedialog.askopenfilename(
            title="Select Green Channel Input",
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.tiff *.bmp"), ("All files", "*.*")]
        )
        if file:
            self.input_green = file
            self.label_green.configure(text=os.path.basename(file), text_color="white")
            self.update_preview()
            L.Logger().log(f"Green channel input loaded: {os.path.basename(file)}", "INFO")

    def set_blue_channel(self):
        file = filedialog.askopenfilename(
            title="Select Blue Channel Input",
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.tiff *.bmp"), ("All files", "*.*")]
        )
        if file:
            self.input_blue = file
            self.label_blue.configure(text=os.path.basename(file), text_color="white")
            self.update_preview()
            L.Logger().log(f"Blue channel input loaded: {os.path.basename(file)}", "INFO")

    def set_alpha_channel(self):
        file = filedialog.askopenfilename(
            title="Select Alpha Channel Input",
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.tiff *.bmp"), ("All files", "*.*")]
        )
        if file:
            self.input_alpha = file
            self.label_alpha.configure(text=os.path.basename(file), text_color="white")
            self.update_preview()
            L.Logger().log(f"Alpha channel input loaded: {os.path.basename(file)}", "INFO")

    def set_output_file(self):
        file = filedialog.asksaveasfilename(
            title="Output Combined Image",
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("TIFF files", "*.tiff"), ("All files", "*.*")]
        )
        if file:
            self.output_file = file
            self.label_output.configure(text=os.path.basename(file), text_color="white")
    
    def generate(self):
        def generate_thr():
            try:
                if not self.output_file:
                    L.Logger().log("Please select an output file", "WARNING")
                    return

                # Check if at least one channel is set
                channels_set = [self.input_red, self.input_green, self.input_blue, self.input_alpha]
                if not any(channels_set):
                    L.Logger().log("Please select at least one input channel", "WARNING")
                    return

                # Load first available channel to get dimensions
                reference_img = None
                for channel_path in channels_set:
                    if channel_path and os.path.exists(channel_path):
                        reference_img = Image.open(channel_path)
                        break

                if not reference_img:
                    L.Logger().log("No valid input channels found", "ERROR")
                    return

                size = reference_img.size
                channels = []

                # Map of input files and their source channels
                channel_configs = [
                    (self.input_red, self.red_source.get()),
                    (self.input_green, self.green_source.get()),
                    (self.input_blue, self.blue_source.get()),
                    (self.input_alpha, self.alpha_source.get())
                ]

                # Load or create each channel from specified source
                for i, (input_path, source_channel) in enumerate(channel_configs):
                    if input_path and os.path.exists(input_path):
                        channel = self.get_channel_from_image(input_path, source_channel)
                        if channel:
                            if channel.size != size:
                                channel = channel.resize(size, Image.LANCZOS)
                            channels.append(channel)
                        else:
                            # Default fill: white for alpha, black for RGB
                            fill_value = 255 if i == 3 else 0
                            channels.append(Image.new("L", size, fill_value))
                    else:
                        # Default fill: white for alpha, black for RGB
                        fill_value = 255 if i == 3 else 0
                        channels.append(Image.new("L", size, fill_value))

                # Merge channels into RGBA image
                combined_img = Image.merge("RGBA", channels)
                combined_img.save(self.output_file)

                L.Logger().log(f"Combined image saved successfully: {os.path.basename(self.output_file)}", "SUCCESS")

            except Exception as e:
                L.Logger().log(f"Failed to combine channels: {str(e)}", "ERROR")

        threading.Thread(target=generate_thr, daemon=True).start()
