import random


def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return "Error: Invalid name"


def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return "Error: Invalid number"


def rpsls(player_choice):
    print()
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0, 5)
    comp_choice = number_to_name(comp_number)
    diff = (comp_number - player_number) % 5
    print("Player chooses "+player_choice)
    print("Computer chooses "+comp_choice)
    if diff == 0:
        print("Player and computer tie!")
    elif diff == 1 or diff == 2:
        print("Computer wins!")
    elif diff == 3 or diff == 4:
        print("Player wins!")
    else:
        print("Error")


t = int(input("Number of games you want to play: "))
for i in range(t):
    rpsls(input("Player's choice: "))
    print()

print("Well Played !")
