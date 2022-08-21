from tkinter import *
import tkinter as tk
from tkinter import messagebox

class TTT(tk.Tk):

    lines = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]

    def __init__(self):
        super().__init__()
        self.wm_title("Tic Tac Toe Application")

        self.geometry("300x300")
        self.resizable(False, False)
        self.btns = [] # create some type of tracking for our squares
        self.btnlist = []
        self.swap = True # swap for player turn
        self.turns = 0

        self._createEntries()

    def _createEntries(self):
        for col in range(0, 3):
            row = []
            
            for indx in range(0, 3):
                butt = Button(self, width=6, height=3, font=("Arial", 14, ""), command=lambda x=col, y=indx: self.buttonClicked(x, y))
                butt.grid(row = indx, column=col)
                row.append(butt)
                self.btnlist.append(butt)

            self.btns.append(row)
        
        Button(self, text="Restart", bg='blue', fg='white', activebackground='blue3', activeforeground='white', command=self.resetGame).grid(row=3, column=1) # Reset button

    def buttonClicked(self, x, y):
        self.turns+=1

        if self.swap:
            self.btns[x][y].config(text="X", bg='black', state="disabled")
        else:
            self.btns[x][y].config(text="O", bg='gray', state="disabled")
        
        self.check()
        self.swap = not self.swap # swap back

    def check(self):
        for line in self.lines:
            o = line[0]
            i = line[1]
            t = line[2]

            if self.btnlist[o].cget('text') != "" and self.btnlist[o].cget('text') == self.btnlist[i].cget('text') and self.btnlist[o].cget('text') == self.btnlist[t].cget('text'):
                if self.swap:
                    char = 'X'
                else:
                    char = 'O'
                
                messagebox.showinfo("Tic Tac Toe", char + " has won the game in " + str(self.turns) + " turns!")
                self.resetGame()
                return

        if self.turns >= 9:
            messagebox.showinfo("Tic Tac Toe", "The game has come to a draw.")
            self.resetGame()

    def resetGame(self):
        for button in self.btnlist:
            button.config(text="", bg="white", state="normal")
        
        self.swap = True
        self.turns = 0

TTT().mainloop()
