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
# BLEND CLASS
# ============================================================================

class BlendTab:
    def __init__(self, master):
        self.img = u.load_preview_image()
        self.input_path_a = None
        self.input_path_b = None
        self.output_path = None

        left_tab_frame, frame_top, frame_scroll, frame_bottom = u.create_tab_frame(master)

        # Frames - rows
        frame1 = ctk.CTkFrame(frame_scroll); frame1.pack()
        frame2 = ctk.CTkFrame(frame_scroll); frame2.pack()
        frame3 = ctk.CTkFrame(frame_scroll); frame3.pack()
        
        # Blend operations frames
        # Row 1: Multiply, Power
        frame01 = ctk.CTkFrame(frame1, width=CELL_W, height=CELL_H); frame01.pack(padx=2, pady=2, side=LEFT); frame01.propagate(False)
        frame02 = ctk.CTkFrame(frame1, width=CELL_W, height=CELL_H); frame02.pack(padx=2, pady=2, side=LEFT); frame02.propagate(False)
        # Row 2: Add, Subtract
        frame03 = ctk.CTkFrame(frame2, width=CELL_W, height=CELL_H); frame03.pack(padx=2, pady=2, side=LEFT); frame03.propagate(False)
        frame04 = ctk.CTkFrame(frame2, width=CELL_W, height=CELL_H); frame04.pack(padx=2, pady=2, side=LEFT); frame04.propagate(False)
        # Row 3: Max, Min
        frame05 = ctk.CTkFrame(frame3, width=CELL_W, height=CELL_H); frame05.pack(padx=2, pady=2, side=LEFT); frame05.propagate(False)
        frame06 = ctk.CTkFrame(frame3, width=CELL_W, height=CELL_H); frame06.pack(padx=2, pady=2, side=LEFT); frame06.propagate(False)
        
       
        # Info frame
        frame9 = ctk.CTkFrame(frame_scroll, width=CELL_W * 2 + 4, height=CELL_H); 
        frame9.pack(padx=2, pady=2)
        frame9.propagate(False) 
        ctk.CTkLabel(
            frame9,
            text="Blend operations combine two images\nMultiply: A × B | Add: A + B | Subtract: A - B\nPower: A ^ B | Min: min(A,B) | Max: max(A,B)\nSelect which channels to use from each image",
            font=S_FONT1
        ).pack(pady=10)

        # Input/Output frames
        frame07 = ctk.CTkFrame(frame_top, width=400, height=70); frame07.pack(padx=2, pady=1); frame07.propagate(False)
        
        frame08 = ctk.CTkFrame(frame_top, width=400, height=70); frame08.pack(padx=2, pady=1); frame08.propagate(False)
        
        frame09 = ctk.CTkFrame(frame_top, width=400, height=30); frame09.pack(padx=2, pady=1); frame09.propagate(False)
        

        # Preview
        self.create_preview(left_tab_frame)

        # Input A / Input B / Output file
        self.create_input_file_a(frame07)
        self.create_input_file_b(frame08)
        self.create_output_file(frame09)
        


        # Buttons
        self.export_button = ctk.CTkButton(frame_bottom, text="Export", width=198, height=40,
                                         state=DISABLED, command=self.export, font=B_FONT)
        self.export_button.pack(pady=2, padx=2, side=RIGHT)

        generate_button = ctk.CTkButton(frame_bottom, text="Generate", width=198, height=40,
                                         command=self.generate, font=B_FONT)
        generate_button.pack(pady=2, padx=2, side=RIGHT)

        # Blend operations
        self.create_blend_inputs(frame01, frame02, frame03, frame04, frame05, frame06)

    # ------------------ UI CREATION ------------------

    def create_preview(self, master):
        preview_image = ctk.CTkImage(light_image=self.img, size=(480, 480))
        self.preview_label = ctk.CTkLabel(master, image=preview_image, text='')
        self.preview_label.pack(pady=PREVIEW_BORDER_WIDTH, padx=PREVIEW_BORDER_WIDTH)

    def update_preview(self):
        img_preview = ctk.CTkImage(light_image=self.img, size=(480, 480))
        self.preview_label.configure(image=img_preview)
        self.preview_label.image = img_preview

    def create_input_file_a(self, master):

        # =======================
        # FRAME 1 – Label, Status, Button
        # =======================
        frame_top = ctk.CTkFrame(master)
        frame_top.pack(fill="x", padx=4, pady=(2, 0))
        frame_bottom = ctk.CTkFrame(master)
        frame_bottom.pack(fill="x", padx=4, pady=(0, 4))

        label_in = ctk.CTkLabel(frame_top, text="Input A:", font=S_FONT)
        label_in.pack(pady=2, padx=6, side=LEFT)

        self.label_input_a = ctk.CTkLabel(
            frame_top, text="[Not set]", font=S_FONT, text_color=NOTSET_COLOR
        )
        self.label_input_a.pack(pady=2, padx=6, side=LEFT)

        button = ctk.CTkButton(
            frame_top,
            text="Set Input A",
            width=110,
            height=28,
            command=self.set_input_file_a,
            font=S_FONT
        )
        button.pack(padx=6, pady=2, side=RIGHT)

        # =======================
        # FRAME 2 – Segmented Button
        # =======================

        self.channel_a_var = ctk.StringVar(value="RGBA")

        channel_seg_a = ctk.CTkSegmentedButton(
            frame_bottom,
            variable=self.channel_a_var,
            values=["RGBA", "R", "G", "B", "A"],
            font=S_FONT,
            height=28
        )
        channel_seg_a.pack(pady=4, padx=4, side=LEFT)



    def create_input_file_b(self, master):

        # =======================
        # FRAME 1 – Label, Status, Button
        # =======================
        frame_top = ctk.CTkFrame(master)
        frame_top.pack(fill="x", padx=4, pady=(2, 0))
        frame_bottom = ctk.CTkFrame(master)
        frame_bottom.pack(fill="x", padx=4, pady=(0, 4))

        label_in = ctk.CTkLabel(frame_top, text="Input B:", font=S_FONT)
        label_in.pack(pady=2, padx=6, side=LEFT)

        self.label_input_b = ctk.CTkLabel(
            frame_top, text="[Not set]", font=S_FONT, text_color=NOTSET_COLOR
        )
        self.label_input_b.pack(pady=2, padx=6, side=LEFT)

        button = ctk.CTkButton(
            frame_top,
            text="Set Input B",
            width=110,
            height=28,
            command=self.set_input_file_b,
            font=S_FONT
        )
        button.pack(padx=6, pady=2, side=RIGHT)

        # =======================
        # FRAME 2 – Segmented Button
        # =======================

        self.channel_b_var = ctk.StringVar(value="RGBA")

        channel_seg_b = ctk.CTkSegmentedButton(
            frame_bottom,
            variable=self.channel_b_var,
            values=["RGBA", "R", "G", "B", "A"],
            font=S_FONT,
            height=28
        )
        channel_seg_b.pack(pady=4, padx=4, side=LEFT)

    def create_output_file(self, master):
        label_out = ctk.CTkLabel(master, text="Output:", font=S_FONT)
        label_out.pack(pady=2, padx=6, side=LEFT)

        button = ctk.CTkButton(master, text="Set Output", width=110, height=28,
                               command=self.set_output_file, font=S_FONT)
        button.pack(padx=6, pady=2, side=RIGHT)

        self.label_output = ctk.CTkLabel(master, text="[Not set]", font=S_FONT, text_color=NOTSET_COLOR)
        self.label_output.pack(pady=2, padx=6, side=LEFT)

    def create_blend_inputs(self, f1, f2, f3, f4, f5, f6):
        # Blend operation buttons
        self.blend_mode = ctk.StringVar(value="multiply")
        
        # Row 1: Multiply, Power
        btn_multiply = ctk.CTkRadioButton(f1, text="Multiply\nA × B", variable=self.blend_mode, 
                                          value="multiply", font=M_FONT)
        btn_multiply.pack(pady=20, padx=16)
        
        btn_power = ctk.CTkRadioButton(f2, text="Power\nA ^ B", variable=self.blend_mode, 
                                       value="power", font=M_FONT)
        btn_power.pack(pady=20, padx=16)
        
        # Row 2: Add, Subtract
        btn_add = ctk.CTkRadioButton(f3, text="Add\nA + B", variable=self.blend_mode, 
                                     value="add", font=M_FONT)
        btn_add.pack(pady=20, padx=16)
        
        btn_subtract = ctk.CTkRadioButton(f4, text="Subtract\nA - B", variable=self.blend_mode, 
                                          value="subtract", font=M_FONT)
        btn_subtract.pack(pady=20, padx=16)
        
        # Row 3: Max, Min
        btn_max = ctk.CTkRadioButton(f5, text="Max\nmax(A,B)", variable=self.blend_mode, 
                                     value="max", font=M_FONT)
        btn_max.pack(pady=20, padx=16)
        
        btn_min = ctk.CTkRadioButton(f6, text="Min\nmin(A,B)", variable=self.blend_mode, 
                                     value="min", font=M_FONT)
        btn_min.pack(pady=20, padx=16)

    # ------------------ FILE HANDLERS ------------------

    def set_input_file_a(self):
        file = filedialog.askopenfilename(title="Select Input File A")
        if file:
            self.input_path_a = file
            filename = os.path.basename(file)
            self.label_input_a.configure(text=filename, text_color="white")
            try:
                img_a = Image.open(file)
                L.Logger().log(f"Input file A loaded: {filename}", "INFO")
                # Update preview with image A
                self.img = img_a
                self.update_preview()
            except Exception as e:
                L.Logger().log(f"Failed to open image A: {str(e)}", "ERROR")
        else:
            self.input_path_a = None
            self.label_input_a.configure(text="(Not set)", text_color=NOTSET_COLOR)
            L.Logger().log("Input file A not selected.", "WARN")

    def set_input_file_b(self):
        file = filedialog.askopenfilename(title="Select Input File B")
        if file:
            self.input_path_b = file
            filename = os.path.basename(file)
            self.label_input_b.configure(text=filename, text_color="white")
            L.Logger().log(f"Input file B loaded: {filename}", "INFO")
        else:
            self.input_path_b = None
            self.label_input_b.configure(text="(Not set)", text_color=NOTSET_COLOR)
            L.Logger().log("Input file B not selected.", "WARN")

    def set_output_file(self):
        file = filedialog.asksaveasfilename(
            title="Select Output File",
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("TIFF files", "*.tiff"),
                       ("JPEG files", "*.jpg"), ("All files", "*.*")]
        )
        if file:
            self.output_path = file
            filename = os.path.basename(file)
            self.label_output.configure(text=filename, text_color="white")
            L.Logger().log(f"Output file set: {filename}", "INFO")
        else:
            self.output_path = None
            self.label_output.configure(text="(Not set)", text_color=NOTSET_COLOR)
            L.Logger().log("Output file not selected.", "WARN")

    # ------------------ IMAGE PROCESSING ------------------
    def generate(self):
        def generate_thr():
            try:
                if not self.input_path_a or not os.path.exists(self.input_path_a):
                    L.Logger().log("Please select input file A first.", "WARNING")
                    return
                
                if not self.input_path_b or not os.path.exists(self.input_path_b):
                    L.Logger().log("Please select input file B first.", "WARNING")
                    return

                # Load images
                img_a = Image.open(self.input_path_a).convert("RGBA")
                img_b = Image.open(self.input_path_b).convert("RGBA")

                # Check if images have the same dimensions
                if img_a.size != img_b.size:
                    L.Logger().log(f"Images must have the same dimensions. A: {img_a.size}, B: {img_b.size}", "ERROR")
                    return

                # Convert to numpy arrays (float32 for precision)
                img_array_a = np.array(img_a, dtype=np.float32) / 255.0  # Normalize to 0-1
                img_array_b = np.array(img_b, dtype=np.float32) / 255.0  # Normalize to 0-1

                # Get channel selections
                ch_a = self.channel_a_var.get()
                ch_b = self.channel_b_var.get()
                
                # Extract channels from image A
                if ch_a == "RGBA":
                    channels_a = img_array_a
                elif ch_a == "R":
                    channels_a = np.stack([img_array_a[:,:,0]] * 4, axis=-1)
                elif ch_a == "G":
                    channels_a = np.stack([img_array_a[:,:,1]] * 4, axis=-1)
                elif ch_a == "B":
                    channels_a = np.stack([img_array_a[:,:,2]] * 4, axis=-1)
                elif ch_a == "A":
                    channels_a = np.stack([img_array_a[:,:,3]] * 4, axis=-1)
                
                # Extract channels from image B
                if ch_b == "RGBA":
                    channels_b = img_array_b
                elif ch_b == "R":
                    channels_b = np.stack([img_array_b[:,:,0]] * 4, axis=-1)
                elif ch_b == "G":
                    channels_b = np.stack([img_array_b[:,:,1]] * 4, axis=-1)
                elif ch_b == "B":
                    channels_b = np.stack([img_array_b[:,:,2]] * 4, axis=-1)
                elif ch_b == "A":
                    channels_b = np.stack([img_array_b[:,:,3]] * 4, axis=-1)

                # Apply blend operation based on selected mode
                blend_mode = self.blend_mode.get()
                
                if blend_mode == "multiply":
                    # Multiply: A × B
                    img_result = channels_a * channels_b
                elif blend_mode == "add":
                    # Add: A + B (clamped to 1.0)
                    img_result = np.clip(channels_a + channels_b, 0, 1)
                elif blend_mode == "subtract":
                    # Subtract: A - B (clamped to 0.0)
                    img_result = np.clip(channels_a - channels_b, 0, 1)
                elif blend_mode == "power":
                    # Power: A ^ B (handle edge cases)
                    # Avoid issues with 0^0 and negative bases
                    with np.errstate(divide='ignore', invalid='ignore'):
                        img_result = np.power(channels_a, channels_b)
                        img_result = np.nan_to_num(img_result, nan=0.0, posinf=1.0, neginf=0.0)
                    img_result = np.clip(img_result, 0, 1)
                elif blend_mode == "min":
                    # Min: minimum of A and B for each pixel
                    img_result = np.minimum(channels_a, channels_b)
                elif blend_mode == "max":
                    # Max: maximum of A and B for each pixel
                    img_result = np.maximum(channels_a, channels_b)

                # Convert back to 0-255 range
                img_result = np.clip(img_result * 255, 0, 255).astype(np.uint8)
                
                self.img = Image.fromarray(img_result, mode='RGBA')

                self.export_button.configure(state=NORMAL)
                self.update_preview()
                L.Logger().log(f"Blend {blend_mode} completed successfully!", "SUCCESS")

            except Exception as e:
                L.Logger().log(f"Failed to process: {str(e)}", "ERROR")

        threading.Thread(target=generate_thr, daemon=True).start()

    # ------------------ EXPORT ------------------
    def export(self):
        def export_thr():
            try:
                if not self.output_path:
                    self.set_output_file()
                    if not self.output_path:
                        L.Logger().log("Export aborted: No output file specified.", "ERROR")
                        return

                self.img.save(self.output_path)
                L.Logger().log(f"Image saved to: {self.output_path}", "SUCCESS")
            except Exception as e:
                L.Logger().log(f"Failed to save: {str(e)}", "ERROR")

        threading.Thread(target=export_thr, daemon=True).start()