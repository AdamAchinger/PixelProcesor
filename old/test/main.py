import customtkinter as ctk
import sys
import json
import os

SETTINGS_FILE = "settings.json"

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Dynamiczna zmiana motywu - CustomTkinter")
        self.geometry("600x500")
        
        # 1️⃣ Wczytaj zapisane ustawienia lub ustaw domyślne
        settings = self.load_settings()
        self.mode_var = ctk.StringVar(value=settings.get("mode", "dark"))
        self.color_var = ctk.StringVar(value=settings.get("color", "blue"))
        
        # 2️⃣ Ustawienia globalne
        ctk.set_appearance_mode(self.mode_var.get())
        ctk.set_default_color_theme(self.color_var.get())
        
        # 3️⃣ Utwórz interfejs
        self.create_widgets()
        
    def create_widgets(self):
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        self.title_label = ctk.CTkLabel(
            self.main_frame, 
            text="🎨 Dynamiczna zmiana motywu",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        self.title_label.pack(pady=20)
        
        # Tryb (light/dark/system)
        self.mode_frame = ctk.CTkFrame(self.main_frame)
        self.mode_frame.pack(pady=10, padx=20, fill="x")
        
        self.mode_label = ctk.CTkLabel(self.mode_frame, text="Tryb wyglądu:", font=ctk.CTkFont(size=16))
        self.mode_label.pack(pady=10)
        
        self.mode_options = ctk.CTkSegmentedButton(
            self.mode_frame,
            values=["light", "dark", "system"],
            variable=self.mode_var,
            command=self.change_appearance_mode
        )
        self.mode_options.pack(pady=10, padx=20)
        
        # Kolor motywu (blue/green/dark-blue)
        self.color_frame = ctk.CTkFrame(self.main_frame)
        self.color_frame.pack(pady=10, padx=20, fill="x")
        
        self.color_label = ctk.CTkLabel(self.color_frame, text="Kolor motywu:", font=ctk.CTkFont(size=16))
        self.color_label.pack(pady=10)
        
        self.color_menu = ctk.CTkOptionMenu(
            self.color_frame,
            values=["blue", "green", "dark-blue"],
            variable=self.color_var,
            command=self.change_color_theme
        )
        self.color_menu.pack(pady=10)
        
        # Przykładowe elementy interfejsu
        self.demo_frame = ctk.CTkFrame(self.main_frame)
        self.demo_frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        self.demo_label = ctk.CTkLabel(self.demo_frame, text="Przykładowe elementy interfejsu:", font=ctk.CTkFont(size=14, weight="bold"))
        self.demo_label.pack(pady=10)
        
        self.demo_button = ctk.CTkButton(self.demo_frame, text="Przykładowy przycisk", command=lambda: print("Kliknięto przycisk!"))
        self.demo_button.pack(pady=5)
        
        self.demo_entry = ctk.CTkEntry(self.demo_frame, placeholder_text="Wpisz coś tutaj...")
        self.demo_entry.pack(pady=5)
        
        self.demo_slider = ctk.CTkSlider(self.demo_frame, from_=0, to=100)
        self.demo_slider.pack(pady=5)
        self.demo_slider.set(50)
        
        self.demo_switch = ctk.CTkSwitch(self.demo_frame, text="Przykładowy przełącznik")
        self.demo_switch.pack(pady=5)
        
        self.demo_progress = ctk.CTkProgressBar(self.demo_frame)
        self.demo_progress.pack(pady=5)
        self.demo_progress.set(0.7)

    # --- Funkcje zmiany i zapisu ustawień ---
    def change_appearance_mode(self, mode):
        ctk.set_appearance_mode(mode)
        print(f"Zmieniono tryb na: {mode}")
        self.save_settings()

    def change_color_theme(self, color):
        ctk.set_default_color_theme(color)
        self.color_var.set(color)
        print(f"Zmieniono motyw na: {color}")
        self.save_settings()
        self.restart_app()
        
    def restart_app(self):
        if hasattr(self, 'main_frame'):
            self.main_frame.destroy()
        self.create_widgets()
        ctk.set_appearance_mode(self.mode_var.get())

    # --- Zapisywanie/odczyt ustawień ---
    def save_settings(self):
        data = {
            "mode": self.mode_var.get(),
            "color": self.color_var.get()
        }
        with open(SETTINGS_FILE, "w") as f:
            json.dump(data, f)
        print("Ustawienia zapisane:", data)

    def load_settings(self):
        if os.path.exists(SETTINGS_FILE):
            with open(SETTINGS_FILE, "r") as f:
                return json.load(f)
        return {}

if __name__ == "__main__":
    app = App()
    app.mainloop()
