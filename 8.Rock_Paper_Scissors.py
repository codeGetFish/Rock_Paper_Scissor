import random

while True:
    try:
        # Take player input for the choice of rock, paper or scissors
        player1 = input("Rock, Paper or Scissors: ")
        
        # check if the input is valid
        if player1.capitalize() not in ["Rock", "Paper", "Scissors"]:
            raise ValueError("Error: Please enter a valid choice.")
        
        # Randomly select choice for computer from rock, paper or scissors
        computer = random.choice(["Rock","Paper","Scissors"])

        # Capitalize the player's choice
        choice = str(player1).capitalize()

        # Check for tie
        if choice == computer:
            print(f"It's a tie, you both chose {computer}")
        # Check for player win
        elif choice == "Rock" and computer == "Scissors":
            print(f"You win! You chose {choice} and the computer chose {computer}")
        elif choice == "Paper" and computer == "Rock":
            print(f"You win! You chose {choice} and the computer chose {computer}")
        elif choice == "Scissors" and computer == "Paper":
            print(f"You win! You chose {choice} and the computer chose {computer}")
        # If none of the above conditions are met, player loses
        else:
            print(f"You loose! You chose {choice} and the computer chose {computer}")
    except ValueError as e:
        print(str(e))
    except:
        print("Error: An unknown error occurred.")
