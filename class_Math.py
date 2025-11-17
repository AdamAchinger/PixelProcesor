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
# MATH CLASS
# ============================================================================

class MathTab:
    def __init__(self, master):
        self.img = u.load_preview_image()
        self.input_path = None
        self.output_path = None

        left_tab_frame, frame_top, frame_scroll, frame_bottom = u.create_tab_frame(master)

        # Frames - rzędy
        frame1 = ctk.CTkFrame(frame_scroll); frame1.pack()
        frame2 = ctk.CTkFrame(frame_scroll); frame2.pack()
        frame3 = ctk.CTkFrame(frame_scroll); frame3.pack()
        frame4 = ctk.CTkFrame(frame_scroll); frame4.pack()
        

        # Math operations frames
        frame01 = ctk.CTkFrame(frame1, width=CELL_W, height=CELL_H); frame01.pack(padx=2, pady=2, side=LEFT); frame01.propagate(False)
        frame02 = ctk.CTkFrame(frame1, width=CELL_W, height=CELL_H); frame02.pack(padx=2, pady=2, side=LEFT); frame02.propagate(False)
        frame03 = ctk.CTkFrame(frame2, width=CELL_W, height=CELL_H); frame03.pack(padx=2, pady=2, side=LEFT); frame03.propagate(False)
        frame04 = ctk.CTkFrame(frame2, width=CELL_W, height=CELL_H); frame04.pack(padx=2, pady=2, side=LEFT); frame04.propagate(False)
        frame05 = ctk.CTkFrame(frame3, width=CELL_W, height=CELL_H); frame05.pack(padx=2, pady=2, side=LEFT); frame05.propagate(False)
        frame06 = ctk.CTkFrame(frame3, width=CELL_W, height=CELL_H); frame06.pack(padx=2, pady=2, side=LEFT); frame06.propagate(False)

        frame9 = ctk.CTkFrame(frame_scroll, width=CELL_W * 2 + 4, height=CELL_H); 
        frame9.pack(padx=2, pady=2) # Używamy pack(), aby umieścić go na dole
        frame9.propagate(False) 
        ctk.CTkLabel(
            frame9,
            text="Multiplication > Exponentiation > Addition > Subtraction\nMin/Max > Inversion > Posterization",
            font=S_FONT1
        ).pack(pady=10)

        # Input/Output frames
        frame07 = ctk.CTkFrame(frame_top, width=400, height=30); frame07.pack(padx=2, pady=1); frame07.propagate(False)
        frame08 = ctk.CTkFrame(frame_top, width=400, height=30); frame08.pack(padx=2, pady=1); frame08.propagate(False)

        # Invert i Posterize frames - w rzędzie 4 (frame4), obok siebie
        # Ujednolicamy rozmiar na CELL_W x CELL_H, aby pasowały do logiki create_field
        frame_invert = ctk.CTkFrame(frame4, width=CELL_W, height=CELL_H*1.25); frame_invert.pack(padx=2, pady=2, side=LEFT); frame_invert.propagate(False) # Kolumna 1
        frame_posterize = ctk.CTkFrame(frame4, width=CELL_W, height=CELL_H*1.25); frame_posterize.pack(padx=2, pady=2, side=LEFT); frame_posterize.propagate(False) # Kolumna 2

        # Preview
        self.create_preview(left_tab_frame)

        # Input / Output file
        self.create_input_file(frame07)
        self.create_output_file(frame08)

        # Buttons
        self.export_button = ctk.CTkButton(frame_bottom, text="Export", width=198, height=40,
                                         state=DISABLED, command=self.export, font=B_FONT)
        self.export_button.pack(pady=2, padx=2, side=RIGHT)

        generate_button = ctk.CTkButton(frame_bottom, text="Generate", width=198, height=40,
                                         command=self.generate, font=B_FONT)
        generate_button.pack(pady=2, padx=2, side=RIGHT)

        # Math operations
        self.create_math_inputs(frame01, frame02, frame03, frame04, frame05, frame06)

        # Invert & Posterize panels
        self.create_invert_panel(frame_invert)
        self.create_posterize_panel(frame_posterize)

    # ------------------ UI CREATION ------------------

    def create_preview(self, master):
        preview_image = ctk.CTkImage(light_image=self.img, size=(480, 480))
        self.preview_label = ctk.CTkLabel(master, image=preview_image, text='')
        self.preview_label.pack(pady=PREVIEW_BORDER_WIDTH, padx=PREVIEW_BORDER_WIDTH)

    def update_preview(self):
        img_preview = ctk.CTkImage(light_image=self.img, size=(480, 480))
        self.preview_label.configure(image=img_preview)
        self.preview_label.image = img_preview

    def create_input_file(self, master):
        label_in = ctk.CTkLabel(master, text="Input:", font=S_FONT)
        label_in.pack(pady=2, padx=6, side=LEFT)

        button = ctk.CTkButton(master, text="Set Input", width=110, height=30,
                               command=self.set_input_file, font=S_FONT)
        button.pack(padx=6, pady=2, side=RIGHT)
        button.pack_propagate(False)

        self.label_input = ctk.CTkLabel(master, text="[Not set]", font=S_FONT,  text_color=NOTSET_COLOR)
        self.label_input.pack(pady=2, padx=6, side=LEFT)

    def create_output_file(self, master):
        label_out = ctk.CTkLabel(master, text="Output:", font=S_FONT)
        label_out.pack(pady=2, padx=6, side=LEFT)

        button = ctk.CTkButton(master, text="Set Output", width=110, height=30,
                               command=self.set_output_file, font=S_FONT)
        button.pack(padx=6, pady=2, side=RIGHT)
        button.pack_propagate(False)

        self.label_output = ctk.CTkLabel(master, text="[Not set]", font=S_FONT,  text_color=NOTSET_COLOR)
        self.label_output.pack(pady=2, padx=6, side=LEFT)

    # Funkcja pomocnicza do tworzenia pól wejściowych dla operacji matematycznych
    def create_field(self, frame, text, default):
        label = ctk.CTkLabel(frame, text=text, font=M_FONT)
        label.pack(pady=6, padx=16)
        entry = ctk.CTkEntry(frame, width=128, font=S_FONT)
        entry.pack(pady=6, padx=16)
        entry.insert(0, default)
        return entry

    def create_math_inputs(self, f1, f2, f3, f4, f5, f6):
        self.input_multiply = self.create_field(f1, "MULTIPLY", "1,1,1,1")
        self.input_power = self.create_field(f2, "POWER", "1,1,1,1")
        self.input_add = self.create_field(f3, "ADD", "0,0,0,0")
        self.input_subtract = self.create_field(f4, "SUBTRACT", "0,0,0,0")
        self.input_max = self.create_field(f5, "MAX", "1,1,1,1")
        self.input_min = self.create_field(f6, "MIN", "0,0,0,0")

    def create_invert_panel(self, master):
        # Etykieta
        ctk.CTkLabel(master, text="INVERT", font=M_FONT).pack(pady=4)

        # Główny container
        main_container = ctk.CTkFrame(master)
        main_container.pack(padx=25, pady=0)

        # Rząd 1: R, G
        frame_row1 = ctk.CTkFrame(main_container,corner_radius=0)
        frame_row1.pack()

        # Rząd 2: B, A
        frame_row2 = ctk.CTkFrame(main_container,corner_radius=0)
        frame_row2.pack()

        # Inicjalizacja zmiennych BooleanVar
        self.invert_r = ctk.BooleanVar(value=False)
        self.invert_g = ctk.BooleanVar(value=False)
        self.invert_b = ctk.BooleanVar(value=False)
        self.invert_a = ctk.BooleanVar(value=False)

        # Checkboxy w układzie 2x2
        ctk.CTkCheckBox(frame_row1, text="R", variable=self.invert_r, font=M_FONT, width=75).pack(side=LEFT, padx=2, pady=2)
        ctk.CTkCheckBox(frame_row1, text="G", variable=self.invert_g, font=M_FONT, width=75).pack(side=LEFT, padx=2, pady=2)
        
        ctk.CTkCheckBox(frame_row2, text="B", variable=self.invert_b, font=M_FONT, width=75).pack(side=LEFT, padx=2, pady=2)
        ctk.CTkCheckBox(frame_row2, text="A", variable=self.invert_a, font=M_FONT, width=75).pack(side=LEFT, padx=2, pady=2)

    def create_posterize_panel(self, master):
        """Panel Posterize używający funkcji create_field dla ujednoliconego wyglądu."""
        
        # Używamy tej samej funkcji, co dla operacji matematycznych
        self.input_posterize = self.create_field(master, "POSTERIZE", "8,8,8,8")


    # ------------------ FILE HANDLERS ------------------

    def set_input_file(self):
        file = filedialog.askopenfilename(title="Select Input File")
        if file:
            self.input_path = file
            filename = os.path.basename(file)
            self.label_input.configure(text=filename, text_color="white")
            try:
                self.img = Image.open(file)
                self.update_preview()
                L.Logger().log(f"Input file loaded: {filename}", "INFO")
            except Exception as e:
                L.Logger().log(f"Failed to open image: {str(e)}", "ERROR")
        else:
            self.input_path = None
            self.label_input.configure(text="[Not set]",  text_color=NOTSET_COLOR)
            L.Logger().log("Input file not selected.", "WARN")

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
            self.label_output.configure(text="[Not set]",  text_color=NOTSET_COLOR)
            L.Logger().log("Output file not selected.", "WARN")

    # ------------------ IMAGE PROCESSING ------------------
    def generate(self):
        def generate_thr():
            try:
                if not self.input_path or not os.path.exists(self.input_path):
                    L.Logger().log("Please select an input file first.", "WARNING")
                    return
                
                # Parsowanie wartości dla operacji matematycznych
                multiply = u.parse_rgba_values(self.input_multiply.get(), "Multiply")
                power = u.parse_rgba_values(self.input_power.get(), "Power")
                add = u.parse_rgba_values(self.input_add.get(), "Add")
                subtract = u.parse_rgba_values(self.input_subtract.get(), "Subtract")
                min_vals = u.parse_rgba_values(self.input_min.get(), "Min")
                max_vals = u.parse_rgba_values(self.input_max.get(), "Max")

                if None in [multiply, power, add, subtract, min_vals, max_vals]:
                    return

                img_input = Image.open(self.input_path).convert("RGBA")
                img_array = np.array(img_input, dtype=np.float32)

                # Standard math operations
                img_array *= np.array(multiply)
                img_array = np.power(img_array, np.array(power))
                img_array += np.array(add) * 255
                img_array -= np.array(subtract) * 255

                min_array = np.array(min_vals) * 255
                max_array = np.array(max_vals) * 255
                img_array = np.clip(img_array, min_array, max_array)

                # --------- Invert per channel ---------
                for channel_idx, should_invert in enumerate([
                    self.invert_r.get(), 
                    self.invert_g.get(), 
                    self.invert_b.get(), 
                    self.invert_a.get()
                ]):
                    if should_invert:
                        img_array[..., channel_idx] = 255 - img_array[..., channel_idx]

                # --------- Posterize per channel ---------
                posterize_bits_float = u.parse_rgba_values(self.input_posterize.get(), "Posterize Bits")
                
                if posterize_bits_float is None:
                    return

                # Konwersja na liczby całkowite
                posterize_bits = [int(round(b)) for b in posterize_bits_float]
                
                for channel_idx, bits in enumerate(posterize_bits):
                    # Ograniczenie wartości bitów do zakresu [1, 8]
                    bits = max(1, min(8, bits))

                    if bits < 8:
                        levels = 2 ** bits
                        channel_data = img_array[..., channel_idx]
                        # Logika posterizacji
                        img_array[..., channel_idx] = np.floor(channel_data / 256 * levels) * (256 / levels)

                img_array = np.clip(img_array, 0, 255).astype(np.uint8)
                self.img = Image.fromarray(img_array, mode='RGBA')

                self.export_button.configure(state=NORMAL)
                self.update_preview()
                L.Logger().log("Image processed successfully!", "SUCCESS")

            except Exception as e:
                L.Logger().log(f"Failed to process: {str(e)}", "ERROR")

        threading.Thread(target=generate_thr, daemon=True).start()

    # ------------------ EXPORT ------------------
    def export(self):
        def export_thr():
            try:
                if not self.output_path:
                    # Jeśli ścieżka nie jest ustawiona, wywołaj okno dialogowe 'Zapisz jako'
                    self.set_output_file()
                    # Sprawdź, czy użytkownik ustawił ścieżkę
                    if not self.output_path:
                        L.Logger().log("Export aborted: No output file specified.", "ERROR")
                        return

                self.img.save(self.output_path)
                L.Logger().log(f"Image saved to: {self.output_path}", "SUCCESS")
            except Exception as e:
                L.Logger().log(f"Failed to save: {str(e)}", "ERROR")

        threading.Thread(target=export_thr, daemon=True).start()