from tkinter import *
from tkinter import ttk
import tkinter as tk


class ProjectFunctions:

    def __init__(self):
        pass
    
    # This function starts an event that when the user clicks on an entry field
    # the placeholder text is deleted.
    def click(self, event):
        entry_name = event.widget
        entry_name.configure(state=NORMAL)
        entry_name.delete(0, END)
        entry_name.unbind('<Button-1>',  self.clicked)
        
        
    # This function creates and opens player profile entry windown from the "Enter Profile" button on the main page.
    def player_profile_entry(self):
        player_profile_entry = Toplevel()
        player_profile_entry.title("Player Profile Entry")
        player_profile_entry.geometry("750x500")
        player_profile_entry.iconbitmap("C:\\Users\\ericj_dmnhny4\\Desktop\\Cap_ranking_Project\\Images\\vince-lombardi-football-trophy.ico")

        # get the screen dimensions
        screen_width = player_profile_entry.winfo_screenwidth()
        screen_height = player_profile_entry.winfo_screenheight()

        # calculate the position of the window
        window_width = 750
        window_height = 500
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # set the geometry of the window
        player_profile_entry.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Top level canvas definition
        ppe_canvas = Canvas(player_profile_entry, width=750, height=500)
        ppe_canvas.pack(fill= "both", expand= True)

        # Entry field widgets defined
        fname = Entry(player_profile_entry, width= 15, font=('Arial', 14))
        fname.insert(0, 'First Name')

        lname = Entry(player_profile_entry, width= 15, font=('Arial', 14))
        lname.insert(0, 'Last Name')

        current_team = Entry(player_profile_entry, width= 15, font=('Arial', 14))
        current_team.insert(0, 'Current Team')

        years_in_league = Entry(player_profile_entry, width= 15, font=('Arial', 14))
        years_in_league.insert(0, 'Years in League')

        current_salary = Entry(player_profile_entry, width= 15, font=('Arial', 14))
        current_salary.insert(0, 'Current Salary')

        # Widgets placed in the canvas
        ppe_canvas.create_window(90, 25, window= fname)

        ppe_canvas.create_window(90, 70, window= lname)

        ppe_canvas.create_window(90, 115, window=current_team)

        ppe_canvas.create_window(90, 160, window=years_in_league)
        
        ppe_canvas.create_window(90, 205, window=current_salary)


        # This is a dictionary that maps each entry widget to its corresponding click event binding.
        self.clicked =  {
            fname: fname.bind('<Button-1>', self.click),
        
            lname: lname.bind('<Button-1>', self.click),

            current_team: current_team.bind('<Button-1>', self.click),

            years_in_league: years_in_league.bind('<Button-1>', self.click),
            
            current_salary: current_salary.bind('<Button-1>', self.click),

        }

        
             
       
       




    def players_list(self):
        players_list = Toplevel()
        players_list.title("Players List")
        players_list.geometry("750x500")
        players_list.iconbitmap("C:\\Users\\ericj_dmnhny4\\Desktop\\Cap_ranking_Project\\Images\\vince-lombardi-football-trophy.ico")

        # get the screen dimensions
        screen_width = players_list.winfo_screenwidth()
        screen_height = players_list.winfo_screenheight()

        # calculate the position of the window
        window_width = 750
        window_height = 500
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # set the geometry of the window
        players_list.geometry(f"{window_width}x{window_height}+{x}+{y}")

   
class PlayerProfile:
    
    def __init__(self, fname, lname, team, years, salary, injuries, score, projected):
        self.fname = fname
        self.lname = lname
        self.team = team
        self.year =  years
        self.salary = salary
        self.injuries = injuries
        self.score  = score
        self.projected  = projected

    


