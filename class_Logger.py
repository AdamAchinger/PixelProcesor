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

# ============================================================================
# LOGGER CLASS
# ============================================================================

class Logger:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance.log_text = None
        return cls._instance
    
    def set_widget(self, text_widget):
        self.log_text = text_widget
    
    def log(self, message, level="INFO"):
        if self.log_text:
            timestamp = datetime.now().strftime("%H:%M:%S")
            color = "white"
            if level == "ERROR":
                color = "#ff4444"
            elif level == "SUCCESS":
                color = "#44ff44"
            elif level == "WARNING":
                color = "#ffaa44"
            
            self.log_text.configure(state="normal")
            self.log_text.insert("end", f"[{timestamp}] ", "timestamp")
            self.log_text.insert("end", f"{message}\n", level.lower())
            self.log_text.tag_config("timestamp", foreground="#888888")
            self.log_text.tag_config("info", foreground="white")
            self.log_text.tag_config("success", foreground="#44ff44")
            self.log_text.tag_config("error", foreground="#ff4444")
            self.log_text.tag_config("warning", foreground="#ffaa44")
            self.log_text.configure(state="disabled")
            self.log_text.see("end")
