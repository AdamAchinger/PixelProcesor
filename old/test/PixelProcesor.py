import os
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image
import numpy as np
import customtkinter as ctk
from datetime import datetime

# ============================================================================
# CONSTANTS
# ============================================================================
TOOL_VERSION = "5.0"

CELL_H = 85
CELL_H2 = 175
CELL_W = 180
CELL_W2 = 364

ENTRY_WIDTH = 140

APP_WIDTH = 910
APP_HEIGHT = 703

BG_COLOR = "#353535"
FG_COLOR = "#696969"
THEME = "blue"
PREVIEW_BORDER_COLOR = "black"
PREVIEW_BORDER_WIDTH = 5

S_FONT1 = ("Consolas", 14)
S_FONT = ("Consolas", 16)
M_FONT = ("Consolas", 20)
B_FONT = ("Consolas", 22)

EXTENSIONS = ["PNG", "JPG", "TIFF"]
ORIENT = ["H", "H.F", "V", "V.F"]

BASE_PATH = os.getcwd()
PREVIEW_PATH = "img/Preview_2.png"
ICON_PATH = "img/AA_icon.ico"

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

# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def create_tab_frame(master):
    """Tworzy główną strukturę ramek dla zakładki"""
    frame_master = ctk.CTkFrame(master, fg_color=FG_COLOR)
    frame_master.pack(fill=Y, expand=TRUE)

    frame_top = ctk.CTkFrame(frame_master)
    frame_top.pack(padx=2, pady=2)

    left_tab_frame = ctk.CTkFrame(frame_top, width=500, fg_color=PREVIEW_BORDER_COLOR)
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
        Logger().log(f"Invalid {param_name} format: {str(e)}. Expected: R,G,B,A", "ERROR")
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


# ============================================================================
# SOLID COLOR CLASS
# ============================================================================

class SolidColorTab:
    def __init__(self, master):
        self.img = load_preview_image()
        self.output_path = None  # brak automatycznego outputu

        left_tab_frame, frame_top, frame_scroll, frame_bottom = create_tab_frame(master)

        # Frames for inputs
        frame1 = ctk.CTkFrame(frame_scroll)
        frame1.pack()
        frame2 = ctk.CTkFrame(frame_scroll)
        frame2.pack()
        frame3 = ctk.CTkFrame(frame_scroll)
        frame3.pack(padx=1, side=LEFT)

        frame01 = ctk.CTkFrame(frame1, width=CELL_W2, height=CELL_H2)
        frame01.pack(padx=2, pady=2, side=LEFT)
        frame01.propagate(False)

        frame02 = ctk.CTkFrame(frame2, width=CELL_W, height=CELL_H)
        frame02.pack(padx=2, pady=2, side=LEFT)
        frame02.propagate(False)

        frame03 = ctk.CTkFrame(frame2, width=CELL_W, height=CELL_H)
        frame03.pack(padx=2, pady=2, side=LEFT)
        frame03.propagate(False)

        frame04 = ctk.CTkFrame(frame3, width=CELL_W, height=CELL_H)
        frame04.pack(padx=2, pady=2, side=LEFT)
        frame04.propagate(False)

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

        # Color sliders
        label_color = ctk.CTkLabel(frame01, text="Color (RGBA)", font=M_FONT)
        label_color.pack(pady=6, padx=16)

        self.slider_red = create_slider(frame01, "Red", False)
        self.slider_green = create_slider(frame01, "Green", False)
        self.slider_blue = create_slider(frame01, "Blue", False)
        self.slider_alpha = create_slider(frame01, "Alpha", True)

        # Filename
        label_filename = ctk.CTkLabel(frame02, text="File Name", font=M_FONT)
        label_filename.pack(pady=6, padx=16)

        self.input_filename = ctk.CTkEntry(frame02, width=ENTRY_WIDTH, font=M_FONT)
        self.input_filename.pack(pady=6, padx=16)
        self.input_filename.insert(0, "T_SolidColor")

        # Size
        label_size = ctk.CTkLabel(frame03, text="Size", font=M_FONT)
        label_size.pack(pady=6, padx=16)

        self.input_size_width = ctk.CTkEntry(frame03, width=ENTRY_WIDTH/2, font=M_FONT)
        self.input_size_width.pack(pady=6, padx=8, side=LEFT)
        self.input_size_width.insert(0, "512")

        label_x = ctk.CTkLabel(frame03, text="x", font=M_FONT)
        label_x.pack(pady=6, padx=0, side=LEFT)

        self.input_size_height = ctk.CTkEntry(frame03, width=ENTRY_WIDTH/2, font=M_FONT)
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

    def create_preview(self, master):
        preview_image = ctk.CTkImage(light_image=self.img, size=(480, 480))
        self.preview_label = ctk.CTkLabel(master, image=preview_image, text='')
        self.preview_label.pack(pady=PREVIEW_BORDER_WIDTH, padx=PREVIEW_BORDER_WIDTH)

    def update_preview(self):
        img_preview = ctk.CTkImage(light_image=self.img, size=(480, 480))
        self.preview_label.configure(image=img_preview)
        self.preview_label.image = img_preview

    def create_output_dir(self, master):
        label_out = ctk.CTkLabel(master, text="Output:", font=S_FONT)
        label_out.pack(pady=2, padx=6, side=LEFT)

        # ✅ (Not set) jest czerwone
        self.label_path = ctk.CTkLabel(
            master,
            text="(Not set)",
            font=S_FONT,
            text_color="red"
        )
        self.label_path.pack(pady=2, padx=6, side=LEFT)

        # ✅ Rigid button (nie skaluje się)
        button = ctk.CTkButton(
            master,
            text="Set Output",
            width=110,
            height=30,
            command=self.set_output_dir,
            font=S_FONT
        )
        button.pack(padx=6, pady=2, side=RIGHT)
        button.pack_propagate(False)  # Zapobiega zmianie rozmiaru

    def set_output_dir(self):
        directory = filedialog.askdirectory(title="Select Output Directory")
        if directory:
            self.output_path = directory
            self.label_path.configure(text=self.output_path, text_color="white")  # ✅ biały po ustawieniu
            Logger().log(f"Output directory set: {directory}", "INFO")
        else:
            self.output_path = None
            self.label_path.configure(text="(Not set)", text_color="red")
            Logger().log("Output directory not selected.", "WARN")

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

    def generate(self):
        try:
            r = self.slider_red.get()
            g = self.slider_green.get()
            b = self.slider_blue.get()
            a = self.slider_alpha.get()

            filetype = self.filetype.get().lower()
            width = int(self.input_size_width.get())
            height = int(self.input_size_height.get())

            if filetype == "jpg":
                color = (int(r * 255), int(g * 255), int(b * 255))
                self.img = Image.new("RGB", (width, height), color)
            else:
                color = (int(r * 255), int(g * 255), int(b * 255), int(a * 255))
                self.img = Image.new("RGBA", (width, height), color)

            self.export_button.configure(state=NORMAL)
            self.update_preview()
            Logger().log("Solid color image generated successfully!", "SUCCESS")

        except Exception as e:
            Logger().log(f"Failed to generate: {e}", "ERROR")

    def export(self):
        try:
            full_path = self.refresh_path()
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            self.img.save(full_path)
            Logger().log(f"Image saved to: {full_path}", "SUCCESS")
        except Exception as e:
            Logger().log(f"Failed to save: {e}", "ERROR")



# ============================================================================
# GRADIENT CLASS
# ============================================================================

class GradientTab:
    def __init__(self, master):
        self.img = load_preview_image()
        self.output_path = BASE_PATH

        left_tab_frame, frame_top, frame_scroll, frame_bottom = create_tab_frame(master)

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
        self.export_button = ctk.CTkButton(frame_bottom, text="Export", width=198, height=40,
                                          state=DISABLED, command=self.export, font=B_FONT)
        self.export_button.pack(pady=2, padx=2, side=RIGHT)

        generate_button = ctk.CTkButton(frame_bottom, text="Generate", width=198, height=40,
                                       command=self.generate, font=B_FONT)
        generate_button.pack(pady=2, padx=2, side=RIGHT)

        # Color A
        label_color_a = ctk.CTkLabel(frame01, text="Color A (RGBA)", font=M_FONT)
        label_color_a.pack(pady=6, padx=16)

        self.a_slider_red = create_slider(frame01, "Red", False, 1.0)
        self.a_slider_green = create_slider(frame01, "Green", False, 1.0)
        self.a_slider_blue = create_slider(frame01, "Blue", False, 1.0)
        self.a_slider_alpha = create_slider(frame01, "Alpha", True)

        # Color B
        label_color_b = ctk.CTkLabel(frame011, text="Color B (RGBA)", font=M_FONT)
        label_color_b.pack(pady=6, padx=16)

        self.b_slider_red = create_slider(frame011, "Red", False, 0.0)
        self.b_slider_green = create_slider(frame011, "Green", False, 0.0)
        self.b_slider_blue = create_slider(frame011, "Blue", False, 0.0)
        self.b_slider_alpha = create_slider(frame011, "Alpha", True)

        # Filename
        label_filename = ctk.CTkLabel(frame02, text="File Name", font=M_FONT)
        label_filename.pack(pady=6, padx=16)

        self.input_filename = ctk.CTkEntry(frame02, width=ENTRY_WIDTH, font=M_FONT)
        self.input_filename.pack(pady=6, padx=16)
        self.input_filename.insert(0, "T_Gradient")

        # Size
        label_size = ctk.CTkLabel(frame03, text="Size", font=M_FONT)
        label_size.pack(pady=6, padx=16)

        self.input_size_width = ctk.CTkEntry(frame03, width=ENTRY_WIDTH/2, font=M_FONT)
        self.input_size_width.pack(pady=6, padx=8, side=LEFT)
        self.input_size_width.insert(0, "512")

        label_x = ctk.CTkLabel(frame03, text="x", font=M_FONT)
        label_x.pack(pady=6, padx=0, side=LEFT)

        self.input_size_height = ctk.CTkEntry(frame03, width=ENTRY_WIDTH/2, font=M_FONT)
        self.input_size_height.pack(pady=6, padx=8, side=LEFT)
        self.input_size_height.insert(0, "512")

        # File type
        label_filetype = ctk.CTkLabel(frame04, text="File Type", font=M_FONT)
        label_filetype.pack(pady=6, padx=16)

        self.filetype = ctk.StringVar()
        self.filetype.set(EXTENSIONS[0])
        self.input_filetype = ctk.CTkSegmentedButton(frame04, width=250, variable=self.filetype,
                                                     values=EXTENSIONS, font=S_FONT)
        self.input_filetype.pack(pady=6, padx=16)

        # Orient
        label_orient = ctk.CTkLabel(frame05, text="Orient", font=M_FONT)
        label_orient.pack(pady=6, padx=16)

        self.input_orient = ctk.StringVar()
        self.input_orient.set(ORIENT[0])
        orient_btn = ctk.CTkSegmentedButton(frame05, width=250, variable=self.input_orient,
                                           values=ORIENT, font=S_FONT)
        orient_btn.pack(pady=6, padx=16)

    def create_preview(self, master):
        preview_image = ctk.CTkImage(light_image=self.img, size=(480, 480))
        self.preview_label = ctk.CTkLabel(master, image=preview_image, text='')
        self.preview_label.pack(pady=PREVIEW_BORDER_WIDTH, padx=PREVIEW_BORDER_WIDTH)

    def update_preview(self):
        img_preview = ctk.CTkImage(light_image=self.img, size=(480, 480))
        self.preview_label.configure(image=img_preview)
        self.preview_label.image = img_preview

    def create_output_dir(self, master):
        label_out = ctk.CTkLabel(master, text="Output:", font=S_FONT)
        label_out.pack(pady=2, padx=6, side=LEFT)

        self.label_path = ctk.CTkLabel(master, text=self.output_path, font=S_FONT)
        self.label_path.pack(pady=2, padx=6, side=LEFT)

        button = ctk.CTkButton(master, text="Set Output", width=100,
                              command=self.set_output_dir, font=S_FONT)
        button.pack(pady=2, padx=2, side=RIGHT)

    def set_output_dir(self):
        directory = filedialog.askdirectory(title="Output Directory")
        if directory:
            self.output_path = directory
            self.label_path.configure(text=self.output_path)
            Logger().log(f"Output directory set: {directory}", "INFO")

    def generate(self):
        try:
            filename = self.input_filename.get()
            filetype = self.filetype.get().lower()
            orient = self.input_orient.get()
            width = int(self.input_size_width.get())
            height = int(self.input_size_height.get())

            r1 = self.a_slider_red.get()
            g1 = self.a_slider_green.get()
            b1 = self.a_slider_blue.get()
            a1 = self.a_slider_alpha.get()
            
            r2 = self.b_slider_red.get()
            g2 = self.b_slider_green.get()
            b2 = self.b_slider_blue.get()
            a2 = self.b_slider_alpha.get()

            # Create gradient using numpy (MUCH faster)
            if orient in ["H", "H.F"]:
                gradient = np.linspace(0, 1, height)[:, np.newaxis]
                gradient = np.tile(gradient, (1, width))
            else:
                gradient = np.linspace(0, 1, width)[np.newaxis, :]
                gradient = np.tile(gradient, (height, 1))

            if orient in ["H.F", "V.F"]:
                gradient = 1 - gradient

            # Vectorized color interpolation
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

            # Add extension if not present
            if not filename.endswith(f".{filetype}"):
                filename = filename + "." + filetype
            
            self.full_path = os.path.join(self.output_path, filename)
            self.export_button.configure(state=NORMAL)
            self.update_preview()
            Logger().log("Gradient generated successfully!", "SUCCESS")

        except Exception as e:
            Logger().log(f"Failed to generate: {str(e)}", "ERROR")

    def export(self):
        try:
            self.img.save(self.full_path)
            Logger().log(f"Image saved to: {self.full_path}", "SUCCESS")
        except Exception as e:
            Logger().log(f"Failed to save: {str(e)}", "ERROR")


# ============================================================================
# MATH CLASS
# ============================================================================

class MathTab:
    def __init__(self, master):
        self.img = load_preview_image()
        self.input_file = ""
        self.output_file = ""

        left_tab_frame, frame_top, frame_scroll, frame_bottom = create_tab_frame(master)

        # Frames
        frame1 = ctk.CTkFrame(frame_scroll)
        frame1.pack()
        frame2 = ctk.CTkFrame(frame_scroll)
        frame2.pack()
        frame3 = ctk.CTkFrame(frame_scroll)
        frame3.pack(padx=1, side=LEFT)

        frame01 = ctk.CTkFrame(frame1, width=CELL_W, height=CELL_H)
        frame01.pack(padx=2, pady=2, side=LEFT)
        frame01.propagate(False)

        frame02 = ctk.CTkFrame(frame1, width=CELL_W, height=CELL_H)
        frame02.pack(padx=2, pady=2, side=LEFT)
        frame02.propagate(False)

        frame03 = ctk.CTkFrame(frame2, width=CELL_W, height=CELL_H)
        frame03.pack(padx=2, pady=2, side=LEFT)
        frame03.propagate(False)

        frame04 = ctk.CTkFrame(frame2, width=CELL_W, height=CELL_H)
        frame04.pack(padx=2, pady=2, side=LEFT)
        frame04.propagate(False)

        frame05 = ctk.CTkFrame(frame3, width=CELL_W, height=CELL_H)
        frame05.pack(padx=2, pady=2, side=LEFT)
        frame05.propagate(False)

        frame06 = ctk.CTkFrame(frame3, width=CELL_W, height=CELL_H)
        frame06.pack(padx=2, pady=2, side=LEFT)
        frame06.propagate(False)

        frame08 = ctk.CTkFrame(frame_top, width=400, height=30)
        frame08.pack(padx=2, pady=1)
        frame08.propagate(False)

        frame09 = ctk.CTkFrame(frame_top, width=400, height=30)
        frame09.pack(padx=2, pady=1)
        frame09.propagate(False)

        # Preview
        self.create_preview(left_tab_frame)

        # Input/Output files
        self.create_input_file(frame08)
        self.create_output_file(frame09)

        # Buttons
        self.export_button = ctk.CTkButton(frame_bottom, text="Export", width=198, height=40,
                                          state=DISABLED, command=self.export, font=B_FONT)
        self.export_button.pack(pady=2, padx=2, side=RIGHT)

        generate_button = ctk.CTkButton(frame_bottom, text="Generate", width=198, height=40,
                                       command=self.generate, font=B_FONT)
        generate_button.pack(pady=2, padx=2, side=RIGHT)

        # Math operations
        label_multiply = ctk.CTkLabel(frame01, text="MULTIPLY", font=M_FONT)
        label_multiply.pack(pady=6, padx=16)
        self.input_multiply = ctk.CTkEntry(frame01, width=128, font=S_FONT)
        self.input_multiply.pack(pady=6, padx=16)
        self.input_multiply.insert(0, "1,1,1,1")

        label_power = ctk.CTkLabel(frame02, text="POWER", font=M_FONT)
        label_power.pack(pady=6, padx=16)
        self.input_power = ctk.CTkEntry(frame02, width=128, font=S_FONT)
        self.input_power.pack(pady=6, padx=16)
        self.input_power.insert(0, "1,1,1,1")

        label_add = ctk.CTkLabel(frame03, text="ADD", font=M_FONT)
        label_add.pack(pady=6, padx=16)
        self.input_add = ctk.CTkEntry(frame03, width=128, font=S_FONT)
        self.input_add.pack(pady=6, padx=16)
        self.input_add.insert(0, "0,0,0,0")

        label_subtract = ctk.CTkLabel(frame04, text="SUBTRACT", font=M_FONT)
        label_subtract.pack(pady=6, padx=16)
        self.input_subtract = ctk.CTkEntry(frame04, width=128, font=S_FONT)
        self.input_subtract.pack(pady=6, padx=16)
        self.input_subtract.insert(0, "0,0,0,0")

        label_max = ctk.CTkLabel(frame05, text="MAX", font=M_FONT)
        label_max.pack(pady=6, padx=16)
        self.input_max = ctk.CTkEntry(frame05, width=128, font=S_FONT)
        self.input_max.pack(pady=6, padx=16)
        self.input_max.insert(0, "1,1,1,1")

        label_min = ctk.CTkLabel(frame06, text="MIN", font=M_FONT)
        label_min.pack(pady=6, padx=16)
        self.input_min = ctk.CTkEntry(frame06, width=128, font=S_FONT)
        self.input_min.pack(pady=6, padx=16)
        self.input_min.insert(0, "0,0,0,0")

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

        self.label_input = ctk.CTkLabel(master, text="(Not set)", text_color="red", font=S_FONT)
        self.label_input.pack(pady=2, padx=6, side=LEFT)

        button = ctk.CTkButton(master, text="Set Input", width=100,
                              command=self.set_input_file, font=S_FONT)
        button.pack(pady=2, padx=2, side=RIGHT)

    def create_output_file(self, master):
        label_out = ctk.CTkLabel(master, text="Output:", font=S_FONT)
        label_out.pack(pady=2, padx=6, side=LEFT)

        self.label_output = ctk.CTkLabel(master, text="(Not set)", text_color="red", font=S_FONT)
        self.label_output.pack(pady=2, padx=6, side=LEFT)

        button = ctk.CTkButton(master, text="Set Output", width=100,
                              command=self.set_output_file, font=S_FONT)
        button.pack(pady=2, padx=2, side=RIGHT)

    def set_input_file(self):
        file = filedialog.askopenfilename(title="Select Input File")
        if file:
            self.input_file = file
            filename = os.path.basename(file)
            self.label_input.configure(text=filename, text_color="white")
            try:
                self.img = Image.open(file)
                self.update_preview()
                Logger().log(f"Input file loaded: {filename}", "INFO")
            except Exception as e:
                Logger().log(f"Failed to open image: {str(e)}", "ERROR")

    def set_output_file(self):
        file = filedialog.asksaveasfilename(
            title="Select Output File",
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("TIFF files", "*.tiff"), ("JPEG files", "*.jpg"), ("All files", "*.*")]
        )
        if file:
            self.output_file = file
            filename = os.path.basename(file)
            self.label_output.configure(text=filename, text_color="white")
            Logger().log(f"Output file set: {filename}", "INFO")

    def generate(self):
        try:
            if not self.input_file or not os.path.exists(self.input_file):
                Logger().log("Please select an input file first", "WARNING")
                return

            if not self.output_file:
                Logger().log("Please select an output file first", "WARNING")
                return

            # Parse all input values
            multiply = parse_rgba_values(self.input_multiply.get(), "Multiply")
            power = parse_rgba_values(self.input_power.get(), "Power")
            add = parse_rgba_values(self.input_add.get(), "Add")
            subtract = parse_rgba_values(self.input_subtract.get(), "Subtract")
            min_vals = parse_rgba_values(self.input_min.get(), "Min")
            max_vals = parse_rgba_values(self.input_max.get(), "Max")

            if None in [multiply, power, add, subtract, min_vals, max_vals]:
                return

            # Open image and convert to numpy array
            img_input = Image.open(self.input_file).convert("RGBA")
            img_array = np.array(img_input, dtype=np.float32)

            # Apply operations using numpy (very fast!)
            img_array *= np.array(multiply)
            img_array = np.power(img_array, np.array(power))
            img_array += np.array(add) * 255
            img_array -= np.array(subtract) * 255

            # Clamp to min/max
            min_array = np.array(min_vals) * 255
            max_array = np.array(max_vals) * 255
            img_array = np.clip(img_array, min_array, max_array)

            # Convert back to image
            img_array = np.clip(img_array, 0, 255).astype(np.uint8)
            self.img = Image.fromarray(img_array, mode='RGBA')

            self.export_button.configure(state=NORMAL)
            self.update_preview()
            Logger().log("Image processed successfully!", "SUCCESS")

        except Exception as e:
            Logger().log(f"Failed to process: {str(e)}", "ERROR")

    def export(self):
        try:
            self.img.save(self.output_file)
            Logger().log(f"Image saved to: {self.output_file}", "SUCCESS")
        except Exception as e:
            Logger().log(f"Failed to save: {str(e)}", "ERROR")


# ============================================================================
# SEPARATE CHANNELS CLASS
# ============================================================================

class SeparateTab:
    def __init__(self, master):
        self.img = load_preview_image()
        self.input_file = ""
        self.output_red = ""
        self.output_green = ""
        self.output_blue = ""
        self.output_alpha = ""

        left_tab_frame, frame_top, frame_scroll, frame_bottom = create_tab_frame(master)

        # Input frame
        frame08 = ctk.CTkFrame(frame_top, width=400, height=30)
        frame08.pack(padx=2, pady=1)
        frame08.propagate(False)

        # Channel frames
        frame1 = ctk.CTkFrame(frame_scroll)
        frame1.pack()
        frame01 = ctk.CTkFrame(frame1, width=CELL_W2, height=CELL_H)
        frame01.pack(padx=2, pady=2, side=LEFT)
        frame01.propagate(False)

        frame2 = ctk.CTkFrame(frame_scroll)
        frame2.pack()
        frame02 = ctk.CTkFrame(frame2, width=CELL_W2, height=CELL_H)
        frame02.pack(padx=2, pady=2, side=LEFT)
        frame02.propagate(False)

        frame3 = ctk.CTkFrame(frame_scroll)
        frame3.pack()
        frame03 = ctk.CTkFrame(frame3, width=CELL_W2, height=CELL_H)
        frame03.pack(padx=2, pady=2, side=LEFT)
        frame03.propagate(False)

        frame4 = ctk.CTkFrame(frame_scroll)
        frame4.pack()
        frame04 = ctk.CTkFrame(frame4, width=CELL_W2, height=CELL_H)
        frame04.pack(padx=2, pady=2, side=LEFT)
        frame04.propagate(False)

        # Preview (4 channels)
        self.create_preview_4(left_tab_frame)

        # Input file selector
        label_in = ctk.CTkLabel(frame08, text="Input:", width=32, font=S_FONT)
        label_in.pack(pady=2, padx=6, side=LEFT)

        self.label_input = ctk.CTkLabel(frame08, text="(Not set)", text_color="red", font=S_FONT)
        self.label_input.pack(pady=2, padx=6, side=LEFT)

        button_in = ctk.CTkButton(frame08, text="Set Input", width=100,
                                 command=self.set_input_file, font=S_FONT)
        button_in.pack(pady=2, padx=2, side=RIGHT)

        # Generate button
        generate_button = ctk.CTkButton(frame_bottom, text="Separate", width=400, height=40,
                                       command=self.generate, font=B_FONT)
        generate_button.pack(pady=2, padx=2, side=RIGHT)

        # Red channel
        frame011 = ctk.CTkFrame(frame01, width=400, height=40)
        frame011.pack(padx=2, pady=1, fill=X, expand=TRUE)
        frame012 = ctk.CTkFrame(frame01, width=400, height=40)
        frame012.pack(padx=2, pady=1, fill=X, expand=TRUE)

        label_red = ctk.CTkLabel(frame011, text="Red Channel", font=M_FONT)
        label_red.pack(pady=6, padx=12, side=LEFT)

        button_red = ctk.CTkButton(frame011, text="Set Red", width=100,
                                  command=self.set_red_channel, font=S_FONT)
        button_red.pack(pady=2, padx=2, side=RIGHT)

        label_out_red = ctk.CTkLabel(frame012, text="Output:", font=S_FONT)
        label_out_red.pack(pady=2, padx=6, side=LEFT)

        self.label_red = ctk.CTkLabel(frame012, text="(Not set)", text_color="red", font=S_FONT)
        self.label_red.pack(pady=2, padx=6, side=LEFT)

        # Green channel
        frame021 = ctk.CTkFrame(frame02, width=400, height=40)
        frame021.pack(padx=2, pady=1, fill=X, expand=TRUE)
        frame022 = ctk.CTkFrame(frame02, width=400, height=40)
        frame022.pack(padx=2, pady=1, fill=X, expand=TRUE)

        label_green = ctk.CTkLabel(frame021, text="Green Channel", font=M_FONT)
        label_green.pack(pady=6, padx=12, side=LEFT)

        button_green = ctk.CTkButton(frame021, text="Set Green", width=100,
                                    command=self.set_green_channel, font=S_FONT)
        button_green.pack(pady=2, padx=2, side=RIGHT)

        label_out_green = ctk.CTkLabel(frame022, text="Output:", font=S_FONT)
        label_out_green.pack(pady=2, padx=6, side=LEFT)

        self.label_green = ctk.CTkLabel(frame022, text="(Not set)", text_color="red", font=S_FONT)
        self.label_green.pack(pady=2, padx=6, side=LEFT)

        # Blue channel
        frame031 = ctk.CTkFrame(frame03, width=400, height=40)
        frame031.pack(padx=2, pady=1, fill=X, expand=TRUE)
        frame032 = ctk.CTkFrame(frame03, width=400, height=40)
        frame032.pack(padx=2, pady=1, fill=X, expand=TRUE)

        label_blue = ctk.CTkLabel(frame031, text="Blue Channel", font=M_FONT)
        label_blue.pack(pady=6, padx=12, side=LEFT)

        button_blue = ctk.CTkButton(frame031, text="Set Blue", width=100,
                                   command=self.set_blue_channel, font=S_FONT)
        button_blue.pack(pady=2, padx=2, side=RIGHT)

        label_out_blue = ctk.CTkLabel(frame032, text="Output:", font=S_FONT)
        label_out_blue.pack(pady=2, padx=6, side=LEFT)

        self.label_blue = ctk.CTkLabel(frame032, text="(Not set)", text_color="red", font=S_FONT)
        self.label_blue.pack(pady=2, padx=6, side=LEFT)

        # Alpha channel
        frame041 = ctk.CTkFrame(frame04, width=400, height=40)
        frame041.pack(padx=2, pady=1, fill=X, expand=TRUE)
        frame042 = ctk.CTkFrame(frame04, width=400, height=40)
        frame042.pack(padx=2, pady=1, fill=X, expand=TRUE)

        label_alpha = ctk.CTkLabel(frame041, text="Alpha Channel", font=M_FONT)
        label_alpha.pack(pady=6, padx=16, side=LEFT)

        button_alpha = ctk.CTkButton(frame041, text="Set Alpha", width=100,
                                    command=self.set_alpha_channel, font=S_FONT)
        button_alpha.pack(pady=2, padx=2, side=RIGHT)

        label_out_alpha = ctk.CTkLabel(frame042, text="Output:", font=S_FONT)
        label_out_alpha.pack(pady=2, padx=6, side=LEFT)

        self.label_alpha = ctk.CTkLabel(frame042, text="(Not set)", text_color="red", font=S_FONT)
        self.label_alpha.pack(pady=2, padx=6, side=LEFT)

    def create_preview_4(self, master):
        # Load preview image or create gray channels
        try:
            if os.path.exists(PREVIEW_PATH):
                preview_img = Image.open(PREVIEW_PATH).convert("RGBA")
                channels = list(preview_img.split())
            else:
                channels = [Image.new("L", (240, 240), 128) for _ in range(4)]
        except:
            channels = [Image.new("L", (240, 240), 128) for _ in range(4)]
        
        size = (236, 236)

        frame = ctk.CTkFrame(master)
        frame.pack(pady=PREVIEW_BORDER_WIDTH, padx=PREVIEW_BORDER_WIDTH)

        self.preview_labels = []

        # Row 1
        row1 = ctk.CTkFrame(frame)
        row1.pack(side="top")

        for i in range(2):
            img = ctk.CTkImage(light_image=channels[i], size=size)
            lbl = ctk.CTkLabel(row1, image=img, text='')
            lbl.image = img
            lbl.pack(side="left", padx=2, pady=2)
            self.preview_labels.append(lbl)

        # Row 2
        row2 = ctk.CTkFrame(frame)
        row2.pack(side="top")

        for i in range(2, 4):
            img = ctk.CTkImage(light_image=channels[i], size=size)
            lbl = ctk.CTkLabel(row2, image=img, text='')
            lbl.image = img
            lbl.pack(side="left", padx=2, pady=2)
            self.preview_labels.append(lbl)

    def update_preview(self):
        if hasattr(self, 'img') and self.img:
            channels = list(self.img.split())
            size = (236, 236)

            # Fill missing channels with black
            while len(channels) < 4:
                channels.append(Image.new("L", self.img.size, 0))

            for i, label in enumerate(self.preview_labels):
                img = ctk.CTkImage(light_image=channels[i], size=size)
                label.configure(image=img)
                label.image = img

    def set_input_file(self):
        file = filedialog.askopenfilename(title="Select Input File")
        if file:
            self.input_file = file
            filename = os.path.basename(file)
            self.label_input.configure(text=filename, text_color="white")
            try:
                self.img = Image.open(file).convert("RGBA")
                self.update_preview()
                Logger().log(f"Input file loaded: {filename}", "INFO")
            except Exception as e:
                Logger().log(f"Failed to open: {str(e)}", "ERROR")

    def set_red_channel(self):
        file = filedialog.asksaveasfilename(
            title="Output Red Channel",
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("TIFF files", "*.tiff"), ("All files", "*.*")]
        )
        if file:
            self.output_red = file
            self.label_red.configure(text=os.path.basename(file), text_color="white")

    def set_green_channel(self):
        file = filedialog.asksaveasfilename(
            title="Output Green Channel",
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("TIFF files", "*.tiff"), ("All files", "*.*")]
        )
        if file:
            self.output_green = file
            self.label_green.configure(text=os.path.basename(file), text_color="white")

    def set_blue_channel(self):
        file = filedialog.asksaveasfilename(
            title="Output Blue Channel",
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("TIFF files", "*.tiff"), ("All files", "*.*")]
        )
        if file:
            self.output_blue = file
            self.label_blue.configure(text=os.path.basename(file), text_color="white")

    def set_alpha_channel(self):
        file = filedialog.asksaveasfilename(
            title="Output Alpha Channel",
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("TIFF files", "*.tiff"), ("All files", "*.*")]
        )
        if file:
            self.output_alpha = file
            self.label_alpha.configure(text=os.path.basename(file), text_color="white")

    def generate(self):
        try:
            if not self.input_file or not os.path.exists(self.input_file):
                Logger().log("Please select an input file", "WARNING")
                return

            img_input = Image.open(self.input_file)
            if img_input.mode != 'RGBA':
                img_input = img_input.convert('RGBA')

            r, g, b, a = img_input.split()

            saved_count = 0
            if self.output_red:
                r.save(self.output_red)
                saved_count += 1

            if self.output_green:
                g.save(self.output_green)
                saved_count += 1

            if self.output_blue:
                b.save(self.output_blue)
                saved_count += 1

            if self.output_alpha:
                a.save(self.output_alpha)
                saved_count += 1

            if saved_count > 0:
                Logger().log(f"Saved {saved_count} channel(s) successfully!", "SUCCESS")
            else:
                Logger().log("No output files selected", "WARNING")

        except Exception as e:
            Logger().log(f"Failed to separate: {str(e)}", "ERROR")


# ============================================================================
# MAIN APPLICATION
# ============================================================================

def main():
    # Initialize window
    root = ctk.CTk()
    ctk.set_default_color_theme(THEME)
    root.configure(bg=BG_COLOR)
    root.title(f"Pixel Processor {TOOL_VERSION}")
    
    # Try to set icon, but don't fail if it doesn't exist
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
    tab4 = tab_view.add("Separate")

    # Style tabs
    my_font = ctk.CTkFont(size=18)
    for button in tab_view._segmented_button._buttons_dict.values():
        button.configure(height=32, font=my_font)

    # Initialize tabs
    solid_tab = SolidColorTab(tab1)
    gradient_tab = GradientTab(tab2)
    math_tab = MathTab(tab3)
    separate_tab = SeparateTab(tab4)

    # Log section at the bottom
    log_frame = ctk.CTkFrame(main_frame, height=100)
    log_frame.pack(fill="x", padx=5, pady=5, side="bottom")
    log_frame.pack_propagate(False)

    log_text = ctk.CTkTextbox(
        log_frame,
        height=70,
        font=("Consolas", 12),
        fg_color="#2b2b2b",
        state="disabled"
    )
    log_text.pack(fill="both", expand=True, padx=10, pady=5)

    # Initialize logger
    logger = Logger()
    logger.set_widget(log_text)
    logger.log("Pixel Processor started successfully.", "SUCCESS")

    root.mainloop()


if __name__ == "__main__":
    main()