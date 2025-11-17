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

def create_tab_frame(master):
    """Tworzy główną strukturę ramek dla zakładki"""
    frame_master = ctk.CTkFrame(master, fg_color=FG_COLOR)
    frame_master.pack(fill=Y, expand=TRUE)

    frame_top = ctk.CTkFrame(frame_master)
    frame_top.pack(padx=2, pady=2)

    left_tab_frame = ctk.CTkFrame(frame_top, width=550, fg_color=PREVIEW_BORDER_COLOR)
    left_tab_frame.pack(padx=5, pady=5, side=LEFT)

    right_tab_frame = ctk.CTkFrame(frame_top, width=400)
    right_tab_frame.pack(fill=Y, side=LEFT)

    frame_top_right = ctk.CTkFrame(right_tab_frame, height=50)
    frame_top_right.pack(padx=1, pady=1, side=TOP)

    frame_scroll = ctk.CTkScrollableFrame(right_tab_frame, width=400)
    frame_scroll.pack(padx=1, pady=1, fill=Y, expand=TRUE)

    frame_bottom = ctk.CTkFrame(frame_master, height=50)
    frame_bottom.pack(padx=1, pady=1, side=TOP, fill=X)

    return left_tab_frame, frame_top_right, frame_scroll, frame_bottom

def create_slider(master, label, is_alpha, default=0.5):
    """Tworzy slider z etykietą i polem tekstowym"""
    frame = ctk.CTkFrame(master)
    frame.pack(padx=2, pady=1, fill=X)

    label_widget = ctk.CTkLabel(frame, text=label, font=M_FONT)
    label_widget.pack(padx=8, side=LEFT)

    slider_var = ctk.DoubleVar()
    slider_var.set(1 if is_alpha else default)

    slider = ctk.CTkSlider(frame, variable=slider_var, from_=0, to=1, width=200)
    slider.pack(padx=4, side=RIGHT)

    slider_entry = ctk.CTkEntry(frame, textvariable=slider_var, width=60, font=M_FONT)
    slider_entry.pack(padx=4, side=RIGHT)

    return slider

def parse_rgba_values(input_str, param_name):
    """Parsuje i waliduje ciągi znaków RGBA"""
    try:
        values = [float(x.strip()) for x in input_str.split(',')]
        if len(values) != 4:
            raise ValueError(f"{param_name} must have 4 values")
        return values
    except ValueError as e:
        L.Logger().log(f"Invalid {param_name} format: {str(e)}. Expected: R,G,B,A", "ERROR")
        return None

def load_preview_image():
    """Ładuje obrazek podglądu lub tworzy szary jeśli nie istnieje"""
    try:
        if os.path.exists(PREVIEW_PATH):
            return Image.open(PREVIEW_PATH).convert("RGB")
        else:
            return Image.new("RGB", (480, 480), (128, 128, 128))
    except:
        return Image.new("RGB", (480, 480), (128, 128, 128))
    
def load_theme_from_config():
    """Wczytuje motyw z config.json i ustawia go globalnie"""
    config_file = Path("config.json")
    
    try:
        if config_file.exists():
            with open(config_file, 'r') as f:
                config = json.load(f)
                
            theme = config.get('theme', 'blue')
            theme_path = f"themes/{theme}.json"
            
            if Path(theme_path).exists():
                ctk.set_default_color_theme(theme_path)
            else:
                ctk.set_default_color_theme(theme)
        else:
            ctk.set_default_color_theme("blue")
            
    except Exception as e:
        print(f"Błąd wczytywania motywu: {e}")
        ctk.set_default_color_theme("blue")



def resource_path(relative_path):
    """Zwraca prawidłową ścieżkę do zasobów dla aplikacji EXE i zwykłego uruchomienia"""
    try:
        # PyInstaller tworzy tymczasowy folder i przechowuje ścieżkę w _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)
