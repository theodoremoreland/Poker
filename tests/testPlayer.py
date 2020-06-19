# Native
import os
import sys
import unittest
from unittest.mock import patch

# Custom
sys.path.append("..")
from classes.Player import Player


class TestPlayer(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.player = Player("Theo")
        cls.player2 = Player("Theo")
        cls.deck = []
        cls.suits = ['Clubs', 'Spades', 'Diamonds', 'Hearts']

        for suit in cls.suits:
            for rank in range(1,14):
                cls.deck.append((suit, rank))


    @classmethod
    def tearDownClass(cls):
        pass


    def setUp(self):
        self.fresh_deck = []

        for suit in self.suits:
            for rank in range(1,14):
                self.fresh_deck.append((suit, rank))


    def tearDown(self):
        pass


    def test_player_should_draw_five_cards(self):
        """
        """
        player = self.player
        player.draw_cards(self.deck)
        player_hand = player._hand
        self.assertEqual(len(player_hand), 5)


    @patch('builtins.input', return_value="1,2,3,4,5")
    def test_player_should_draw_new_hand(self, patch):
        """
        """
        player = self.player
        original_hand = player._hand.copy()
        player.discard_cards(self.deck)
        new_hand = player._hand

        for idx, card in enumerate(original_hand):
            idx = idx - 1
            self.assertNotEquals(card, new_hand[idx], msg=f"Card #{idx+1} = Original hand: {card}, New hand {new_hand[idx]}")
        


    @patch('builtins.input', return_value="1,2,3,4")
    def test_player_should_replace_first_4_cards(self, patch):
        """
        """
        player = self.player
        original_hand = player._hand.copy()
        player.discard_cards(self.deck)
        new_hand = player._hand
        self.assertNotEqual(original_hand[0], new_hand[0], msg=f"First card:\n{original_hand[0]}\n{new_hand[0]}")
        self.assertNotEqual(original_hand[1], new_hand[1], msg=f"Second card:\n{original_hand[1]}\n{new_hand[1]}")
        self.assertNotEqual(original_hand[2], new_hand[2], msg=f"Third card:\n{original_hand[2]}\n{new_hand[2]}")
        self.assertNotEqual(original_hand[3], new_hand[3], msg=f"Fourth card:\n{original_hand[3]}\n{new_hand[3]}")


    @patch('builtins.input', return_value="1,2,3")
    def test_player_should_replace_first_3_cards(self, patch):
        """
        """
        player = self.player
        original_hand = player._hand.copy()
        player.discard_cards(self.deck)
        new_hand = player._hand
        self.assertNotEqual(original_hand[0], new_hand[0], msg=f"First card:\n{original_hand[0]}\n{new_hand[0]}")
        self.assertNotEqual(original_hand[1], new_hand[1], msg=f"Second card:\n{original_hand[1]}\n{new_hand[1]}")
        self.assertNotEqual(original_hand[2], new_hand[2], msg=f"Second card:\n{original_hand[2]}\n{new_hand[2]}")


    @patch('builtins.input', return_value="1,2")
    def test_player_should_replace_first_2_cards(self, patch):
        """
        """
        player = self.player
        original_hand = player._hand.copy()
        player.discard_cards(self.deck)
        new_hand = player._hand
        self.assertNotEqual(original_hand[0], new_hand[0], msg=f"First card:\n{original_hand[0]}\n{new_hand[0]}")
        self.assertNotEqual(original_hand[1], new_hand[1], msg=f"Second card:\n{original_hand[1]}\n{new_hand[1]}")


    @patch('builtins.input', return_value="1")
    def test_player_should_replace_first_card_only(self, patch):
        """
        """
        player = self.player
        original_hand = player._hand.copy()
        player.discard_cards(self.deck)
        new_hand = player._hand
        self.assertNotEqual(original_hand[0], new_hand[0])
        self.assertListEqual(original_hand[1:], new_hand[1:], msg=f"Last four cards:\n{original_hand[1:]}\n{new_hand[1:]}")


    @patch('builtins.input', return_value="n")
    def test_player_should_replace_0_cards(self, patch):
        """
        """
        player = self.player
        original_hand = set(player._hand.copy())
        player.discard_cards(self.deck)
        new_hand = set(player._hand)
        self.assertTrue(original_hand.issubset(new_hand), msg=f"\nOriginal hand: {original_hand}\nNew hand: {new_hand}")


    def test_player_should_update_state(self):
        """
        """
        self.player.updateState(6, "Straight", 10)
        self.assertEqual(self.player.handRating, 6)
        self.assertEqual(self.player.description, "Straight")
        self.assertEqual(self.player.highCard, 10)


    def test_class_should_override_representation(self):
        """
        """
        self.assertEqual(str(self.player), "Theo")


    def test_class_should_override_equality(self):
        """
        """
        self.assertEqual(self.player, self.player2)


    def test_getter_should_return_hand(self):
        """
        """
        self.assertListEqual(self.player.get_hand(), [])


    def test_getter_should_return_name(self):
        """
        """
        self.assertEqual(self.player.get_name(), "Theo")
    

if __name__ == '__main__':
    # buffer suppresses stdout
    unittest.main(buffer=True)