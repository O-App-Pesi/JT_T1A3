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
        pull_number = 0
        pick_up_cylinder = True
        while pick_up_cylinder:
            try:
                action = Prompt.ask("What will you do?", 
                                    choices=["shake", "roll", "twist", "bash"])
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
                    action_number = random.randint(1, 6)
                    pull_number -= action_number
                print(f"If you finish now you'll get {pull_number}")
                pick_up_cylinder = Confirm.ask("Continue manipulating the cylinder?")
            except MemoryError as e:
                print('You have manipulated the cylinder enough!')
                pull_number = random.randint(1, 50)
                final_fortune(pull_number)
        final_fortune(pull_number)
    else:
        from_fortune()


def final_fortune(pull_number):
    dai_kyo = [8, 47, 14, 25, 49, 6, 17, 45, 26, 3]
    sho_kichi = [30, 33, 9, 44, 24, 18, 34, 50, 43, 2]
    kichi = [40, 29, 21, 15, 28, 35, 23, 36, 27, 1]
    dai_kichi = [42, 38, 7, 10, 32, 11, 4, 37, 48, 16, 5]
    kyo = [46, 19, 31, 12, 20, 22, 41, 39, 13, 4]
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
        direction = Prompt.ask("Where would you like to go?  ", 
                               choices=["East", "West", "Entrance", "Fortunes"])
        if direction == "Entrance":
            entrance()
        elif direction == "West":
            prayer_box()
        elif direction == "East":
            wish_block()
        elif direction == "Fortunes":
            pull_fortune()

def from_wish_block():
        direction = Prompt.ask("Where would you like to go? ", 
                               choices=["North", "West", "Entrance", "Wishes"])
        if direction == "Entrance":
            entrance()
        elif direction == "West":
            prayer_box()
        elif direction == "North":
            pull_fortune()
        elif direction == "Fortunes":
            wish_block()

def from_prayer_box():
        direction = Prompt.ask("Where would you like to go? ", 
                               choices=["North", "East", "Entrance", "Pray"])
        if direction == "Entrance":
            entrance()
        elif direction == "East":
            wish_block()
        elif direction == "North":
            pull_fortune()
        elif direction == "Fortunes":
            wish_block()

def wish_block():
    print("You arrive to rows of wires hung up with small wooden blocks dangling from them")
    print("These wooden blocks have people's wishes written on them")
    print("If you write a wish on block and then hang it up, it may come true...")
    user_choice = Prompt.ask("What is it you choose? ", choices=["Wish", "Review", "Leave"])
    if user_choice == "Wish":
        write_on_block()
    elif user_choice == "Review":
        review_previous_wishes()
    else:
        from_wish_block()

def write_on_block():
    try:
        column_name = ["Date", "Wish"]
        user_wish = input("What is your wish?")
        date = input("What is today's date?")
        with open('mywishes.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow([date, user_wish])
        print("Your hang the block upon the wire hopefully, fate is in the gods hands now...")
        to_do_next_wish()
    except EOFError as e:
        print("Your wishes are full!")
        to_do_next_wish()

def review_previous_wishes():
    try:
        with open('mywishes.csv', "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row[1])
                print(f"This wish was made on {row[0]}")
                print("Has it come true???")
        to_do_next_wish()
    except FileNotFoundError as e:
        print("You didn't make any wishes yet!")
        to_do_next_wish()

def to_do_next_wish():
    user_choice = Prompt.ask("What would you like to do next? ", choices=["Wish", "Review", "Leave"])
    if user_choice == "Wish":
        write_on_block()
    elif user_choice == "Review":
        review_previous_wishes()
    else:
        from_wish_block()


def prayer_box():
    round_number = random.randint(1, 5)
    print("There is a large donation box with a rope attached to a bell hanging above it.")
    print("If you make a donation, you may ring the bell to pray for the god's blessing.")
    print("It's your lucky day, you find a coin on the ground with no one around...")
    print("Is it an auspicious sign?")
    donate = Confirm.ask("Drop the coin in the donation box?")
    if donate:
        print("You drop the coin in the donation box and hear it clink on the bottom.")
        print("Grabbing the rope firmly, you whip it and the bell rings loudly...")
        if round_number == 1:
            print("Suddenly an auspicious wind whips up some fallen leaves, swirling all around you")
            print("Chimes hanging from the eaves begin to jingle and you feel a cool breeze on your neck")
            print("Today your luck feels... irridescent")
        elif round_number == 2:
            print("You wait but nothing occurs... You close your eyes and pray")
            print("You pray as hard as you can but nothing seems to happen")
            print("Today your luck feels inconsequential")
        elif round_number == 3:
            print("You close your eyes and a cold shiver runs down your spine")
            print("as you open them you see the sun has been blocked out by dark clouds")
            print("You quickly run to shelter and it looks like there might be heavy rain any moment")
            print("Today your luck feels foreboding")
        elif round_number == 4:
            print("You feel something inside your shoe that wasn't there before.")
            print("You take off your shoe to get it out but as you hop around on one leg,")
            print("you lose your balance and fall over in the dirt")
            print("Today your luck feels unpredictable...")
        else:
            print("You hear the rustling of a nearby bush")
            print("as you look over, a fox jumps out and greets you")
            print("Foxes are a blessed symbol")
            print("Today your luck feels positively uncomparable")
        draw_fortune = Confirm.ask("With your newfound luck in hand perhaps you would like to try your hand at drawing a fortune?")
        if draw_fortune:
            print("You rush to the fortunes window and quickly take the lottery box in hand")
            final_fortune(round_number)
        else:
            from_prayer_box()
    else:
        from_prayer_box()



def entrance():
    print("Welcome to KaiShin Shrine!")
    print("A large Tori gate stands before you,")
    print("as you walk through it you notice a sign ahead.")
    print("'\u2191 North you can find fortunes'")
    print("'\u21B1 East you can find wishing blocks'")
    print("'\u21B0 West you can pray to the gods of this shrine'")
    print("Quit to exit")
    direction = ""
    while direction != "North" or "East" or "West" or "Quit":
        direction = input("Where would you like to go?  ")
        if direction == "North":
            pull_fortune()
        elif direction == "East":
            wish_block()
        elif direction == "West":
            prayer_box()
        elif direction == "Quit":
            break



    