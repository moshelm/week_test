from game_logic.game import *

def empty_hand(hand):
    """
    check if hand is an empty
    :param hand:
    :return: True or False
    """
    return len(hand) == 0

def play(game:dict):
    # information players
    player1 = game['player_1']
    player2 = game['player_2']
    # hands players
    player1_hand = player1['hand']
    player2_hand = player2['hand']
    # play until one finish hand
    while not empty_hand(player1_hand) and not empty_hand(player2_hand):
        play_round(player1, player2)
    # won pile of players
    player1_won_pile = player1['won_pile']
    player2_won_pile = player2['won_pile']
    # check who own
    if player1_won_pile > player2_won_pile:
        print(f"{player1['name']} won with {len(player1_won_pile)}")
    elif player1_won_pile < player2_won_pile:
        print(f"{player2['name']} won with {len(player2_won_pile)}")
    else:
        print(f'draw {player1_won_pile}')

if __name__ =='__main__':
    game = init_game()
    play(game)


