import random
from rich.prompt import Prompt, Confirm
from colored import fg, bg, attr

def pull_fortune():
    print("You arrive at a window where a shrine maiden is attending")
    print("A hexgonal cylinder sits on the counter in front of the window")
    print("If you shake, twist or roll this box, you can pull out a number")
    print("The shrine maiden will give you an omikuji (sacred fortune) in return...")
    user_continue = Confirm.ask("Would you like to pull a fortune?")
    if user_continue:
        print("You take the hexagonal cylinder in your hands...")
        print("Here's your chance to find your destiny...")
        print("Looks like you can shake, twist or roll it,")
        pick_up_cylinder = True
        while pick_up_cylinder:
            action = Prompt.ask("What will you do?", 
                                choices=["shake", "roll", "twist", "bash"])
            global pull_number
            pull_number = 0
            if action == "shake":
                print("You shake the cylinder vigorously")
                action_number = random.randint(3, 5)
                pull_number += action_number
            elif action == "roll":
                print("You roll the cylinder on its side systematically")
                action_number = random.randint(1, 3)
                pull_number += action_number
            elif action == "twist":
                print("You twist the cylinder left to right, the rods inside clunking top and bottom")
                action_number = random.randint(1, 5)
                pull_number += action_number 
            elif action == "bash":
                print("The shrine maiden gives you a funny look...")
                action_number = -10
                pull_number += action_number
            pick_up_cylinder = Confirm.ask("Continue manipulating the cylinder?")
        final_fortune()
    else:
        from_fortune()


def final_fortune():
    print(f"You draw a stick from the cylinder, it has the number {pull_number}")
    print("You show the stick to the shrine maiden and she pulls a slip of paper from one of many drawers")
    print("The slip of paper reads:")
    if pull_number == 0:
        print("大凶, dai-kyō")
    elif pull_number > 0 < 5:
        print("小吉, shō-kichi")
    elif pull_number >= 5 < 10:
        print("吉, kichi")
    elif pull_number >= 10 < 15:
        print("大吉, dai-kichi")
    elif pull_number < 0:
        print("凶, kyō")
    else:
        print("吉凶未分, kikkyō imada wakarazu")
    from_fortune()
    

def from_fortune():
        direction = Prompt.ask("Where would you like to go?", 
                               choices=["East", "West", "Entrance"],
                               default="Entrance")
        if direction == "Entrance":
            entrance()
        elif direction == "West":
            prayer_box()
        elif direction == "East":
            write_block()

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


    