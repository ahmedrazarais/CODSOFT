import random



class Game:
    def __init__(self):
        self.user_score = 0
        self.computer_score = 0  # setting attributes

    def get_user_choice(self):
        """Prompt the user to choose rock, paper, or scissors."""
        while True:
            user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
            if user_choice in ['rock', 'paper', 'scissors']:
                return user_choice
            else:
                print("Invalid choice. Please choose from rock, paper, or scissors.")

    def get_computer_choice(self):
        """Generate a random choice (rock, paper, or scissors) for the computer."""
        return random.choice(['rock', 'paper', 'scissors'])

    def determine_winner(self, user_choice, computer_choice):
        """Determine the winner based on the user's choice and the computer's choice."""
        if user_choice == computer_choice:
            return "It's a tie!", 0, 0  # If it's a tie, return 0 points for both
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            return "You win!", 1, 0  # If user wins, return 1 point for user and 0 for computer
        else:
            return "Computer wins!", 0, 1  # If computer wins, return 0 for user and 1 point for computer

    def play_game(self):
        """Play a single round of Rock-Paper-Scissors."""
        print("\nLet's play Rock-Paper-Scissors!\n")
        while True:
            user_choice = self.get_user_choice()  # Get user choice
            computer_choice = self.get_computer_choice()  # Get computer choice
            print(f"\nYour choice: {user_choice}")
            print(f"Computer's choice: {computer_choice}")
            result, user_round_score, computer_round_score = self.determine_winner(user_choice, computer_choice)
            # Determine the winner and update scores
            print(result)
            self.user_score += user_round_score  # Update user score
            self.computer_score += computer_round_score  # Update computer score
            print(f"Your score: {self.user_score}")
            print(f"Computer's score: {self.computer_score}")

            # asking for another game
            while True:
                play_again = input("\nDo you want to play again? (yes/no): ").lower()
                if play_again == 'no':
                    print("Thanks for playing!")
                    exit()
                elif play_again == 'yes':
                    break
                else:
                    print("Input not recognized. Please enter 'yes' or 'no'.")

def main():
    game = Game() # making instance of class
    game.play_game()

main()

