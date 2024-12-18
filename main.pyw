from tkinter import *
import customtkinter as ctk
from module import solid, gradient, math, combine, separate, mask 
import constants as c 

#### Initialize Window ####
root = ctk.CTk()
ctk.set_default_color_theme(c.theme) 
root.configure(bg=c.bgColor)
root.title("Pixel Procesor " + str(c.toolVersion))
root.iconbitmap(c.iconPath)
root.resizable(FALSE, FALSE)
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
appXpos = int((screenWidth / 2) - (c.appWidth / 2))
appYpos = int((screenHeight / 2) - (c.appHeight / 2))
root.geometry(f'{c.appWidth}x{c.appHeight}+{appXpos}+{appYpos}')

# Create the tab view (this is the equivalent of a tabbed frame)
tab_view = ctk.CTkTabview(root)
tab_view.pack(expand=True, fill="both")

# Add tabs to the tab view
tab1 = tab_view.add("Solid Color")
tab2 = tab_view.add("Gradient")
tab3 = tab_view.add("Math")
#tab4 = tab_view.add("Separate")
#tab5 = tab_view.add("Combine")
#tab6 = tab_view.add("Mask")
#tab7 = tab_view.add("Resize")
#tab8 = tab_view.add("Color Picker")
#tab8 = tab_view.add("Filter")

my_font = ctk.CTkFont(size=18)  # Font object
for button in tab_view._segmented_button._buttons_dict.values():
    button.configure(height=32, font=my_font)  # Change font using font object



# Initialize classes within the appropriate tabs
solid_tab = solid.Solid(tab1)
gradient_tab = gradient.Gradient(tab2)
math_tab = math.Math(tab3)
#separate_tab = separate.Separate(tab4)
#combine_tab = combine.Combine(tab5)

#mask_tab = mask.Mask(tab6)


root.mainloop()
