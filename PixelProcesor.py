import os
import threading
from tkinter import *
import customtkinter as ctk
import sys
from pathlib import Path
from config import *
import utils as u 
import json


def main():
    def load_theme_from_config():
        """Wczytuje zapisany motyw z config.json"""
        try:
            if getattr(sys, 'frozen', False):
                config_dir = Path(os.path.expanduser("~")) / ".pixelprocessor"
                config_file = config_dir / "config.json"
            else:
                config_file = Path("config.json")
            
            if config_file.exists():
                with open(config_file, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                
                theme = config.get('theme', 'blue')
                
                if getattr(sys, 'frozen', False):
                    theme_path = Path(sys._MEIPASS) / "themes" / f"{theme}.json"
                else:
                    theme_path = Path("themes") / f"{theme}.json"
                
                if theme_path.exists():
                    ctk.set_default_color_theme(str(theme_path))
                    return theme
            
            ctk.set_default_color_theme("blue")
            return "blue"
                
        except Exception as e:
            print(f"Błąd wczytywania motywu: {e}")
            ctk.set_default_color_theme("blue")
            return "blue"
    
    # Initialize window
    root = ctk.CTk()
    ctk.set_appearance_mode("Dark")
    load_theme_from_config()

    root.configure(bg=BG_COLOR)
    root.title(f"Pixel Processor {TOOL_VERSION}")
    
    try:
        if os.path.exists(ICON_PATH):
            root.iconbitmap(ICON_PATH)
    except:
        pass

    root.resizable(FALSE, FALSE)
    
    # Center window
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = int((screen_width / 2) - (APP_WIDTH / 2))
    y = int((screen_height / 2) - (APP_HEIGHT / 2))
    root.geometry(f'{APP_WIDTH}x{APP_HEIGHT}+{x}+{y}')

    # Main frame
    main_frame = ctk.CTkFrame(root)
    main_frame.pack(expand=True, fill="both")

    # Create tab view
    tab_view = ctk.CTkTabview(main_frame, height=APP_HEIGHT - 120)
    tab_view.pack(expand=True, fill="both", padx=5, pady=(5, 0))

    # Add tabs
    tab1 = tab_view.add("Solid Color")
    tab2 = tab_view.add("Gradient")
    tab3 = tab_view.add("Math")
    tab4 = tab_view.add("Blend")
    tab5 = tab_view.add("Separate")
    tab6 = tab_view.add("Combine")
    tab7 = tab_view.add("Transform")
    tab8 = tab_view.add("Atlas")
    tab9 = tab_view.add("Options")

    # Style tabs
    my_font = ctk.CTkFont(size=18)
    for button in tab_view._segmented_button._buttons_dict.values():
        button.configure(height=32, font=my_font)

    # Log section at the bottom (tworzymy PRZED inicjalizacją OptionsTab)
    log_frame = ctk.CTkFrame(main_frame, height=80)
    log_frame.pack(fill="x", padx=5, pady=5, side="bottom")
    log_frame.pack_propagate(False)
    
    log_text = ctk.CTkTextbox(
        log_frame,
        height=70,
        font=LOG_FONT,
        fg_color="#222222",
        state="disabled"
    )
    log_text.pack(fill="both", expand=True, padx=10, pady=5)

    # Initialize tabs
    from class_Soon import SoonTab
    from class_Options import OptionsTab
    from class_Logger import Logger

    from class_SolidColor import SolidColorTab
    solid_tab = SolidColorTab(tab1)

    from class_Gradient import GradientTab
    gradient_tab = GradientTab(tab2)

    from class_Math import MathTab
    math_tab = MathTab(tab3)

    from class_Blend import BlendTab
    blend_tab = BlendTab(tab4)

    from class_Separate import SeparateTab
    separate_tab = SeparateTab(tab5)

    from class_Combine import CombineTab
    combine_tab = CombineTab(tab6)

    transform_tab = SoonTab(tab7)
    atlas_tab = SoonTab(tab8)

    options_tab = OptionsTab(tab9, log_text)  # Przekazujemy referencję do log_text

    # Initialize logger
    logger = Logger()
    logger.set_widget(log_text)
    logger.log("Pixel Processor started successfully.", "SUCCESS")

    root.mainloop()


if __name__ == "__main__":
    main()
    