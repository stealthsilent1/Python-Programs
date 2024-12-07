import random

suits = ["Spades","Clubs","Hearts","Diamonds"]
values = ['A','K','Q','J','10','9','8','7','6','5','4','3','2']
cards_in_deck = []



# players_cards = []
# computers_cards = []
# players_total = 0
# computers_total = 0
# players_coins = 100
# computers_coins = 100

# winner = 0
# newcard = 0
# bet_amount = 0
# next_round = 0
# round_index = 1



# global next_round
# global computers_coins
# global players_coins
# global round_index 


def gen_card():
    number = random.randrange(2, 10, 1)
    return number

def start_draw():
    players_cards = [gen_card(),gen_card()]
    computers_cards = [gen_card(),gen_card()]
    
    players_total = players_cards[0] + players_cards[1]
    computers_total = computers_cards[0] + computers_cards[1]
    
    return players_total,computers_total,players_cards,computers_cards

def draw_player(players_total,players_cards):
    new_card = gen_card()
    players_cards.append(new_card)
    players_total = players_total + new_card
    
    return players_total, players_cards
    
def draw_computer(computers_total,computers_cards):
    new_card = gen_card()
    computers_cards.append(new_card)
    computers_total = computers_total + new_card
    return computers_total,computers_cards

def end_game_check(players_total,computers_total):
    # Player wins
    if (players_total > computers_total and stand == True) or computers_total >21:
        print("Game Over")
        print("You Win")
        
        #change coins
        winner = 1
        if winner == 1:
            players_coins = players_coins + 2*bet_amount
            computers_coins = computers_coins - bet_amount
        next_round = 1
        
        #set cards to 0
        players_cards, computers_cards = []
        players_total,computers_total = 0
        
        
        return winner, players_cards, players_coins, players_total, computers_cards, computers_coins, computers_total, bet_amount, next_round
    # CPU wins
    if (computers_total > players_total and stand == True) or players_total >21:
        print("Game Over")
        print("Computer Wins")
        
        winner = 0
        if winner == 0:
            computers_coins = computers_coins + bet_amount
        next_round = 1
        
        players_cards = []
        computers_cards = []
        players_total = 0
        computers_total = 0
    
        return winner, players_cards, players_coins, players_total, computers_cards, computers_coins, computers_total, bet_amount, next_round
    # Tie
    if players_total == computers_total and stand == True:
        print("Game Over")
        print("It's a Tie")
        next_round = 1
        return next_round
        
        
def player_choice(players_total,players_cards):
    
    while True:
        try:
            choice = int(input("Player, Hit or Stand? 1 for Hit, 2 for Stand "))
            print("        ")
            if choice == 1:
                draw_player(players_total,players_cards)
                hit = True
                return hit
            if choice == 2:
                stand = True
                return stand
            
        except ValueError:
            print("Please input a valid choice, 1 or 2 without any spaces.")
            
        

def print_board(players_cards,computers_cards,players_total,computers_total):
    print("Player's cards:" + str(players_cards))
    print("Computer's cards:" + str(computers_cards))
    print("Player's total:" + str(players_total))
    print("Computer's total:" + str(computers_total))


def player_bet(players_coins,computers_coins):
      
    print(f"Computer's Coins: {computers_coins}")
    print(f"Player's Coins: {players_coins}")
    
    #                                 BETTING AMOUNT
    
    valid_choice = 0
    
    while(valid_choice == 0): #       BETTING AMOUNT
        
        bet_amount = int(input("How much do you want to bet? "))
        
        if bet_amount >=1 and bet_amount <= players_coins:
            valid_choice = 1
        else:
            valid_choice = 0
            print("That was an invalid choice, please input a number between 1 and your max bet")
    
    players_coins = players_coins - bet_amount
    
    return players_coins, bet_amount

    

# def CPU_logic(players_cards,computers_cards):
#     if opponent_cards > yours:
#         return Bet 
#     else:
#         return stand
        
        




#Game
def Game(players_coins,players_total,players_cards,computers_coins,computers_total,computers_cards):
    while(players_coins >0 or computers_coins >0):
        # Match
        start_draw(players_total,computers_total)
        print_board()
        player_bet(players_coins,computers_coins)
        
        next_round = 0
        while(next_round == 0):
            
            
            end_game_check(players_total,computers_total)
            if winner == 1:
                break
            
            player_choice()
        
            print_board()
            
            
            round_index += round_index
            print("Round # " + str(round_index))
            print("            ")
            
Game()