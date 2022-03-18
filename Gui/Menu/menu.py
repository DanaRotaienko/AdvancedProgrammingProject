import tkinter as tk
from tkinter import *

menu = tk.Tk()
menu.geometry('2880x1800')
menu.title("Battleship")
menu.config(bg='#fcfcd4')

# Commands

    # Popup with guidance
def info():
    popup = tk.Tk()
    popup.geometry('500x500')
    popup.title('Tutorial')
    popup.config(bg='#0f0f99')
    popup.eval('tk::PlaceWindow . center')
    rules = tk.Label(popup, font=('Open Sans', 20), text='', justify=LEFT, bg='#0f0f99', fg='#ffffff')
    rulesArr = ["1. Place your ships on a board;\n", "2. Choose a cell to strike enemy's ship;\n", "3. Who strikes all ships first wins.\n"]
    for r in rulesArr:
        rules.config(text=(rules['text']+r))
    rules.grid(row=2, column=4)
    rules.pack()
    back = tk.Button(popup, text="Back", command=popup.destroy, highlightbackground='#0f0f99')
    back.pack()

    #To quit programm
def quit():
    menu.destroy()
# Game name
name = tk.Label(menu, text="Battleship", font=("Herculanum", 130), fg="#0f0f99", bg='#fcfcd4')
name.pack()

# Start button
start = tk.Button(menu, text="Start", font=("Marker Felt", 20), fg="#ffffff", bg='#0f0f99', width=50, pady=20, highlightbackground='#fcfcd4')
start.pack()

# Tutorial 
guide = tk.Button(menu, text="Tutorial", font=("Marker Felt", 20), fg="#ffffff", bg='#0f0f99', width=50, pady=20, command=info, highlightbackground='#fcfcd4')
guide.pack()

# Exit
exit = tk.Button(menu, text="Quit", font=("Marker Felt", 20), fg="#ffffff", bg='#0f0f99', width=50, pady=20, command=quit, highlightbackground='#fcfcd4')
exit.pack()

menu.mainloop()