import random

suits = ["Spades","Clubs","Hearts","Diamonds"]
values = ['A','K','Q','J','10','9','8','7','6','5','4','3','2']
cards_in_deck = []



players_cards = []
computers_cards = []
players_total = 0
computers_total = 0
players_coins = 100
computers_coins = 100

winner = 0
newcard = 0
bet_amount = 0
next_round = 0
round_index = 1



# global next_round
# global computers_coins
# global players_coins
# global round_index 


def gen_card():
    number = random.randrange(2, 10, 1)
    return number

def start_draw():
    global players_total
    new_card = gen_card()
    players_cards.append(new_card)
    players_total = players_total + new_card
    
    new_card = gen_card()
    players_cards.append(new_card)
    players_total = players_total + new_card
    
    global computers_total 
    new_card = gen_card()
    computers_cards.append(new_card)
    computers_total = computers_total + new_card
    
    new_card = gen_card()
    computers_cards.append(new_card)
    computers_total = computers_total + new_card
    
    return players_total,computers_total,players_cards,computers_cards

def draw_player():
    new_card = gen_card()
    players_cards.append(new_card)
    players_total = players_total + new_card
    
    return players_total
    
def draw_computer():
    global computers_total
    new_card = gen_card()
    computers_cards.append(new_card)
    computers_total = computers_total + new_card


def com_win_screen():
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
    
    
def player_win_screen():
    print("Game Over")
    print("You Win")
    
    winner = 1
    if winner == 1:
        players_coins = players_coins + 2*bet_amount
        computers_coins = computers_coins - bet_amount
    next_round = 1
    
    players_cards = []
    computers_cards = []
    players_total = 0
    computers_total = 0
    
    return winner, players_cards, players_coins, players_total, computers_cards, computers_coins, computers_total, bet_amount, next_round
    
    
def win_lose_check():
    if players_total >21:
        player_win_screen()
    if computers_total >21:
        com_win_screen()
    if players_total == 21:
        com_win_screen()
    if computers_total == 21:
        player_win_screen()
        

def end_game_check():
    if players_total > computers_total:
        return player_win_screen()
    if computers_total > players_total:
        return com_win_screen()
    if players_total == computers_total:
        print("Game Over")
        print("It's a Tie")
        global next_round
        next_round = 1
        return 
        
        
def player_choice():
    
    while(1):
        choice = input("Player, Hit or Stand? 1 for Hit, 2 for Stand ")
        print("        ")
        if choice == "1":
            draw_player()
            break
        if choice == "2":
            end_game_check()
            break
        else:
            print("Please input a valid choice, 1 or 2 without any spaces.")
            
    return choice
        

def print_board():
    # print("Player's cards:" + str(players_cards))
    # print("Computer's cards:" + str(computers_cards))
    print("Player's total:" + str(players_total))
    print("Computer's total:" + str(computers_total))


def player_bet():
    
    print(f"Computer's Coins: " + str(computers_coins))
    print(f"Player's Coins: " + str(players_coins))
    #                                 BETTING AMOUNT
    valid_choice = 0
    while(valid_choice == 0): #       BETTING AMOUNT
        bet_amount = int(input("How much do you want to bet? "))
        
        if bet_amount >=1 or bet_amount < players_coins:
            valid_choice = 1
        else:
            valid_choice = 0
            print("That was an invalid choice, please input a number between 1 and your max bet")
    
    players_coins = players_coins - bet_amount
    
    return players_coins, bet_amount, computers_coins

    

# def CPU_logic(players_cards,computers_cards):
#     if opponent_cards > yours:
#         return Bet 
#     else:
#         return stand
        
        




#Game
while(players_coins >0 or computers_coins >0):
    # Match
    start_draw()
    print_board()
    player_bet()
    
    next_round = 0
    while(next_round == 0):
        
        
        win_lose_check()
        if winner == 1:
            break
        
        player_choice()
     
        print_board()
        
        
        round_index += round_index
        print("Round # " + str(round_index))
        print("            ")