import tkinter as Tk
from tkinter import *
from tkinter import ttk
import pandas
from openpyxl import Workbook
from funcs import *



pf = ProjectFunctions()

# Main window initializaton and setup
main = Tk()

main.title("Free Agent Rankings")
main.geometry("1920x1080")
main.resizable(True, True)
main.iconbitmap("C:\\Users\\ericj_dmnhny4\\Desktop\\Cap_ranking_Project\\Images\\vince-lombardi-football-trophy.ico")

# Define Canvas
main_canvas = Canvas(main, width=1920, height=1080)
main_canvas.pack(fill="both", expand=True)
main_canvas.configure(bg='#516f75')
main_canvas.pack()

# get the screen dimensions
screen_width = main.winfo_screenwidth()
screen_height = main.winfo_screenheight()

# calculate the position of the window
window_width = 1920
window_height = 1080
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

# set the geometry of the window
main.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create custom TTK styles
style = ttk.Style()
style.configure('TButton', borderwidth=0, relief="groove", background="black", foreground="#2c3030", padding=10, width=50, height=50)
style.map('TButton', background=[('active', 'black')], foreground=[('active', '#06313b')])

# Define buttons
player_entry_button = ttk.Button(main, text= 'Enter Player Profile',style='TButton', command= pf.player_profile_entry)
view_players = ttk.Button(main, text= 'View Players', style='TButton', command=ProjectFunctions.players_list)

# Place buttons on canvas
main_canvas.create_window(960, 50, window=player_entry_button)
main_canvas.create_window(960, 100, window=view_players)

def on_resize(event):
    # update button size based on window size
    width = event.width // 10
    height = event.height // 20
    player_entry_button.config(width=width, height=height)

    
    view_players.config(width=width, height=height)

main.bind('<Configure>', on_resize)

main.mainloop()



