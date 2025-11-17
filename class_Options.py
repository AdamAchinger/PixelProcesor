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




class OptionsTab:
    def __init__(self, master, log_text_widget=None):
        self.master = master
        self.log_text_widget = log_text_widget
        self.log_color = "#222222"
        
        # Ścieżka do pliku konfiguracyjnego - zapisujemy w folderze użytkownika
        # aby konfiguracja przetrwała między uruchomieniami EXE
        if getattr(sys, 'frozen', False):
            # Jeśli aplikacja jest spakowana do EXE
            config_dir = Path(os.path.expanduser("~")) / ".pixelprocessor"
            config_dir.mkdir(exist_ok=True)
            self.config_file = config_dir / "config.json"
        else:
            # Jeśli uruchamiamy ze skryptu Python
            self.config_file = Path("config.json")
        
        # Wczytaj zapisaną konfigurację
        self.load_config()
        
        self.main_frame = ctk.CTkFrame(
            master, 
            corner_radius=10, 
            border_width=2,
            fg_color=("white", "gray20")
        )
        self.main_frame.pack(padx=20, pady=20, fill="both")

        self.left_frame = ctk.CTkFrame(self.main_frame)
        self.left_frame.pack(side="left",padx=20, pady=20, fill="both",expand=True)

        text = (
            f"PixelProcessor - Version: {TOOL_VERSION}\n" 
        )

        self.label = ctk.CTkLabel(
            self.left_frame, 
            text=text,
            font=S_FONT, 
            text_color=("gray10", "white"),
            justify="left"
        )
        self.label.pack(side="top", padx=20, pady=(30, 1), anchor="w")

        self.link = ctk.CTkLabel(
            self.left_frame,
            text=(
                "Created by Adam Achinger\n"
                "https://github.com/AdamAchinger\n"
                "¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯"    
            ),
            font=S_FONT,
            text_color="#3D6DD5",
            justify="left"
        )
        self.link.pack(side="top", padx=20, pady=(1, 10), anchor="w") 
        self.link.bind("<Button-1>", lambda e: webbrowser.open_new("https://github.com/AdamAchinger"))
        
        self.functions_label = ctk.CTkLabel(
            self.left_frame,
            text=FUNCTIONS,
            font=S_FONT,
            text_color=("gray10", "white"),
            justify="left"
        )
        self.functions_label.pack(side="bottom",padx=20, pady=(10, 10), anchor="w") 

        self.right_frame = ctk.CTkFrame(self.main_frame)
        self.right_frame.pack(side="right",padx=20, pady=20, fill="both",expand=True)

        self.theme_frame = ctk.CTkFrame(self.right_frame, fg_color="transparent")
        self.theme_frame.pack(padx=30, pady=(10, 20))

        self.theme_label = ctk.CTkLabel(
            self.theme_frame,
            text="Appearance",
            font=M_FONT, 
            text_color=("gray10", "white")
        )
        self.theme_label.pack(padx=0, pady=(0, 10))

        # --- Tryby (Light/Dark) ---
        self.mode_buttons_frame = ctk.CTkFrame(self.theme_frame, fg_color="transparent")
        self.mode_buttons_frame.pack(padx=0, pady=0)

        self.light_mode_button = ctk.CTkButton(
            self.mode_buttons_frame,
            text="Light Mode",
            command=self.set_light_mode,
            font=S_FONT, 
            width=100
        )
        self.light_mode_button.pack(side="left", padx=(0, 4))

        self.dark_mode_button = ctk.CTkButton(
            self.mode_buttons_frame,
            text="Dark Mode",
            command=self.set_dark_mode,
            font=S_FONT,
            width=100
        )
        self.dark_mode_button.pack(side="left", padx=4)

        # --- Motywy (Theme Buttons) ---
        self.theme_buttons_frame_row1 = ctk.CTkFrame(self.theme_frame, fg_color="transparent")
        self.theme_buttons_frame_row1.pack(padx=0, pady=(15, 0))

        self.breeze_theme_button = ctk.CTkButton(
            self.theme_buttons_frame_row1,
            text="Breeze",
            command=lambda: self.set_theme("breeze"),
            font=S_FONT,
            width=85
        )
        self.breeze_theme_button.pack(side="left", padx=4, pady=5)

        self.marsh_theme_button = ctk.CTkButton(
            self.theme_buttons_frame_row1,
            text="Marsh",
            command=lambda: self.set_theme("marsh"),
            font=S_FONT,
            width=85
        )
        self.marsh_theme_button.pack(side="left", padx=4, pady=5)

        self.metal_theme_button = ctk.CTkButton(
            self.theme_buttons_frame_row1,
            text="Metal",
            command=lambda: self.set_theme("metal"),
            font=S_FONT,
            width=85
        )
        self.metal_theme_button.pack(side="left", padx=4, pady=5)

        self.red_theme_button = ctk.CTkButton(
            self.theme_buttons_frame_row1,
            text="Red",
            command=lambda: self.set_theme("red"),
            font=S_FONT,
            width=85
        )
        self.red_theme_button.pack(side="left", padx=4, pady=5)

        self.rime_theme_button = ctk.CTkButton(
            self.theme_buttons_frame_row1,
            text="Rime",
            command=lambda: self.set_theme("rime"),
            font=S_FONT,
            width=85
        )
        self.rime_theme_button.pack(side="left", padx=4, pady=5)

        self.theme_buttons_frame_row2 = ctk.CTkFrame(self.theme_frame, fg_color="transparent")
        self.theme_buttons_frame_row2.pack(padx=0, pady=0)

        self.yellow_theme_button = ctk.CTkButton(
            self.theme_buttons_frame_row2,
            text="Yellow",
            command=lambda: self.set_theme("yellow"),
            font=S_FONT,
            width=85
        )
        self.yellow_theme_button.pack(side="left", padx=4, pady=5)

        self.blue_theme_button = ctk.CTkButton(
            self.theme_buttons_frame_row2,
            text="Rime",
            command=lambda: self.set_theme("rime"),
            font=S_FONT,
            width=85
        )
        self.blue_theme_button.pack(side="left", padx=4, pady=5)

        self.darkblue_theme_button = ctk.CTkButton(
            self.theme_buttons_frame_row2,
            text="Blue",
            command=lambda: self.set_theme("dark-blue"),
            font=S_FONT,
            width=85
        )
        self.darkblue_theme_button.pack(side="left", padx=4, pady=5)

        self.green_theme_button = ctk.CTkButton(
            self.theme_buttons_frame_row2,
            text="Green",
            command=lambda: self.set_theme("green"),
            font=S_FONT,
            width=85
        )
        self.green_theme_button.pack(side="left", padx=4, pady=5)

        # --- Frame dla Save and Restart i wybranego motywu ---
        self.save_frame = ctk.CTkFrame(self.theme_frame, fg_color="transparent")
        self.save_frame.pack(padx=0, pady=(20, 0))

        # Label pokazujący wybrany motyw
        self.selected_theme_label = ctk.CTkLabel(
            self.save_frame,
            text=f"Selected: {getattr(self, 'current_theme', 'blue').capitalize()}",
            font=S_FONT,
            text_color=("gray10", "white")
        )
        self.selected_theme_label.pack(side="left", padx=(0, 10))

        # Przycisk "Save and Restart"
        self.save_restart_button = ctk.CTkButton(
            self.save_frame,
            text="Save and Restart",
            command=self.save_and_restart,
            font=S_FONT,
            width=100
        )
        self.save_restart_button.pack(side="left", padx=4)

    def load_config(self):
        """Wczytuje konfigurację z pliku JSON i zwraca motyw"""
        try:
            if self.config_file.exists():
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                    
                # Wczytaj motyw
                theme = config.get('theme', 'blue')
                self.current_theme = theme
                
                # Wczytaj tryb (light/dark)
                appearance = config.get('appearance_mode', 'Dark')
                ctk.set_appearance_mode(appearance)
                
                # Ustaw kolor logu
                if appearance == "Light":
                    self.log_color = "#4C4C4C"
                else:
                    self.log_color = "#222222"
                
                return theme
                    
            else:
                # Domyślna konfiguracja
                self.current_theme = 'blue'
                ctk.set_appearance_mode("Dark")
                return 'blue'
                
        except Exception as e:
            print(f"Błąd wczytywania konfiguracji: {e}")
            self.current_theme = 'blue'
            ctk.set_appearance_mode("Dark")
            return 'blue'

    def save_config(self):
        """Zapisuje aktualną konfigurację do pliku JSON"""
        try:
            config = {
                'theme': getattr(self, 'current_theme', 'blue'),
                'appearance_mode': ctk.get_appearance_mode()
            }
            
            # Upewnij się, że katalog istnieje
            self.config_file.parent.mkdir(parents=True, exist_ok=True)
            
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=4)
                
            return True
        except Exception as e:
            print(f"Błąd zapisywania konfiguracji: {e}")
            return False

    def set_light_mode(self):
        ctk.set_appearance_mode("Light")
        self.log_color = "#4C4C4C"
        if self.log_text_widget:
            self.log_text_widget.configure(fg_color=self.log_color)
    
    def set_dark_mode(self):
        ctk.set_appearance_mode("Dark")          
        self.log_color = "#222222"
        if self.log_text_widget:
            self.log_text_widget.configure(fg_color=self.log_color)

    def set_theme(self, theme_name):
        """Ustawia wybrany motyw (bez restartu)"""
        self.current_theme = theme_name
        # Aktualizuj label z wybranym motywem
        self.selected_theme_label.configure(text=f"Selected: {theme_name.capitalize()}")

    def save_and_restart(self):
        """Zapisuje konfigurację i restartuje aplikację"""
        if self.save_config():
            # Restartuj aplikację
            import subprocess
            
            if getattr(sys, 'frozen', False):
                # Jeśli aplikacja jest spakowana do EXE
                subprocess.Popen([sys.executable])
            else:
                # Jeśli uruchamiamy ze skryptu Python
                python = sys.executable
                subprocess.Popen([python] + sys.argv)
            
            # Zamknij obecne okno
            self.master.quit()
