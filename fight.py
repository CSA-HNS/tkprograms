"""
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>

This is a fighting program where a card is picked on right and left side and they fight each other
Wins and losses are counted
Version .1
Author: Hanzala Siddiqui
"""

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

global caw
global imw
global cal
global iml
caw = 0
imw = 0
cal = 0
iml = 0

class Moves:
    def __init__(self, name, attack, defense, health):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.health = health
        self.total = attack + defense + health


# Left side characters
Punch = Moves("Punch", 42, 50, 80)
Shield = Moves("Shield", 15, 54, 100)
Kick = Moves("Kick", 60, 35, 80)
# Both sides have totals of 165 168 and 175
# Right side characters
Exoskeleton = Moves("Exoskeleton", 12, 97, 83)
Missiles = Moves("Missiles", 55, 17, 90)
Rocket = Moves("Rocket", 73, 28, 88)

left_characters = {
    "Punch": Moves("Punch", 42, 50, 80),
    "Shield": Moves("Shield", 15, 54, 100),
    "Kick": Moves("Kick", 60, 35, 80),
}

right_characters = {
    "Exoskeleton": Moves("Exoskeleton", 12, 97, 83),
    "Missiles": Moves("Missiles", 55, 17, 90),
    "Rocket": Moves("Rocket", 73, 28, 88),
}

leftnames = list(left_characters.keys())
rightnames = list(right_characters.keys())


def about():  # Function that opens messagebox and shows version info and program name
    messagebox.showinfo("Version", "Fighting Game\nVersion .1")


def statDisplay1(*args):  # Displays stats for characters in left box
    idxs = lbox.curselection()[0]
    saveattack = 0
    savedefense = 0

    savehealth = 0
    savename = ""
    if idxs == 0:
        savename = "Punch"
        saveattack = Punch.attack
        savedefense = Punch.defense
        savehealth = Punch.health
    elif idxs == 1:
        savename = "Shield"
        saveattack = Shield.attack
        savedefense = Shield.defense
        savehealth = Shield.health
    elif idxs == 2:
        savename = "Kick"
        saveattack = Kick.attack
        savedefense = Kick.defense
        savehealth = Kick.health
    statusmsg1.set(
        savename + "\nAttack: " + str(saveattack) + "\nDefense: " + str(savedefense) + "\nHealth: " + str(savehealth))


def statDisplay2(*args):  # Displays stats for characters in right box
    idxs = rbox.curselection()[0]
    saveattack = 0
    savedefense = 0
    savehealth = 0
    savename = ""
    if idxs == 0:
        savename = "Exoskeleton"
        saveattack = Exoskeleton.attack
        savedefense = Exoskeleton.defense
        savehealth = Exoskeleton.health
    elif idxs == 1:
        savename = "Missiles"
        saveattack = Missiles.attack
        savedefense = Missiles.defense
        savehealth = Missiles.health
    elif idxs == 2:
        savename = "Rocket"
        saveattack = Rocket.attack
        savedefense = Rocket.defense
        savehealth = Rocket.health
    statusmsg2.set(
        savename + "\nAttack: " + str(saveattack) + "\nDefense: " + str(savedefense) + "\nHealth: " + str(savehealth))


def fight():  # Part of code that checks for wins and loss checks which has greater total stats and deletes from list box
    global caw
    global imw
    global cal
    global iml

    try:
        wins.set("Wins:")
        loss.set("Losses:")
        namel = lbox.get(lbox.curselection()[0])
        namer = rbox.get(rbox.curselection()[0])

        totalleft = left_characters[namel].total
        totalright = right_characters[namer].total


        if totalleft > totalright:  # Checks if won or lost]
            caw+=1
            iml+=1
            wins.set(wins.get() + "\n" + "Captain America:"+str(caw) + "\n" + "Iron Man:"+str(imw))
            loss.set(loss.get() + "\n"+"Captain America:"+str(cal) +"\n"+ "Iron Man:"+str(iml))
        else:
            cal+=1
            imw+=1
            wins.set(wins.get() + "\n" + "Captain America:" + str(caw) + "\n" + "Iron Man:" + str(imw))
            loss.set(loss.get() + "\n" + "Captain America:" + str(cal) + "\n" + "Iron Man:" + str(iml))
    except IndexError:
        pass



# Sets title and creates gui
root = Tk()
root.title("Age of Ultron")

root.option_add('*tearOff', FALSE)
# Creates menu which options will be added
topMenu = Menu(root)
root.config(menu=topMenu)

# Creates menu and submenus
subMenu = Menu(topMenu)

# Gives menu File option and exit as a suboption which exits program
topMenu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Exit", command=root.destroy)

# Gives menu help option and About as a suboption
helpMenu = Menu(topMenu)
topMenu.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_command(label="About", command=about)

# Makes grid and places it
mainframe = ttk.Frame(root, padding=(5, 5, 12, 0))
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

# Makes a listbox on left side
ttk.Label(mainframe, text="Captain America").grid(column=0, row=0, sticky =(N,W))
leftnames = ('Punch', 'Shield', 'Kick')
lnames = StringVar(value=leftnames)
lbox = Listbox(mainframe, listvariable=lnames, exportselection=0, height=3)
lbox.grid(column=0, row=1)

statusmsg1 = StringVar()
status1 = ttk.Label(mainframe, textvariable=statusmsg1)
status1.grid(column=0, row=2, sticky=(N,W))

# Makes listbox for characters on right side
ttk.Label(mainframe, text="Iron Man").grid(column=2, row=0, sticky =(N,W))
rightnames = ('Exoskeleton', 'Missiles', 'Rocket')
rnames = StringVar(value=rightnames)
rbox = Listbox(mainframe, listvariable=rnames, exportselection=0, height=3)
rbox.grid(column=2, row=1)
# Disables right listbox for random use instead of user

statusmsg2 = StringVar()
status2 = ttk.Label(mainframe, textvariable=statusmsg2)
status2.grid(column=2, row=2, sticky=W)

# Shows users wins and lossses

wins = StringVar()
loss = StringVar()
# Labels the wins and losses

# Adds the character that won their match and the ones that lost their match
ttk.Label(mainframe, textvariable=wins).grid(column=1, row=1, sticky=(W, E))
ttk.Label(mainframe, textvariable=loss).grid(column=1, row=2, sticky=(W, E))
wins.set("Wins:")
loss.set("Losses:")
# Shows stats of character when clicked
lbox.bind('<<ListboxSelect>>', statDisplay1)
rbox.bind('<<ListboxSelect>>', statDisplay2)

# Button for fighting
fightbttn = ttk.Button(mainframe, text="Fight", command=fight)
fightbttn.grid(column=1, row=3, sticky=(E))

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.mainloop()