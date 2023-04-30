import random
from rich.prompt import Prompt, Confirm
from colored import fg, bg, attr

def pull_fortune():
    print("You arrive at a window where a shrine maiden is attending")
    print("A box sits on the counter in front of the window")
    print("If you shake, twist or roll this box, you can pull out a number")
    print("The shrine maiden will give you an omikuji (sacred fortune) in return...")
    user_continue = Confirm.ask("Would you like to pull a fortune?")

def write_block():
    print("write on wish block")

def prayer_box():
    print("pray to the god of this shrine")

def entrance():
    print("Welcome to KaiShin Shrine!")
    print("A large Tori gate stands before you,")
    print("as you walk through it you notice a sign ahead.")
    print("'\u2191 North you can find fortunes'")
    print("'\u21B1 East you can find wishing blocks'")
    print("'\u21B0 West you can pray to the gods of this shrine'")
    direction = ""
    while direction == "":
        direction = input("Where would you like to go?  ")
        if direction == "North":
            pull_fortune()
        elif direction == "East":
            write_block()
        elif direction == "West":
            prayer_box()


    