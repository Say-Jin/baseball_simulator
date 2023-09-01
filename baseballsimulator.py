import random
baseball = random.randint(1, 410)

while True:
    response = input(f'Ready to play? swing or leave: ')
    if response == "swing":
        if baseball >= 360:
            print("It's a hit! HOMERUN!")
            print(f"{baseball}" + " meters")
            response = input("Would you like to swing again?: ")
            if response == "yes":
                continue
            else:
                break
        elif baseball < 360:
            print("It's a hit!")
            print(f"{baseball}" + " meters")
            response = input("Would you like to swing again?: ")
            if response == "yes":
                continue
            else:
                break
        elif baseball < 120:
            print("It's a miss")
            print(f"{baseball}" + " meters")
            response = input("Would you like to swing again?: ")
            if response == "yes":
                continue
            else:
                break
        else:
            print("Error")
            break
    else:
        response == input('Please try again: ')
        break