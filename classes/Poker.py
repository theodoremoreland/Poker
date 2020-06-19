# Native
import sys

# Third party
from colorama import Fore, Back, Style

sys.path.append("..")

class Poker():
    """
    """
    variant = "5-Card Draw"
    hands = []

    def __init__(self):
        pass


    @classmethod
    def define_hands(cls):
        """
        """
        straightFlush = lambda cardSuits, cardRanks : len(set(cardSuits)) == 1 and len(set(cardRanks)) == 5 and max(cardRanks) - min(cardRanks) == 4
        fourOfAKind = lambda cardSuits, cardRanks : len(set(cardRanks)) == 2 and cardRanks.count(cardRanks[0]) == 1 or cardRanks.count(cardRanks[0]) == 4
        fullHouse = lambda cardSuits, cardRanks : len(set(cardRanks)) == 2 and cardRanks.count(cardRanks[0]) == 2 or cardRanks.count(cardRanks[0]) == 3
        flush = lambda cardSuits, cardRanks : len(set(cardSuits)) == 1
        straight = lambda cardSuits, cardRanks : len(set(cardRanks)) == 5 and max(cardRanks) - min(cardRanks) == 4
        threeOfAKind = lambda cardSuits, cardRanks : len(set(cardRanks)) == 3 and cardRanks.count(cardRanks[0]) == 3
        twoPairCheck = lambda cardSuits, cardRanks : len(set(cardRanks)) == 3 and cardRanks.count(cardRanks[0]) == 2
        pairCheck = lambda cardSuits, cardRanks : len(set(cardRanks)) == 3 and cardRanks.count(cardRanks[0]) == 2

        if len(cls.hands) == 0:
            cls.hands.append([
                ("Straight Flush", straightFlush)
                ,("Four Of A Kind", fourOfAKind)
                ,("Full House", fullHouse)
                ,("Flush", flush)
                ,("Straight", straight)
                ,("Three Of A Kind", threeOfAKind)
                ,("Two Pair", twoPairCheck)
                ,("One Pair", pairCheck)
            ])

            # Flattens list from 2d to 1d (e.g. [[elements]] >> [elements])
            cls.hands = [hand for hand in cls.hands[0]]


    @classmethod
    def five_card_draw(cls, cards, player_name="Player"):
        """Returns Tuple (rank of hand [0-7], "Name of Poker hand", High card value [1-13])
        """
        cardRanks = []
        cardSuits = []

        for card in cards:
            cardRanks.append(card.get_rank())
            cardSuits.append(card.get_suit())

        highCard = max(cardRanks)
        
        for hand_rank, poker_hand in enumerate(cls.hands):
            has_poker_hand = poker_hand[1]
            poker_hand_name = poker_hand[0]
            if has_poker_hand(cardSuits, cardRanks):
                print(f"Rank: {hand_rank}, Hand: {poker_hand_name}, High: {highCard}")
                return (hand_rank, poker_hand_name, highCard)

        print(f"Rank: {highCard}, Hand: High Card, High: {highCard}")
        return (highCard, "High Card", highCard)


    @classmethod
    def evaluate_hand(cls, cards, player_name="Player"):
        """
        """
        
        print(f'\n{player_name}, your final hand is: {Fore.MAGENTA}{cards}{Style.RESET_ALL}')

        if cls.variant == "5-Card Draw":
            return cls.five_card_draw(cards, player_name)




