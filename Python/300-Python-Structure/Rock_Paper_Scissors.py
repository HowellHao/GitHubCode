def rock_paper_scissors(player):
    import random

    choices = ['rock', 'paper', 'scissors']
    computer = random.choice(choices)
    print("Computer chose:", computer)
    
    # Determine the winner
    if player == computer:
        return "tie"
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'paper' and computer == 'rock') or \
         (player == 'scissors' and computer == 'paper'):
        return "player"
    else:
        return "computer"
    
def main():
    player_wins = 0
    computer_wins = 0
    ties = 0

    player_choice = input("Enter rock, paper, or scissors: ").lower()
    if player_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please try again.")
        return

    result = rock_paper_scissors(player_choice)
    if result == "player":
        print("You win!")
        player_wins += 1
    elif result == "computer":
        print("You lose!")
        computer_wins += 1
    else:
        print("It's a tie!")
        ties += 1

    while True:
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again == 'yes':
            player_choice = input("Enter rock, paper, or scissors: ").lower()
            if player_choice not in ['rock', 'paper', 'scissors']:
                print("Invalid choice. Please try again.")
                continue
            result = rock_paper_scissors(player_choice)
            if result == "player":
                print("You win!")
                player_wins += 1
            elif result == "computer":
                print("You lose!")
                computer_wins += 1
            else:
                print("It's a tie!")
                ties += 1
        elif play_again == 'no':
            print(f"Final score: Player wins: {player_wins}, Computer wins: {computer_wins}, Ties: {ties}")
            print("Thanks for playing!")
            break
        else:
            print("Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()