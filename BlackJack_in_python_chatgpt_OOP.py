import random

# Constants
BLACKJACK = 21
COMPUTER_HIT_THRESHOLD = 17
INITIAL_COINS = 100





class BlackjackGame:
    def __init__(self):
        self.player = Player("Player")
        self.computer = Player("Computer")
        self.round_index = 1

    def player_bet(self):
        """Handles the player's bet, ensuring it's a valid amount."""
        while True:
            try:
                bet = int(input(f"Place your bet (Available: {self.player.coins}): "))
                if 1 <= bet <= self.player.coins:
                    self.player.coins -= bet
                    return bet
                print("Invalid bet. Try again.")
            except ValueError:
                print("Enter a valid number.")


    def play_round(self):
        """Plays a single round of Blackjack."""
        print(f"--- Round {self.round_index} ---")
        bet = self.player_bet()
        self.player.reset_hand()
        self.computer.reset_hand()

        # Initial draw
        for _ in range(2):
            self.player.draw_card()
            self.computer.draw_card()

        print(f"Player's Cards: {self.player.cards} | Total: {self.player.total}")
        print(f"Computer's Cards: [{self.computer.cards[0]}, ?]")

        # Player's turn
        while self.player.total < BLACKJACK:
            choice = input("Hit or Stand? (1 for Hit, 2 for Stand): ")
            if choice == "1":
                self.player.draw_card()
                print(f"Player's Cards: {self.player.cards} | Total: {self.player.total}")
            elif choice == "2":
                break
            else:
                print("Invalid choice. Please select 1 or 2.")

        # Computer's turn
        while self.computer.total < COMPUTER_HIT_THRESHOLD:
            self.computer.draw_card()

        print(f"Player's Final Cards: {self.player.cards} | Total: {self.player.total}")
        print(f"Computer's Final Cards: {self.computer.cards} | Total: {self.computer.total}")

        # Determine winner
        result = self.determine_winner()
        print(f"Result: {result}")
        self.adjust_coins(bet, result)

    def determine_winner(self):
        """Determines the winner of the round."""
        if self.player.total > BLACKJACK:
            return "Computer Wins"
        if self.computer.total > BLACKJACK:
            return "Player Wins"
        if self.player.total > self.computer.total:
            return "Player Wins"
        if self.computer.total > self.player.total:
            return "Computer Wins"
        return "Tie"

    def adjust_coins(self, bet, result):
        """Adjusts the coins based on the result of the round."""
        if result == "Player Wins":
            self.player.coins += bet * 2
            self.computer.coins -= bet
        elif result == "Computer Wins":
            self.computer.coins += bet

    def is_game_over(self):
        """Checks if the game is over based on coins."""
        if self.player.coins <= 0:
            print("Game Over! Computer Wins the Match.")
            return True
        if self.computer.coins <= 0:
            print("Game Over! Player Wins the Match.")
            return True
        return False

    def play(self):
        """Runs the main game loop."""
        while not self.is_game_over():
            self.play_round()
            self.round_index += 1
            print("\n")


# Run the game
if __name__ == "__main__":
    game = BlackjackGame()
    game.play()
