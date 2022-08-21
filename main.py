from tkinter import *
import tkinter as tk

class TTT(tk.Tk):

    def __init__(self):
        super().__init__()
        self.wm_title("Tic Tac Toe Application")

        self.geometry("300x250")
        self.resizable(False, False)
