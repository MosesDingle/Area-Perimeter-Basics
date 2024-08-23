import random

options = ("rock", "paper", "scissors")
playing = True


while playing:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a valid choice of (rock, paper, scissors):")

    print(f"player: {player}")
    print(f"Computer: {computer}")
    if player == computer:
        print("Tie")

    elif player == "rock" and computer == "scissors":
        print("That's a massive W in the chat")

    elif player == "paper" and computer == "rock":
        print("That's a massive W in the chat")

    elif player == "scissors" and computer == "paper":
        print("That's a massive W in the chat")

    else:
        print("That's a big L buddy")

    play_again = input("Play again? (y/n): ").lower()
    if not play_again == "y":
        playing = False

print("Thanks for playing")
