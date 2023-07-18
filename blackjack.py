# Imports
import sys
from random import choice

# Global variables
PLAYER_BALANCE = 0
PLAYER_NAME = ''
SUITS = ["Diamond's", "Club's", "Heart's", "Spade's"]
CARDS = ["Ace", "2", "3", "4", "5", "6", "7",
         "8", "9", "10", "Jack", "King", "Queen"]
# CARDS = [values for values in range(1,14)]


def main():
    # Start the Game
    game_menu()

# -------------------------------------------------------------------------------------------------


def game_menu():
    print("Welcome To BlackJack")
    #
    # Prompt user to Play or Exit the Game
    # #
    start_game = int(input("Select \n1) Play \n2) Exit \n"))
    if start_game == 1:
        game_engine()
    else:
        sys.exit()
# ------------------------------------------------------------------------------------------------
def game_engine():
    new_player = player_info()
    new_game(new_player["name"], new_player["balance"])
# ------------------------------------------------------------------------------------------------
def player_info():
    global PLAYER_NAME, PLAYER_BALANCE
    PLAYER_NAME = input("Enter Name: ")
    PLAYER_BALANCE = deposit()

    while PLAYER_BALANCE <= 10:
        print(f"${PLAYER_BALANCE} minimum deposit is $10")
        PLAYER_BALANCE += deposit()

    return {"balance": PLAYER_BALANCE, "name": PLAYER_NAME}
# -------------------------------------------------------------------------------------------------
def deposit():
    while True:
        amount = input("Enter amount to deposit $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be above $1")
        else:
            print("Invalid amount")

    return amount
# -----------------------------------------------------------------------------------------------
def new_game(name, balance):
    print(f"Name: {name} Account Balance: {balance}")
    bet_amount = get_bet()  # gets amount the player want to bet for prior to cards being dealt
    deal_cards(bet_amount)  # Deal player and dealer cards

# -------------------------------------------------------------------------------------------------
def get_bet():
    bet_amount = input("Amount to bet $")
    if bet_amount.isdigit():
        bet_amount = int(bet_amount)
        if 1 >= bet_amount < PLAYER_BALANCE:
            PLAYER_BALANCE -= bet_amount
    else:
        print("Enter a valid amount")

    return bet_amount
# --------------------------------------------------------------------
def deal_cards(bet_amount):
    """
    1. Get shuffled cards from shuffle_cards function
    2. Iterate through each card dealing two for the player and dealer
    3. Depending on what the player choices i.e 'h' hit, 's' stand 'd' double and 'l' split
        compare the value of the cards 
    4. Dealer auto hits if below 17 
    """
    amount = bet_amount
    balance = PLAYER_BALANCE
    game_cards = shuffle_cards()
    player_cards = []
    dealer_cards = []
    player_card_values = 0
    dealer_card_values = 0

    balance -= amount
    while len(game_cards) > 12:
        player_cards.append(deal_card(game_cards))
        dealer_cards.append(deal_card(game_cards))

        if len(player_cards) and len(dealer_cards) == 2:
            for card in range(len(player_cards)):
                player_card_values += int(player_cards[card]['value'])
            print(f"PLAYER: {player_card_values}")
            print(f"DEALER: {dealer_cards[card]['value']}") #Displays one dealer card value

            while player_card_values <= 21:
                choice = input("Hit (h), Stand (s), Double (d) :").upper()
                if choice == "H":
                    new_card = deal_card(game_cards)
                    player_card_values += int(new_card['value'])
                    print("Your cards value", player_card_values)
                elif choice == "D":
                    new_card = deal_card(game_cards)
                    player_card_values += int(new_card['value'])
                    print("Your cards value", player_card_values)
                    balance -= amount
                    amount *= 2
                    break
                elif choice == "S":
                    break
            
            for card in range(len(dealer_cards)):
                dealer_card_values += int(dealer_cards[card]['value'])

            print("Dealer: ", dealer_card_values)

            while dealer_card_values <= 16 and player_card_values <= 21:
                dc_card = deal_card(game_cards)
                dealer_card_values += int(dc_card['value'])
                print("Dealer: ", dealer_card_values)

                if dealer_card_values <= 21 and dealer_card_values >= 17:
                    break
            
            print() 
            # Compare Dealer cards and player cards
            if compare_values(player_card_values, dealer_card_values) == True:
                balance += amount * 2
                print(f"You WIN {amount} Balance : {balance}")
            elif compare_values(player_card_values, dealer_card_values) == False:
                print(f"You lose {amount} Balance: {balance}")
            elif compare_values(player_card_values, dealer_card_values):
                balance += amount
                print(f"PUSH Balance: {balance}")

            player_cards = []
            dealer_cards = []
            player_card_values = 0
            dealer_card_values = 0

            deal_option = input("Re-bet (r), New Bet(n), Quit (q): ").upper()
            if deal_option == "R":
                amount = bet_amount
                balance -= amount
                continue
            elif deal_option == "N":
                amount = get_bet()
                bet_amount = amount
                balance -= amount
                continue
            elif deal_option == "Q":
                break


# ---------------------------------------------------------------------------------
def deal_card(list):
    dealt_card = list.pop()
    match dealt_card['value']:
        case "Jack" | "Queen" | "King":
            dealt_card["value"] = 10
        case "Ace":
            dealt_card["value"] = 1

    len(list) - 1

    return dealt_card
# --------------------------------------------------------------------------------------
def compare_values(player_values, dealer_values):
    """
    Returns True if player wins and false if lose, push for draw
    """
    # Player wins 
    if player_values <= 21:
        if dealer_values > 21:
            return True
        else: 
            if player_values >  dealer_values:
                return True
            elif player_values < dealer_values:
                return False
            elif player_values == dealer_values:
                return "Push"
    else: 
        return False


    print()
# ---------------------------------------------------------------------
def shuffle_cards():
    # Shuffle cards to return a shuffled deck to play with ##
    # Each card has four cards of each suit i.e Ace of Diamond's, Ace of Spade's etc
    cards = []
    shuffled_deck = []
    for card in CARDS:
        for suit in SUITS:
            deck = {}
            deck["value"] = card
            deck["suit"] = suit
            cards.append(deck)

    while len(cards) != 0:
        card = choice(cards)
        cards.remove(card)
        shuffled_deck.append(card)

    return shuffled_deck

# Main function call#
if __name__ == "__main__":
    main()
