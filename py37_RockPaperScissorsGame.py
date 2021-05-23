import random

while True:
    choices = ["rock", "paper", "scissors"]

    computerChoose = random.choice(choices)
    playerChoose = None

    while playerChoose not in choices:
        playerChoose = input("Rock, Paper, Scissors? : ").lower()

    print("Computer : "+computerChoose)
    print("Player\t : "+playerChoose)

    if playerChoose == computerChoose:
        print("= = = TIE = = =")
    elif playerChoose == "rock":
        if computerChoose == "paper":
            print('= = = YOU LOSE = = =')
        if computerChoose == "scissors":
            print('= = = YOU WIN = = =')
    elif playerChoose == "paper":
        if computerChoose == "scissors":
            print('= = = YOU LOSE = = =')
        if computerChoose == "rock":
            print('= = = YOU WIN = = =')
    elif playerChoose == "scissors":
        if computerChoose == "rock":
            print('= = = YOU LOSE = = =')
        if computerChoose == "paper":
            print('= = = YOU WIN = = =')

    playAgain = input("Play Again? (yes/no) : ").lower()

    if playAgain != "yes":
        break
    
print('End Program')