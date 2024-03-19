from customtkinter import *

class TodoFrame(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(False, width=600, fg_color="slate gray")
        self.grid(row=0, column=1, sticky="NSEW")  # Removed rowspan and columnspan
        self.grid_columnconfigure(1, weight=1)  # Allow resizing of InputFrame


class InputFrame(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        transparent_color = "#FFFFFF"  # Adjust alpha channel value (80 in this case)
        self.configure(False, height=50, width=300, fg_color=transparent_color, bg_color="slate gray")
        self.grid(row=0, column=1, sticky="WES", padx=(50, 50), pady=(0, 40))  # Added negative padding to overlap with TodoFrame

class ListFrame(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(False, height=800, width=100)
        self.grid(row=0, column=0, sticky="WNSE")

class App(CTk):
    def __init__(self, manager) -> None:
        super().__init__()
        from manager.manager import Manager
        
        self.manager: Manager = manager
        self.geometry("800x600")
        self.title("Todo Manager")
        
        self.grid_columnconfigure(0, weight=0, minsize=250)  # Adjusted weight to 1 for resizing
        self.grid_columnconfigure(1, weight=1)  # Adjusted weight to 0
        self.grid_rowconfigure(0, weight=1)

        self.todo_frame = TodoFrame(self)
        self.input_frame = InputFrame(self)
        self.list_frame = ListFrame(self)  

