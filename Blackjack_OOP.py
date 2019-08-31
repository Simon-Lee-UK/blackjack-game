"""
Hey guys. So I wanted to use OOP to make the card deck.
At first I just used a class "Card", which took the arguments "Name" i.e. King, "Suit" i.e. Heart, and "Value" i.e. 10.
But then I thought I could have 4 classes, one for each suit, and each class has a class variable "suit"
So then each class only takes 2 arguments, "Name" and "Value"
I thought this'd be cool, but it may have been clunkier!
See if you guys can do anything to streamline the code! It seems excessively long now.
"""

import numpy as np


class Club:
    suit = 'Club'  # this is from tutorial 2 - it's a class variable!

    def __init__(self, name, value):
        self.name = name
        self.value = value

    # Creating a method within the class!
    def display_card(self):
        return '{} of {}s'.format(self.name, self.suit)


card1 = Club('Ace', '1 or 11')
card2 = Club(2, 2)
card3 = Club(3, 3)
card4 = Club(4, 4)
card5 = Club(5, 5)
card6 = Club(6, 6)
card7 = Club(7, 7)
card8 = Club(8, 8)
card9 = Club(9, 9)
card10 = Club(10, 10)
card11 = Club('Jack', 10)
card12 = Club('Queen', 10)
card13 = Club('King', 10)


class Spade:
    suit = 'Spade'  # this is from tutorial 2 - it's a class variable!

    def __init__(self, name, value):
        self.name = name
        self.value = value

    # Creating a method within the class!
    def display_card(self):
        return '{} of {}s'.format(self.name, self.suit)


card14 = Spade('Ace', '1 or 11')
card15 = Spade(2, 2)
card16 = Spade(3, 3)
card17 = Spade(4, 4)
card18 = Spade(5, 5)
card19 = Spade(6, 6)
card20 = Spade(7, 7)
card21 = Spade(8, 8)
card22 = Spade(9, 9)
card23 = Spade(10, 10)
card24 = Spade('Jack', 10)
card25 = Spade('Queen', 10)
card26 = Spade('King', 10)


class Heart:
    suit = 'Heart'  # this is from tutorial 2 - it's a class variable!

    def __init__(self, name, value):
        self.name = name
        self.value = value

    # Creating a method within the class!
    def display_card(self):
        return '{} of {}s'.format(self.name, self.suit)


card27 = Heart('Ace', '1 or 11')
card28 = Heart(2, 2)
card29 = Heart(3, 3)
card30 = Heart(4, 4)
card31 = Heart(5, 5)
card32 = Heart(6, 6)
card33 = Heart(7, 7)
card34 = Heart(8, 8)
card35 = Heart(9, 9)
card36 = Heart(1, 10)
card37 = Heart('Jack', 10)
card38 = Heart('Queen', 10)
card39 = Heart('King', 10)


class Diamond:
    suit = 'Diamond'  # this is from tutorial 2 - it's a class variable!

    def __init__(self, name, value):
        self.name = name
        self.value = value

    # Creating a method within the class!
    def display_card(self):
        return '{} of {}s'.format(self.name, self.suit)


card40 = Diamond('Ace', '1 or 11')
card41 = Diamond(2, 2)
card42 = Diamond(3, 3)
card43 = Diamond(4, 4)
card44 = Diamond(5, 5)
card45 = Diamond(6, 6)
card46 = Diamond(7, 7)
card47 = Diamond(8, 8)
card48 = Diamond(9, 9)
card49 = Diamond(10, 10)
card50 = Diamond('Jack', 10)
card51 = Diamond('Queen', 10)
card52 = Diamond('King', 10)

deck = [card1, card2, card3, card4, card5, card6, card7, card8, card9, card10,
        card11, card12, card13, card14, card15, card16, card17, card18, card19,
        card20, card21, card22, card23, card24, card25, card26, card27, card28,
        card29, card30, card31, card32, card33, card34, card35, card36, card37,
        card38, card39, card40, card41, card42, card43, card44, card45, card46,
        card47, card48, card49, card50, card51, card52]

random_index_1 = np.random.randint(52)
print('random index 1 = {}'.format(random_index_1))
random_index_2 = np.random.randint(52)
print('random index 2 = {}'.format(random_index_2))

random_card_1 = deck[random_index_1]
random_card_2 = deck[random_index_2]

print('Random card 1 is {}'.format(random_card_1.display_card()))
print('Random card 2 is {}'.format(random_card_2.display_card()))

# I have more code that actually plays the game of Blackjack in a different file
# i.e. it tells you your hand value, and the dealer has 2 secret cards, and then asks you to hit or stick
# But I thought I'd leave it here for now
# You guys could even add that functionality here!
# Would be interested to see how you'd go about it
