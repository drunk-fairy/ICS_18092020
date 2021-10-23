import random

class Card():

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def info_rank(self):
        return self.rank

    def __str__(self):
        return f'{self.rank} {self.suit}'

class Deck():
    
    def __init__(self, cards):
        self.cards = cards
    
    def deck_info(self):
        for card in self.cards:
            print(card)
    
    def shuffle_cards(self):
        random.shuffle(self.cards)
    
    def get_one_card(self):
        if not self.cards:
            return 'no card'
        return random.choice(self.cards)
    def get_six_cards(self):
        return [self.get_one_card() for i in range(6)]

rank = ['Ace', 'King', 'Queen', 'Jack', '10', '9', '8', '7', '6', '5', '4', '3', '2']
suit = ['of hearts', 'of spades', 'of diamonds', 'of clubs']
cards = [Card(s, r) for s in suit for r in rank]

deck = Deck(cards)

print('\n')
print('The deck:\n')
deck.deck_info()
print('\n')

deck.shuffle_cards()
print('Shuffled deck:\n')
deck.deck_info()
print('\n')

print('Getting one card:\n')
print(deck.get_one_card())
print('\n')

print('Getting six cards:\n')
for card in deck.get_six_cards():
    print(card)
print()