from sqlite3 import Row
import tkinter as tk

menu = tk.Tk()
menu.geometry('2880x1800')

# Game name
name = tk.Label(menu, text="Battleship", font=("Herculanum", 130), fg="#0f0f99")
name.pack()

# Start button
start = tk.Button(menu, text="Start", font=("Marker Felt", 20), fg="#000000", bg='#0f0f99', width=50, pady=20)
start.pack()

# Tutorial 
guide = tk.Button(menu, text="Tutorial", font=("Marker Felt", 20), fg="#000000", bg='#0f0f99', width=50, pady=20)
guide.pack()

# Exit
exit = tk.Button(menu, text="Quit", font=("Marker Felt", 20), fg="#000000", bg='#0f0f99', width=50, pady=20)
exit.pack()

menu.mainloop()