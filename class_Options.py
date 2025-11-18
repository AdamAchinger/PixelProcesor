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
        
        # Main container with scrollable frame
        self.main_frame = ctk.CTkScrollableFrame(
            master, 
            corner_radius=10,
            fg_color=("white", "gray20")
        )
        self.main_frame.pack(padx=20, pady=20, fill="both", expand=True)

        # === LEFT COLUMN: About & Functions ===
        self.left_column = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.left_column.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # About Section
        self.about_section = self._create_section_frame(self.left_column, "ABOUT")
        self.about_section.pack(fill="x", padx=10, pady=(10, 20))
        
        version_text = f"PixelProcessor - Version: {TOOL_VERSION}"
        self.version_label = ctk.CTkLabel(
            self.about_section, 
            text=version_text,
            font=M_FONT, 
            text_color=("gray10", "white"),
            justify="left"
        )
        self.version_label.pack(anchor="w", padx=15, pady=(10, 5))

        self.author_link = ctk.CTkLabel(
            self.about_section,
            text="Created by Adam Achinger\nhttps://github.com/AdamAchinger",
            font=S_FONT,
            text_color="#3D6DD5",
            justify="left",
            cursor="hand2"
        )
        self.author_link.pack(anchor="w", padx=15, pady=(0, 10)) 
        self.author_link.bind("<Button-1>", lambda e: webbrowser.open_new("https://github.com/AdamAchinger"))
        

        def add_section(title, text):
            ctk.CTkLabel(
                self.about_section,
                text=title,
                font=M_FONT,
                text_color=("gray10", "white"),
                justify="left"
            ).pack(padx=15, pady=(5, 2),anchor="w")

            ctk.CTkLabel(
                self.about_section,
                text=text,
                font=S_FONT,
                text_color=("gray10", "white"),
                justify="left"
            ).pack(padx=15, pady=(0, 10),anchor="w")


        # Add all sections
        add_section("FUNCTIONS", FUNCTIONS)
        add_section("MATH Pixel-By-Scalar", FUNCTIONS_PBS)
        add_section("BLEND Pixel-By-Pixel", FUNCTIONS_PBP)


        # === RIGHT COLUMN: Appearance Settings ===
        self.right_column = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.right_column.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        # Appearance Section
        self.appearance_section = self._create_section_frame(self.right_column, "APPEARANCE")
        self.appearance_section.pack(fill="x", padx=10, pady=(10, 10))

        # Mode Selection (Light/Dark)
        self.mode_label = ctk.CTkLabel(
            self.appearance_section,
            text="Display Mode",
            font=S_FONT,
            text_color=("gray10", "white")
        )
        self.mode_label.pack(pady=5)

        self.mode_buttons_frame = ctk.CTkFrame(self.appearance_section, fg_color="transparent")
        self.mode_buttons_frame.pack(pady=(0, 15))

        self.light_mode_button = ctk.CTkButton(
            self.mode_buttons_frame,
            text="Light",
            command=self.set_light_mode,
            font=S_FONT,
            width=110,
            height=35
        )
        self.light_mode_button.pack(side="left", padx=5)

        self.dark_mode_button = ctk.CTkButton(
            self.mode_buttons_frame,
            text="Dark",
            command=self.set_dark_mode,
            font=S_FONT,
            width=110,
            height=35
        )
        self.dark_mode_button.pack(side="left", padx=5)

        # Theme Selection
        self.theme_label = ctk.CTkLabel(
            self.appearance_section,
            text="Color Theme",
            font=S_FONT,
            text_color=("gray10", "white")
        )
        self.theme_label.pack(pady=5)

        # Theme buttons grid
        self.themes = [
            ("Breeze", "breeze"),
            ("Marsh", "marsh"),
            ("Metal", "metal"),
            ("Red", "red"),
            ("Rime", "rime"),
            ("Yellow", "yellow"),
            ("Blue", "dark-blue")
        ]

        self.theme_grid = ctk.CTkFrame(self.appearance_section, fg_color="transparent")
        self.theme_grid.pack(pady=(0, 15))

        # Create theme buttons in 2 rows
        for i, (name, theme_id) in enumerate(self.themes):
            row = i // 4
            col = i % 4
            
            btn = ctk.CTkButton(
                self.theme_grid,
                text=name,
                command=lambda t=theme_id, n=name: self.set_theme(t, n),
                font=S_FONT,
                width=90,
                height=35
            )
            btn.grid(row=row, column=col, padx=5, pady=5)

        # Save and Restart button
        self.save_restart_button = ctk.CTkButton(
            self.appearance_section,
            text="💾 Save and Restart",
            command=self.save_and_restart,
            font=M_FONT,
            width=200,
            height=40,
            fg_color=("#3D6DD5", "#1F538D"),
            hover_color=("#2E5AB8", "#164070")
        )
        self.save_restart_button.pack(padx=15, pady=(5, 15),side="right")

        # Configure grid weights for responsive layout
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)

    def _create_section_frame(self, parent, title):
        """Helper method to create consistent section frames"""
        frame = ctk.CTkFrame(
            parent,
            corner_radius=8,
            border_width=2,
            border_color=("gray70", "gray30"),
            fg_color=("gray95", "gray17")
        )
        
        title_label = ctk.CTkLabel(
            frame,
            text=title,
            font=M_FONT,
            text_color=("gray10", "white")
        )
        title_label.pack(pady=(10, 5))
        
        return frame

    def load_config(self):
        """Wczytuje konfigurację z pliku JSON i zwraca motyw"""
        try:
            if self.config_file.exists():
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                    
                # Wczytaj motyw
                theme = config.get('theme', 'dark-blue')
                theme_name = config.get('theme_name', 'Blue')
                self.current_theme = theme
                self.current_theme_name = theme_name
                
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
                self.current_theme = 'dark-blue'
                self.current_theme_name = 'Blue'
                ctk.set_appearance_mode("Dark")
                return 'dark-blue'
                
        except Exception as e:
            print(f"Błąd wczytywania konfiguracji: {e}")
            self.current_theme = 'dark-blue'
            self.current_theme_name = 'Blue'
            ctk.set_appearance_mode("Dark")
            return 'dark-blue'

    def save_config(self):
        """Zapisuje aktualną konfigurację do pliku JSON"""
        try:
            config = {
                'theme': getattr(self, 'current_theme', 'dark-blue'),
                'theme_name': getattr(self, 'current_theme_name', 'Blue'),
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

    def set_theme(self, theme_id, theme_name):
        """Ustawia wybrany motyw (bez restartu)"""
        self.current_theme = theme_id
        self.current_theme_name = theme_name
        # Aktualizuj label z wybranym motywem
        self.selected_theme_label.configure(text=f"Current: {theme_name}")

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