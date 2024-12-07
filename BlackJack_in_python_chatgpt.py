import random

# Initialize game variables
players_coins = 100
computers_coins = 100
round_index = 1

# Card generation
def gen_card():
    return random.randint(2, 10)

# Initial draw
def start_draw():
    players_cards = [gen_card(), gen_card()]
    computers_cards = [gen_card(), gen_card()]
    players_total = sum(players_cards)
    computers_total = sum(computers_cards)
    return players_cards, computers_cards, players_total, computers_total

# Draw cards
def draw_player(players_cards, players_total):
    new_card = gen_card()
    players_cards.append(new_card)
    players_total += new_card
    return players_cards, players_total

def draw_computer(computers_cards, computers_total):
    new_card = gen_card()
    computers_cards.append(new_card)
    computers_total += new_card
    return computers_cards, computers_total

# Check win/lose conditions
def check_win(players_total, computers_total):
    if players_total > 21:
        return "Computer Wins"
    elif computers_total > 21:
        return "Player Wins"
    elif players_total == 21:
        return "Player Wins"
    elif computers_total == 21:
        return "Computer Wins"
    return None

# End game condition
def end_game(players_total, computers_total):
    if players_total > computers_total:
        return "Player Wins"
    elif computers_total > players_total:
        return "Computer Wins"
    else:
        return "Tie"

# Player's betting function
def player_bet(players_coins):
    while True:
        try:
            bet_amount = int(input(f"How much do you want to bet? (Available: {players_coins}) "))
            if 1 <= bet_amount <= players_coins:
                players_coins -= bet_amount
                return bet_amount, players_coins
            else:
                print("Invalid bet. Please enter a valid amount.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Main game loop
while players_coins > 0 and computers_coins > 0:
    print(f"--- Round {round_index} ---")
    print(f"Player's Coins: {players_coins}, Computer's Coins: {computers_coins}")
    
    # Betting phase
    bet_amount, players_coins = player_bet(players_coins)
    
    
    # Draw initial cards
    players_cards, computers_cards, players_total, computers_total = start_draw()
    print(f"Player's Cards: {players_cards} | Total: {players_total}")
    print(f"Computer's Cards: [{computers_cards[0]}, ?]")
    
    # Player's turn
    while players_total < 21:
        choice = input("Hit or Stand? (1 for Hit, 2 for Stand): ")
        if choice == "1":
            players_cards, players_total = draw_player(players_cards, players_total)
            print(f"Player's Cards: {players_cards} | Total: {players_total}")
        elif choice == "2":
            break
        else:
            print("Invalid choice. Please select 1 or 2.")
    
    # Computer's turn
    while computers_total < 17:
        computers_cards, computers_total = draw_computer(computers_cards, computers_total)
    
    # Display final cards and totals
    print(f"Player's Cards: {players_cards} | Total: {players_total}")
    print(f"Computer's Cards: {computers_cards} | Total: {computers_total}")
    
    # Determine round result
    result = check_win(players_total, computers_total)
    if not result:
        result = end_game(players_total, computers_total)
    
    print(f"Result: {result}")
    if result == "Player Wins":
        players_coins += bet_amount * 2
        computers_coins -= bet_amount
    elif result == "Computer Wins":
        computers_coins += bet_amount
    
    # Check for game over
    if players_coins <= 0:
        print("Game Over! Computer Wins the Match.")
        break
    elif computers_coins <= 0:
        print("Game Over! Player Wins the Match.")
        break
    
    round_index += 1
    print("\n")

