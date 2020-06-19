class Card():

    def __init__(self, suit, rank):
        self._suit = suit
        self._rank = int(rank)


    def __eq__(self, other):
        """
        """
        if isinstance(other, Card):
            return f"{self._suit}{self._rank}" == f"{other._suit}{other._rank}"
        return False


    def __repr__(self):
        return f"{self.get_kind()} of {self.get_suit()}"


    def get_rank(self):
        return self._rank


    def get_kind(self):
        """ 2-10 are just numbers
        """
        if self._rank == 1:
            return 'Ace'
        elif self._rank == 11: 
            return 'Jack'
        elif self._rank == 12: 
            return 'Queen'
        elif self._rank == 13: 
            return 'King'
        else:
            return str(self._rank)


    def get_suit(self):
        return self._suit