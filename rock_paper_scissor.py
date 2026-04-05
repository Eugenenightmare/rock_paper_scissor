import random

player_choice = input("Please enter your choice (rock, paper, or scissors): ").lower()

while player_choice != "rock" and player_choice != "paper" and player_choice != "scissors":
    print("That's not a valid move!")

    player_choice = input("Please try again: ").lower() 

print(f"You chose: {player_choice}")
    

random_number = random.randint(1,3)
if random_number == 1:
    computer_choice = "rock"
elif random_number == 2:
    computer_choice ="paper"
else:
    computer_choice = "scissors"
    
print("You chose: ", player_choice)
print("Computer chose: ", computer_choice)

if player_choice == computer_choice:
    print("It's a tie!")
    
elif (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "paper"and computer_choice == "rock") or (player_choice == "scissors" and computer_choice == "paper"):
    print("You Win!")
else:
    print("The computer wins!")
