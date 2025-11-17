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
# GRADIENT CLASS
# ============================================================================

class GradientTab:
    def __init__(self, master):
        self.img = u.load_preview_image()
        self.output_path = None  # brak automatycznego outputu

        left_tab_frame, frame_top, frame_scroll, frame_bottom = u.create_tab_frame(master)

        # Frames
        frame1 = ctk.CTkFrame(frame_scroll)
        frame1.pack()
        frame11 = ctk.CTkFrame(frame_scroll)
        frame11.pack()
        frame2 = ctk.CTkFrame(frame_scroll)
        frame2.pack()
        frame3 = ctk.CTkFrame(frame_scroll)
        frame3.pack(padx=1, side=LEFT)

        frame01 = ctk.CTkFrame(frame1, width=CELL_W2, height=CELL_H2)
        frame01.pack(padx=2, pady=2, side=LEFT)
        frame01.propagate(False)

        frame011 = ctk.CTkFrame(frame11, width=CELL_W2, height=CELL_H2)
        frame011.pack(padx=2, pady=2, side=LEFT)
        frame011.propagate(False)

        frame02 = ctk.CTkFrame(frame2, width=CELL_W, height=CELL_H)
        frame02.pack(padx=2, pady=2, side=LEFT)
        frame02.propagate(False)

        frame03 = ctk.CTkFrame(frame2, width=CELL_W, height=CELL_H)
        frame03.pack(padx=2, pady=2, side=LEFT)
        frame03.propagate(False)

        frame04 = ctk.CTkFrame(frame3, width=CELL_W, height=CELL_H)
        frame04.pack(padx=2, pady=2, side=LEFT)
        frame04.propagate(False)

        frame05 = ctk.CTkFrame(frame3, width=CELL_W, height=CELL_H)
        frame05.pack(padx=2, pady=2, side=LEFT)
        frame05.propagate(False)

        frame06 = ctk.CTkFrame(frame_top, width=400, height=30)
        frame06.pack(padx=2, pady=2)
        frame06.propagate(False)

        # Preview
        self.create_preview(left_tab_frame)

        # Output directory
        self.create_output_dir(frame06)

        # Buttons
        self.export_button = ctk.CTkButton(
            frame_bottom, text="Export", width=198, height=40,
            state=DISABLED, command=self.export, font=B_FONT
        )
        self.export_button.pack(pady=2, padx=2, side=RIGHT)

        generate_button = ctk.CTkButton(
            frame_bottom, text="Generate", width=198, height=40,
            command=self.generate, font=B_FONT
        )
        generate_button.pack(pady=2, padx=2, side=RIGHT)

        # Color A
        label_color_a = ctk.CTkLabel(frame01, text="Color A (RGBA)", font=M_FONT)
        label_color_a.pack(pady=6, padx=16)

        self.a_slider_red = u.create_slider(frame01, "Red", False, 1.0)
        self.a_slider_green = u.create_slider(frame01, "Green", False, 1.0)
        self.a_slider_blue = u.create_slider(frame01, "Blue", False, 1.0)
        self.a_slider_alpha = u.create_slider(frame01, "Alpha", True)

        # Color B
        label_color_b = ctk.CTkLabel(frame011, text="Color B (RGBA)", font=M_FONT)
        label_color_b.pack(pady=6, padx=16)

        self.b_slider_red = u.create_slider(frame011, "Red", False, 0.0)
        self.b_slider_green = u.create_slider(frame011, "Green", False, 0.0)
        self.b_slider_blue = u.create_slider(frame011, "Blue", False, 0.0)
        self.b_slider_alpha = u.create_slider(frame011, "Alpha", True)

        # Filename
        label_filename = ctk.CTkLabel(frame02, text="File Name", font=M_FONT)
        label_filename.pack(pady=6, padx=16)

        self.input_filename = ctk.CTkEntry(frame02, width=ENTRY_WIDTH, font=M_FONT)
        self.input_filename.pack(pady=6, padx=16)
        self.input_filename.insert(0, "T_Gradient")

        # Size
        label_size = ctk.CTkLabel(frame03, text="Size", font=M_FONT)
        label_size.pack(pady=6, padx=16)

        self.input_size_width = ctk.CTkEntry(frame03, width=ENTRY_WIDTH / 2, font=M_FONT)
        self.input_size_width.pack(pady=6, padx=8, side=LEFT)
        self.input_size_width.insert(0, "512")

        label_x = ctk.CTkLabel(frame03, text="x", font=M_FONT)
        label_x.pack(pady=6, padx=0, side=LEFT)

        self.input_size_height = ctk.CTkEntry(frame03, width=ENTRY_WIDTH / 2, font=M_FONT)
        self.input_size_height.pack(pady=6, padx=8, side=LEFT)
        self.input_size_height.insert(0, "512")

        # File type
        label_filetype = ctk.CTkLabel(frame04, text="File Type", font=M_FONT)
        label_filetype.pack(pady=6, padx=16)

        self.filetype = ctk.StringVar()
        self.filetype.set(EXTENSIONS[0])
        self.input_filetype = ctk.CTkSegmentedButton(
            frame04, width=250, variable=self.filetype, values=EXTENSIONS, font=S_FONT
        )
        self.input_filetype.pack(pady=6, padx=16)

        # Orientation
        label_orient = ctk.CTkLabel(frame05, text="Orientation", font=M_FONT)
        label_orient.pack(pady=6, padx=16)

        self.input_orient = ctk.StringVar()
        self.input_orient.set(ORIENT[0])
        orient_btn = ctk.CTkSegmentedButton(
            frame05, width=250, variable=self.input_orient, values=ORIENT, font=S_FONT
        )
        orient_btn.pack(pady=6, padx=16)

    # ---------- PREVIEW ----------
    def create_preview(self, master):
        preview_image = ctk.CTkImage(light_image=self.img, size=(480, 480))
        self.preview_label = ctk.CTkLabel(master, image=preview_image, text='')
        self.preview_label.pack(pady=PREVIEW_BORDER_WIDTH, padx=PREVIEW_BORDER_WIDTH)

    def update_preview(self):
        img_preview = ctk.CTkImage(light_image=self.img, size=(480, 480))
        self.preview_label.configure(image=img_preview)
        self.preview_label.image = img_preview

    # ---------- OUTPUT DIRECTORY ----------
    def create_output_dir(self, master):
        label_out = ctk.CTkLabel(master, text="Output:", font=S_FONT)
        label_out.pack(pady=2, padx=6, side=LEFT)

        button = ctk.CTkButton(
            master,
            text="Set Output",
            width=110,
            height=30,
            command=self.set_output_dir,
            font=S_FONT
        )
        button.pack(padx=6, pady=2, side=RIGHT)
        button.pack_propagate(False)

        self.label_path = ctk.CTkLabel(
            master,
            text="[Not set]",
            font=S_FONT,
             text_color=NOTSET_COLOR
        )
        self.label_path.pack(pady=2, padx=6, side=LEFT)

    def set_output_dir(self):
        directory = filedialog.askdirectory(title="Select Output Directory")
        if directory:
            self.output_path = directory
            self.label_path.configure(text=self.output_path, text_color="white")
            L.Logger().log(f"Output directory set: {directory}", "INFO")
        else:
            self.output_path = None
            self.label_path.configure(text="[Not set]",  text_color=NOTSET_COLOR)
            L.Logger().log("Output directory not selected.", "WARN")

    def refresh_path(self):
        if not self.output_path:
            raise ValueError("Output path not set. Please set it before exporting.")

        filename = self.input_filename.get().strip()
        filetype = self.filetype.get().lower()

        if not filename:
            raise ValueError("File name cannot be empty.")

        if not filename.endswith(f".{filetype}"):
            filename += f".{filetype}"

        self.full_path = os.path.join(self.output_path, filename)
        return self.full_path

    # ---------- GENERATION ----------
    def generate(self):
        def generate_thr():
            try:
                # Pobranie kolorów
                r1, g1, b1, a1 = (
                    self.a_slider_red.get(),
                    self.a_slider_green.get(),
                    self.a_slider_blue.get(),
                    self.a_slider_alpha.get(),
                )
                r2, g2, b2, a2 = (
                    self.b_slider_red.get(),
                    self.b_slider_green.get(),
                    self.b_slider_blue.get(),
                    self.b_slider_alpha.get(),
                )

                filetype = self.filetype.get().lower()
                orient = self.input_orient.get()
                width = int(self.input_size_width.get())
                height = int(self.input_size_height.get())

                # Tworzenie gradientu
                if orient in ["H", "H.F"]:
                    gradient = np.linspace(0, 1, width)[np.newaxis, :]
                    gradient = np.tile(gradient, (height, 1))
                else:
                    gradient = np.linspace(0, 1, height)[:, np.newaxis]
                    gradient = np.tile(gradient, (1, width))

                if orient in ["H.F", "V.F"]:
                    gradient = 1 - gradient

                r = (gradient * r2 + (1 - gradient) * r1) * 255
                g = (gradient * g2 + (1 - gradient) * g1) * 255
                b = (gradient * b2 + (1 - gradient) * b1) * 255
                a = (gradient * a2 + (1 - gradient) * a1) * 255

                if filetype == "jpg":
                    img_array = np.stack([r, g, b], axis=2).astype(np.uint8)
                    self.img = Image.fromarray(img_array, mode='RGB')
                else:
                    img_array = np.stack([r, g, b, a], axis=2).astype(np.uint8)
                    self.img = Image.fromarray(img_array, mode='RGBA')

                self.export_button.configure(state=NORMAL)
                self.update_preview()
                L.Logger().log("Gradient image generated successfully!", "SUCCESS")

            except Exception as e:
                L.Logger().log(f"Failed to generate: {e}", "ERROR")
        
        threading.Thread(target=generate_thr, daemon=True).start()

    # ---------- EXPORT ----------
    def export(self):
        def export_thr():
            try:
                full_path = self.refresh_path()
                os.makedirs(os.path.dirname(full_path), exist_ok=True)
                self.img.save(full_path)
                L.Logger().log(f"Image saved to: {full_path}", "SUCCESS")
            except Exception as e:
                L.Logger().log(f"Failed to save: {e}", "ERROR")
        
        threading.Thread(target=export_thr, daemon=True).start()
