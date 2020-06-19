# Native
import time
import random
from os import system, name 

# Third party
from colorama import Fore, Back, Style

# Custom
from classes.Card import Card
from classes.Poker import Poker
from classes.Player import Player


def initialize_players():
    """ Prompts players for party size and player names.
    """
    system('cls')
    players = []
    playerCount = input('Enter the numbers of players: ')

    for playerN in range(int(playerCount)):
        playerName = input(f'Enter the name for player {playerN + 1}: ')
        players.append(Player(playerName))

    print("Let's get started!")

    return players


def create_deck():
    """
    """
    deck = []
    suits = ['Clubs', 'Spades', 'Diamonds', 'Hearts']

    for suit in suits:
        for rank in range(1,14):
            deck.append(Card(suit, rank))

    random.shuffle(deck)
    return deck


def players_draw_cards(players, deck):
    """
    """
    players = players.copy()

    # Clears shell / console
    system('cls')

    if len(players) > 0:
        time.sleep(1)
        player = players.pop()
        player.draw_cards(deck)
        player.discard_cards(deck)
        return players_draw_cards(players, deck)

    return None


def rate_players(players):
    """
    """
    players = players.copy()

    if len(players) > 0:
        player = players.pop()
        player_hand = player.get_hand()
        player_name = player.get_name()
        time.sleep(1)
        hand_ranking = Poker.evaluate_hand(player_hand, player_name) # Returns Tuple
        (handRating, description, highCard) = hand_ranking # Unpacks Tuple
        player.updateState(handRating, description, highCard)
        return rate_players(players)

    return None


def determine_winner(players, winningPlayer="", winningHand=14, highCard=0, description=""):
    """
    """
    players = players.copy()
    
    if len(players) > 0:
        player = players.pop()
        if (player.handRating < winningHand):
            winningHand = player.handRating
            highCard = player.highCard
            winningPlayer = player
            description = player.description
        return determine_winner(players, winningPlayer, winningHand, highCard, description)
    
    time.sleep(2)
    print(f"\nWinning Player is {Fore.GREEN}{winningPlayer}{Style.RESET_ALL} who won with a hand of {Fore.GREEN}{*winningPlayer.get_hand(),}{Style.RESET_ALL}, {winningPlayer} had {description}.\n")


def play_game(keepPlaying=True):
    """Begins a round of Poker
    """

    # Base case
    if keepPlaying != True:
        # Clears shell / console
        system('cls')
        print("Game session ceased.")
        return None

    players = initialize_players()
    deck = create_deck()
    players_draw_cards(players, deck)
    Poker.define_hands()
    rate_players(players)
    determine_winner(players)

    keepPlaying = input(f"{Style.BRIGHT}Do you want to play again (Y/N)? {Style.RESET_ALL}").lower().strip() in ["y", "ye", "yes", "yea", "yeah", "ys", "u", "t"]
    return play_game(keepPlaying)

    
if __name__ == '__main__':
    play_game()