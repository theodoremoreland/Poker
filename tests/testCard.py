import sys
import unittest

sys.path.append("..")
from classes.Card import Card

class TestCard(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.suits = ['Clubs', 'Spades', 'Diamonds', 'Hearts']
        cls.card = Card("Diamonds", 13)

    @classmethod
    def tearDownClass(self):
        pass


    def setUp(self):
        pass


    def tearDown(self):
        pass

    
    def test_should_cast_rank_to_number(self):
        """
        """
        self.assertIsInstance(self.card.get_rank(), int)


    def test_should_get_suit(self):
        """
        """
        self.assertEqual(self.card.get_suit(), "Diamonds")


    def test_should_return_kind_for_ace(self):
        """
        """

        card = Card('Diamonds', 1)
        kind = card.get_kind()
        self.assertEqual('Ace', kind)


    def test_should_return_kind_for_jack(self):
        """
        """

        card = Card('Diamonds', 11)
        kind = card.get_kind()
        self.assertEqual('Jack', kind)


    def test_should_return_kind_for_queen(self):
        """
        """

        card = Card('Spades', 12) 
        kind = card.get_kind()
        self.assertEqual('Queen', kind)


    def test_should_return_kind_for_king(self):
        """
        """

        card = Card('Hearts', 13)
        kind = card.get_kind()
        self.assertEqual('King', kind)


    def test_should_return_kind_for_numbers(self):
        """
        """
        for number in range(2,11):
            card = Card('Hearts', number)
            kind = card.get_kind()
            self.assertEqual(str(number), kind, f"Test failed on number: {number} and kind: {kind}.")


    def test_should_return_all_ranks(self):
        """
        """
        for number in range(1,14):
            card = Card('Hearts', number)
            rank = card.get_rank()
            self.assertEqual(number, rank)


    def test_should_return_expression_for_ace(self):
        """
        """
        for suit in self.suits:
            card = Card(suit, 1)
            kind = str(card)
            self.assertEqual(f'Ace of {suit}', kind, f'Test failed on suit: {suit}')


    def test_should_return_expression_for_jack(self):
        """
        """
        for suit in self.suits:
            card = Card(suit, 11)
            kind = str(card)
            self.assertEqual(f'Jack of {suit}', kind, f'Test failed on suit: {suit}')


    def test_should_return_expression_for_queen(self):
        """
        """
        for suit in self.suits:
            card = Card(suit, 12)
            kind = str(card)
            self.assertEqual(f'Queen of {suit}', kind, f'Test failed on suit: {suit}')


    def test_should_return_expression_for_king(self):
        """
        """
        for suit in self.suits:
            card = Card(suit, 13)
            kind = str(card)
            self.assertEqual(f'King of {suit}', kind, f'Test failed on suit: {suit}')


    def test_should_override_object_representation(self):
        """
        """
        self.assertIsInstance(str(self.card), str)


    def test_should_override_object_equality(self):
        """
        """
        card_1 = Card("Hearts", 13)
        card_2 = Card("Hearts", 13)
        card_3 = Card("Hearts", 12)
        self.assertEqual(card_1, card_2)
        self.assertNotEqual(card_2, card_3)


if __name__ == '__main__':
    unittest.main()