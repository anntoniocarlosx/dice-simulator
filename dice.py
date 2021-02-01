"""Fun little project to get started with Tkinter"""
import tkinter as tk
import random

root = tk.Tk()

root.geometry("600x400")
root.title("Dice Rolling Simulator")

tk.Label(root, text="Roll the Dice!", font="cambria 20 italic").pack()

result = tk.IntVar()


def roll_dice():
    """Rolls the dice"""
    result.set(random.randint(1, 6))


def exit_window():
    """Pretty self-explanatory"""
    root.destroy()


tk.Label(root, font="arial 60 bold", textvariable=result).place(x=270, y=100)

tk.Button(
    root,
    font="cambria 12 bold",
    text="Roll Dice",
    width=8,
    command=roll_dice,
    bg="LimeGreen",
    padx=2,
).place(x=250, y=250)

tk.Button(
    root,
    font="cambria 12 bold",
    text="EXIT",
    widt=8,
    command=exit_window,
    bg="OrangeRed",
    padx=2,
).place(x=250, y=300)

root.mainloop()
