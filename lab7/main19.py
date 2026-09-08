import tkinter as tk
from model19 import LibraryModel
from view19 import LibraryView
from controller19 import LibraryController

root = tk.Tk()

model = LibraryModel()
view = LibraryView(root)
controller = LibraryController(model, view)

root.mainloop()

