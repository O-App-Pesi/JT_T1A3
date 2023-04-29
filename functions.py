def pull_fortune():
    print("pull a fortune")

def write_block():
    print("write on wish block")

def prayer_box():
    print("pray to the god of this shrine")

def entrance():
    print("Welcome to KaiShin Shrine!")
    print("A large Tori gate stands before you,")
    print("as you walk through it you notice a sign ahead.")
    print("The sign reads: 'North you can find fortunes'")
    print("'East you can find wishing blocks'")
    print("'West you can pray to the gods of this shrine'")
    direction = ""
    while direction != "North" or "East" or "West":
        direction = input("Where would you like to go?")
        if direction == "North":
            pull_fortune()
        elif direction == "East":
            write_block()
        elif direction == "West":
            prayer_box()
    