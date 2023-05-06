import random
import csv
from rich.prompt import Prompt, Confirm
from console import console
from rich.table import Table

def pull_fortune():
    print(" ")
    console.print("[i]You arrive at a window where a [u]Shrine Maiden[/u] is attending.[/i]")
    console.print("[i]A [u]hexagonal cylinder[/u] sits on the counter in front of the window.[/i]")
    console.print("[i]If you [black on yellow]shake[/], [black on yellow]twist[/] or [black on yellow]roll[/] this cylinder, you can pull out a number[/i]")
    console.print("[i]The Shrine Maiden will give you an [blue on grey]omikuji[/] (sacred fortune) based on the number you pull[/i]")
    print(" ")
    user_continue = Confirm.ask("Would you like to pull for a fortune?")
    if user_continue:
        print(" ")
        console.print("[i]You take the hexagonal cylinder in your hands...[/i]")
        console.print("[i]Here's your chance to find your destiny...[/i]")
        print(" ")[i]
        pull_number = 0
        pick_up_cylinder = True
        while pick_up_cylinder:
            try:
                action = Prompt.ask("What will you do?", 
                                    choices=["shake", "roll", "twist", "bash"])
                if action == "shake":
                    console.print("[i]You shake the cylinder vigorously[/i]")
                    action_number = random.randint(3, 8)
                    pull_number += action_number
                elif action == "roll":
                    console.print("[i]You roll the cylinder on its side systematically[/i]")
                    action_number = random.randint(1, 4)
                    pull_number += action_number
                elif action == "twist":
                    console.print("[i]You twist the cylinder left to right, the rods inside clunking top and bottom[/i]")
                    action_number = random.randint(5, 9)
                    pull_number += action_number 
                elif action == "bash":
                    console.print("[i]The shrine maiden gives you a funny look...[/i]")
                    action_number = random.randint(1, 6)
                    pull_number -= action_number
                console.print(f"If you finish now you'll get {pull_number}")
                pick_up_cylinder = Confirm.ask("Continue manipulating the cylinder?")
            except MemoryError as e:
                print('[bold]You have manipulated the cylinder enough![/bold]')
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
    print(" ")
    console.print(f"[i]You draw a stick from the cylinder, it has the number [blue]{pull_number}[/][/i]")
    console.print("[i]You show the stick to the Shrine Maiden and she pulls a slip of paper from one of many drawers[/i]")
    console.print("[i]The slip of paper reads:[/i]")
    print(" ")
    if pull_number in dai_kyo:
        console.print("[dark red]大凶, dai-kyō[/darkred]")
        print(" ")
        console.print("dai-kyō represents a [b][dark red]terrible curse![/b][/dark red]")
        console.print("Perhaps it would behoove you to not step on any cracks...")
        print(" ")
    elif pull_number in sho_kichi:
        console.print("[light green]小吉, shō-kichi[/light green]")
        print(" ")
        console.print("shō-kichi is [i][light green]small blessing[/light green][/i]")
        console.print("Check your wallet, perhaps you'll find some extra cash")
        print(" ")
    elif pull_number in kichi:
        console.print("[green]吉, kichi[/green]")
        print(" ")
        console.print("kichi is a regular amount of [green]luck[/green]")
        console.print("I heard they're having [b]fifty percent off[/b] at that local restaurant you like so much")
        print(" ")
    elif pull_number in dai_kichi:
        console.print("[bright green]大吉, dai-kichi[/bright green]")
        print(" ")
        console.print("dai-kichi is an [u]extreme[/u] amount of [bright green]luck![/bright green]")
        console.print("I dunno what's gonna happen but it must be [u]good!!![/u]")
        print(" ")
    elif pull_number in kyo:
        console.print("[orange]凶, kyō[/orange]")
        print(" ")
        console.print("kyō represents a [i]small[/i] bit of [orange]bad luck...[/orange]")
        console.print("You might just stub your toe or something soon...")
        print(" ")
    else:
        console.print("吉凶未分, kikkyō imada wakarazu")
    input("Enter to continue: ")
    from_fortune()
    

def from_fortune():
        direction = Prompt.ask("Where would you like to go?  ", 
                               choices=["East", "West", "Entrance", "Fortunes", "Quit"])
        if direction == "Entrance":
            entrance()
        elif direction == "West":
            prayer_box()
        elif direction == "East":
            wish_block()
        elif direction == "Fortunes":
            pull_fortune()
        else:
            raise KeyboardInterrupt

def from_wish_block():
        direction = Prompt.ask("Where would you like to go? ", 
                               choices=["North", "West", "Entrance", "Wishes", "Quit"])
        if direction == "Entrance":
            entrance()
        elif direction == "West":
            prayer_box()
        elif direction == "North":
            pull_fortune()
        elif direction == "Fortunes":
            wish_block()
        else:
            raise KeyboardInterrupt

def from_prayer_box():
        direction = Prompt.ask("Where would you like to go? ", 
                               choices=["North", "East", "Entrance", "Pray", "Quit"])
        if direction == "Entrance":
            entrance()
        elif direction == "East":
            wish_block()
        elif direction == "North":
            pull_fortune()
        elif direction == "Fortunes":
            wish_block()
        else:
            raise KeyboardInterrupt

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
            table = Table(title="My Wishes")
            table.add_column("Date", justify="center", style="cyan", no_wrap=True)
            table.add_column("Wish", justify="center", style="green")
            for row in reader:
                table.add_row(row[0], row[1])
            console.print(table)
            console.print("Have you wishes come true?")  
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
    direction = Prompt.ask("Where would you like to go? ", choices=["North", "East", "West", "Quit"])
    if direction == "North":
        pull_fortune()
    elif direction == "East":
        wish_block()
    elif direction == "West":
        prayer_box()
    elif direction == "Quit":
        raise KeyboardInterrupt



    