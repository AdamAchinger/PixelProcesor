
from tkinter import *
import customtkinter as ctk
from config import *


class SoonTab:
    def __init__(self, master):
        self.main_frame = ctk.CTkFrame(master)
        self.main_frame.pack(padx=20, pady=20, fill="both", expand=True)
    
        self.label = ctk.CTkLabel(
            self.main_frame, 
            text="SOON",
            font=B_FONT
        )
        self.label.pack(expand=True)