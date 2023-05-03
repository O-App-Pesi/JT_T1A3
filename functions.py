import random
import csv
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
                action_number = random.randint(3, 8)
                pull_number += action_number
            elif action == "roll":
                print("You roll the cylinder on its side systematically")
                action_number = random.randint(1, 4)
                pull_number += action_number
            elif action == "twist":
                print("You twist the cylinder left to right, the rods inside clunking top and bottom")
                action_number = random.randint(5, 9)
                pull_number += action_number 
            elif action == "bash":
                print("The shrine maiden gives you a funny look...")
                action_number = random.randint(-1, -6)
                pull_number += action_number
            print(f"If you finish now you'll get {pull_number}")
            pick_up_cylinder = Confirm.ask("Continue manipulating the cylinder?")
        final_fortune()
    else:
        from_fortune()


def final_fortune():
    dai_kyo = [8, 47, 14, 25, 49, 6, 17, 23, 45, 26]
    sho_kichi = [30, 33, 9, 44, 24, 18, 36, 34, 50, 43]
    kichi = [40, 5, 29, 21, 15, 28, 35, 2, 1, 27]
    dai_kichi = [42, 38, 7, 10, 32, 11, 4, 37, 48, 16]
    kyo = [46, 19, 31, 12, 20, 22, 41, 39, 13, 3]
    print(f"You draw a stick from the cylinder, it has the number {pull_number}")
    print("You show the stick to the shrine maiden and she pulls a slip of paper from one of many drawers")
    print("The slip of paper reads:")
    if pull_number in dai_kyo:
        print("大凶, dai-kyō")
    elif pull_number in sho_kichi:
        print("小吉, shō-kichi")
    elif pull_number in kichi:
        print("吉, kichi")
    elif pull_number in dai_kichi:
        print("大吉, dai-kichi")
    elif pull_number in kyo:
        print("凶, kyō")
    else:
        print("吉凶未分, kikkyō imada wakarazu")
    user_continue = Confirm.ask("Continue?")
    from_fortune()
    

def from_fortune():
        direction = Prompt.ask("Where would you like to go?", 
                               choices=["East", "West", "Entrance", "Fortunes"],
                               default="Entrance")
        if direction == "Entrance":
            entrance()
        elif direction == "West":
            prayer_box()
        elif direction == "East":
            wish_block()
        elif direction == "Fortunes":
            pull_fortune()

def from_wish_block():
        direction = Prompt.ask("Where would you like to go?", 
                               choices=["North", "West", "Entrance", "Wishes"],
                               default="Entrance")
        if direction == "Entrance":
            entrance()
        elif direction == "West":
            prayer_box()
        elif direction == "North":
            pull_fortune()
        elif direction == "Fortunes":
            wish_block()

def wish_block():
    print("You arrive to rows of wires hung up with small wooden blocks dangling from them")
    print("These wooden blocks have people's wishes written on them")
    print("If you write a wish on block and then hang it up, it may come true...")
    user_choice = Prompt.ask("What is it you choose?", choices=["Wish", "Review", "Leave"])
    if user_choice == "Wish":
        write_on_block()
    elif user_choice == "Review":
        review_previous_wishes()
    else:
        from_wish_block()

def write_on_block():
    column_name = ["Date", "Wish"]
    user_wish = input("What is your wish?")
    date = input("What is today's date?")
    with open('mywishes.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([date, user_wish])
    print("Your hang the block upon the wire hopefully, fate is in the gods hands now...")
    user_choice = Prompt.ask("What would you like to do next?", choices=["Wish", "Review", "Leave"])
    if user_choice == "Wish":
        write_on_block()
    elif user_choice == "Review":
        review_previous_wishes()
    else:
        from_wish_block()

def review_previous_wishes():
    print("review wishes")

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
            wish_block()
        elif direction == "West":
            prayer_box()


    