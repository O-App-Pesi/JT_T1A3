from functions import entrance

try:
    entrance()
except KeyboardInterrupt as e:
    print(" ")
    print("I hope you enjoyed your time at Kaishin Shrine!")
    print(" ")
except Exception as e:
    print("Sorry we ran into a problem!")


