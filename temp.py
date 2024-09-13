import tkinter
import customtkinter as ctk

root = ctk.CTk()
root.geometry("200x200")

e = ctk.CTkEntry(master=root,
  text_color="green",
  font=("tahoma", 20),
  # borderwidth=5,
  # bd=5,
)
e.insert(0, "text goes here...")
e.pack()

root.mainloop()