import random

user_score = 0
computer_score = 0

print("=== Rock Paper Scissors Game ===")

while True:
    print("\nChoose one:")
    print("1. rock")
    print("2. paper")
    print("3. scissors")

    user = input("Enter your choice: ").lower()

    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)

    print("\nComputer chose:", computer)
    print("You chose:", user)

    if user not in choices:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        continue

    if user == computer:
        print("It's a tie!")

    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        print("You win!")
        user_score += 1

    else:
        print("Computer wins!")
        computer_score += 1

    print("\nScore Board")
    print("Your Score:", user_score)
    print("Computer Score:", computer_score)

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("\nFinal Scores")
        print("Your Score:", user_score)
        print("Computer Score:", computer_score)
        print("Thanks for playing!")
        break