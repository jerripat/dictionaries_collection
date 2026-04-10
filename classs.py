
import tkinter as tk
from tkinter import ttk

def main():
    app = Application()
    app.mainloop()

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x300")
        self.title("Classes")


if __name__ == "__main__":
    main()