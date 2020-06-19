import unittest

from ..classes import Card

class TestCard(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_GetRankForAce(self):
        """
        """

        card = Card('Diamonds', 1)
        value = card.get_rank()
        self.assertEqual('Ace', value)


    def test_GetRankForJack(self):
        """
        """

        card = Card('Diamonds', 11)
        value = card.get_rank()
        self.assertEqual('Jack', value)


    def test_GetRankForQueen(self):
        """
        """

        card = Card('Spades', 12) 
        value = card.get_rank()
        self.assertEqual('Queen', value)


    #TODO: Complete unit test
    def test_GetRankForKing(self):
        """
        """

        card = Card('Hearts', 13)
        value = card.get_rank()
        self.assertEqual('King', value)


    #TODO: Complete unit test
    def test_GetRankForNumberCard(self):
        """
        """

        card = Card('Hearts', 2)
        value = card.get_rank()

        self.assertEqual('2', value)
        self.assertEqual('3', value)
        self.assertEqual('4', value)
        self.assertEqual('5', value)
        self.assertEqual('6', value)
        self.assertEqual('7', value)
        self.assertEqual('8', value)
        self.assertEqual('9', value)
        self.assertEqual('10', value)


    def test_ExpressionForAce(self):
        """
        """

        card = Card('Diamonds', 1)
        value = str(card)
        self.assertEqual('Ace of Diamonds', value)


if __name__ == '__main__':
    unittest.main()