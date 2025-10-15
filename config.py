import os
import sys


TOOL_VERSION = "8.6"

CELL_H = 85
CELL_H2 = 175
CELL_W = 180
CELL_W2 = 364

ENTRY_WIDTH = 140


THEME = "dark-blue"
NOTSET_COLOR = "#FF7878"

APP_WIDTH = 910
APP_HEIGHT = 703

BG_COLOR = "#353535"
FG_COLOR = "#696969"

PREVIEW_BORDER_COLOR = "black"
PREVIEW_BORDER_WIDTH = 5


# Consolas , Roboto
S_FONT1 = ("Roboto", 14)
S_FONT = ("Roboto", 16)
M_FONT = ("Roboto", 20)
B_FONT = ("Roboto", 22)
LOG_FONT = ("Consolas", 16)


EXTENSIONS = ["PNG", "JPG", "TIFF"]
ORIENT = ["H", "H.F", "V", "V.F"]

BASE_PATH = os.getcwd()



def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


PREVIEW_PATH = resource_path("img/Preview_2.png")
ICON_PATH = resource_path("img/AA_icon.ico")

FUNCTIONS = (
f"Color • Gradient • Multiply • Exponentiation\n"
f"Addition • Subtraction • Min • Max • Invert\n"
f"Posterize • Separate • Combine\n"
            )

