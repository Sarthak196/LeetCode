import random

choise = ["rock", "paper", "scissors"]
rule = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

def play_game():
    comp = random.choice(choise)
    user = input("Enter your choice (rock, paper, scissors): ").lower()
    if user not in choise:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        return play_game()
    print(f"Computer chose: {comp}")
    if user == comp:
        print("It's a tie!")
    elif rule[user] == comp:
        print("You win!")
    else:
        print("You lose!")

if __name__ == "__main__":
    while True:
        play_game()
        again = input("Do you want to play again? (yes/no): ").lower()
        if again != "yes":
            print("Thanks for playing!")
            break