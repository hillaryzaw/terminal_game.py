# Welcome
print()
print("Hello, traveller. Welcome to THE Adventure Game!")
print("In this game, we will go through an adventurous journey based on your choices on the character's actions.\n")

name = str(input("To start, please enter your name: "))
# Galaxy of Choice
print(f"\nCrew - 'So, where are we going, Captain {name}?'")
planet = int(input("1. Chaos Galaxy\n2. Cookie Galaxy\n3. Pink Galaxy\n"))
while planet != 1 and planet != 2 and planet != 3:
    print("Invalid choice! Please choose again.")
    planet = int(input("1. Chaos Galaxy\n2. Cookie Galaxy\n3. Pink Galaxy\n"))
if planet == 1:
    galaxy = 'Chaos Galaxy'
elif planet == 2:
    galaxy = 'Cookie Galaxy'
else:
    galaxy = 'Pink Galaxy'
print(f"Crew - 'Alright, {galaxy} it is!\n")
input("Press enter to continue.\n")


# asteroid encounter
Your_hp = 150
print("Oh no! There is a big asteroid in our way.\nYour hp: 150\n")
asteroid = int(input("1. Go around it\n2. Headbump into it\n3. Shoot laser beams to break it\n"))
while asteroid != 1 and asteroid != 2 and asteroid != 3:
    print("Invalid choice! Please choose again.")
    asteroid = int(input("1. Go around it\n2. Headbump into it\n3. Shoot laser beams to break it\n"))
if asteroid == 1:
    print("Phew. That was a close one. Nice call!")
elif asteroid == 2:
    Your_hp -= 30
    print("Uh oh, you lost 30 hp from the collision...")
else:
    Your_hp -= 20
    print("The laser beam broke the asteroid into smaller pieces but you lost 20 hp from bumping your head:(")
print(f"Your hp: {Your_hp}\n")
input("Press enter to continue.\n")


# arrival to galaxy
print(f"You have reached {galaxy}! Where would you like to go for adventure?")
place = int(input("1. Towards the mountains\n2. Towards the ocean\n"))
print("You and your crew feel awe by the captivating view..")
print("Suddenly, you hear a noise and alert the team! 'WATCH OUT'\n")
while place != 1 and place != 2:
    print("Invalid choice! Please choose again.")
    place = int(input("1. Towards the mountains\n2. Towards the ocean\n"))
if place == 1:
    print("You're encountering a goblin!")
    monster = 'Goblin'
else:
    print("You're encountering a giant squid!")
    monster = 'Giant Squid'
input("\nPress enter to go to fight scene.\n")


# fight scene
monster_hp = 200
print(f"{monster}'s hp = 200")
round_num = 1
import random
while monster_hp > 0 and Your_hp > 0:
    print(f"Round - {round_num}")
    monatk = random.randint(1,3)
    if monatk == 1:
        print(f"The {monster} launched an attack and you lost 30 hp!")
        Your_hp -= 30
    elif monatk == 2:
        print(f"The {monster} launched a big attack and you lost 50 hp!")
        Your_hp -= 50
    else:
        print(f"Beware! The {monster} is lauching a super attack!!")
        atk = int(input("Quick! Choose an action:\n 1.Attack\n 2.Block\n 3.Heal\n"))
        if atk == 1:
            Your_hp -= 50
            monster_hp -= 20
            print("You managed to dodge the first punch but you got hit and you lost 50 hp.")
        elif atk == 2:
            print("Nice work! You did not take damage from the attack.")
        elif atk == 3:
            Your_hp -= 70
            print("Uh oh, you got attacked while you were healing and you lost 70 hp:()")
        else:
            Your_hp -= 60
            print("Oops, you were standing still and lost 60 hp from the attack.")
    print(f"\nYour hp: {Your_hp}\n{monster}'s hp: {monster_hp}")
    round_num += 1


    if monster_hp > 0 and Your_hp > 0:
        platk = int(input("Choose your attack:\n1. Punch it\n2. Kick it\n3. Heal\n\n"))
        while platk != 1 and platk != 2 and platk!= 3:
            print("Invalid choice! Please choose again.")
            platk = int(input("Choose your attack:\n1. Punch it\n2. Kick it\n3. Heal\n\n"))
        if platk == 1:
            monster_hp -= 70
            print(f"Nice punch! The {monster} lost 50 hp!")
        elif platk == 2:
            monster_hp -= 90
            print(f"Awesome kick! The {monster} lost 90 hp!")
        else:
            Your_hp += 40
            print("You have gained 40 hp!")   
    print(f"\nYour hp: {Your_hp}\n{monster}'s hp: {monster_hp}")


    if Your_hp <= 0:
        print("\nYou have been defeated:( Try again?\n")
        break
    elif monster_hp <= 0:
        print(f"\nCongratulations Captain {name}, you have defeated the {monster} of the {galaxy} and saved your crew!")
        print(f"Best of luck with your future adventures!")
        print()
        break
# The end!
