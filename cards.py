from random import choice

class Cards:
    SUITS = ["Diamond's", "Club's", "Heart's", "Spade's"]
    CARDS = ["Ace", "2", "3", "4", "5", "6", "7","8", "9", "10", "Jack", "King", "Queen"]
    def __init__(self) -> None:
        pass
    @classmethod
    def shuffle_card(self):
        cards = []
        shuffled_deck = []
        for card in self.CARDS:
            for suit in self.SUITS:
                deck = {}
                deck["value"] = card
                deck["suit"] = suit
                cards.append(deck)

        while card.len() != 0:
            card = choice(cards)
            cards.remove(card)
            shuffled_deck.append(card)
            
        return shuffled_deck
    
    def deal_cards(self):
        ...
    @staticmethod
    def deal_card(list):
        dealt_card = list.pop()