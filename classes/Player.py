# Native
import sys

# Third party
from colorama import Fore, Back, Style

class Player():
    
    def __init__(self, name):
        self._name = name.title()
        self._hand = []
        self.handRating = 0
        self.highCard = 0
        self.description = ''


    def draw_cards(self, deck, count=5):
        """
        """
        for _ in range(count):
            card = deck.pop()
            self.get_hand().append(card)

        print(f'\n{self.get_name()}, you drew: {Fore.CYAN}{self.get_hand()}{Style.RESET_ALL}')
        # self.discard_cards(deck)


    def discard_cards(self, deck):
        """Replaces cards
        """
        discards = input('Which cards do you want to discard? Enter "N" if None: ')

        if (discards.lower() != 'N'.lower() and discards.lower() != '0'):
            for to_be_discarded in discards.split(","):
                self.get_hand()[int(to_be_discarded)-1] = deck.pop()


    def updateState(self, handRating, description, highCard):
        """
        """
        self.handRating = handRating
        self.description = description
        self.highCard = highCard


    def __eq__(self, player):
        """
        """
        if isinstance(player, Player):
            return player._name == self._name

        return False


    def __repr__(self):
        return self._name


    def get_name(self):
        return self._name


    def get_hand(self):
        return self._hand