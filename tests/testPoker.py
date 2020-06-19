# Native
import sys
import unittest
from unittest.mock import patch

# Third party


# Custom
sys.path.append("..")
from classes.Card import Card
from classes.Poker import Poker
from classes.Player import Player


class TestPoker(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.Poker = Poker()
        cls.poker_hands = [
                            "Straight Flush"
                            ,"Four Of A Kind"
                            ,"Full House"
                            ,"Flush"
                            ,"Straight"
                            ,"Three Of A Kind"
                            ,"Two Pair"
                            ,"One Pair"
                            ]

        cls.test_cards = {"Straight Flush": [Card("Hearts" , 7), Card("Hearts", 8), Card("Hearts", 9), Card("Hearts", 10), Card("Hearts", 11)]
                            ,"Four Of A Kind": [Card('Spades' , 7), Card('Spades', 7), Card('Spades', 7), Card('Spades', 7), Card('Spades', 1)]
                            ,"Full House": [Card('Spades', 13), Card('Spades', 13), Card('Spades', 12), Card('Spades', 12), Card('Spades', 12)]
                            ,"Flush": [Card("Hearts", 1), Card("Hearts", 2), Card("Hearts", 3), Card("Hearts", 5), Card("Hearts", 6)]
                            ,"Straight": [Card("Spades" , 7), Card("Hearts", 8), Card("Diamonds", 9), Card("Clubs", 10), Card("Hearts", 11)]
                            ,"Three Of A Kind": [Card("Clubs", 12), Card("Clubs", 12), Card("Clubs", 12), Card("Clubs", 13), Card("Clubs", 11)]
                            ,"Two Pair": [Card("Clubs", 12), Card("Clubs", 12), Card("Clubs", 13), Card("Clubs", 13), Card("Clubs", 11)]
                            ,"One Pair": [Card("Clubs", 12), Card("Clubs", 12), Card("Clubs", 13), Card("Clubs", 1), Card("Clubs", 11)]
                            }

    @classmethod
    def tearDownClass(cls):
        pass


    def setUp(self):
        pass


    def tearDown(self):
        pass
    

    def test_class_should_assign_all_poker_hands(self):
        """
        """
        self.Poker.define_hands()
        poker_hands = [hand[0] for hand in self.Poker.hands]
        self.assertListEqual(poker_hands, self.poker_hands)


    def test_class_should_accurately_evaluate_hand(self):
        """
        """
        sf = Poker.evaluate_hand(self.test_cards["Straight Flush"])[1]
        foac = Poker.evaluate_hand(self.test_cards["Four Of A Kind"])[1]
        fh = Poker.evaluate_hand(self.test_cards["Full House"])[1]
        f = Poker.evaluate_hand(self.test_cards["Flush"])[1]
        s = Poker.evaluate_hand(self.test_cards["Straight"])[1]
        toak = Poker.evaluate_hand(self.test_cards["Three Of A Kind"])[1]
        tp = Poker.evaluate_hand(self.test_cards["Two Pair"])[1]
        op = Poker.evaluate_hand(self.test_cards["One Pair"])[1]

        self.assertEqual(sf, "Straight Flush")
        self.assertEqual(foac, "Four Of A Kind")
        self.assertEqual(fh, "Full House")
        self.assertEqual(f, "Flush")
        self.assertEqual(s, "Straight")
        self.assertEqual(toak, "Three Of A Kind")
        self.assertEqual(tp, "Two Pair")
        self.assertEqual(op, "One Pair")


if __name__ == '__main__':
    # buffer suppresses stdout
    unittest.main()
