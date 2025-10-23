from utils.deck import *

def create_player(name :str ='AI') -> dict:
    player = {
        'name':name,
        'hand':[],
        'won_pile':[]
    }
    return player

def init_game()->dict:
    human_player = create_player('Moshe')
    AI_player = create_player()

    # create deck and shuffle
    deck = create_deck()
    deck = shuffle(deck)
    # deals cards
    human_player['hand'] = deck[:26]
    AI_player['hand'] = deck[26:]

    game_dict = {
        'deck':deck,
        'player_1':human_player,
        'player_2':AI_player
    }
    return game_dict

def play_round(p1:dict,p2:dict)-> None:
    hand_player1 = p1['hand']
    hand_player2 = p2['hand']

    # take out top of cards
    # looking at the value
    card_player1 = hand_player1.pop(0)['value']
    card_player2 = hand_player2.pop(0)['value']

    #check who is the winner
    if card_player1 > card_player2 :
        # help function to append two cards to won_pile
        append_two(card_player1,card_player2,p1['won_pile'])
    elif card_player1 < card_player2:
        append_two(card_player1,card_player2,p2['won_pile'])
    return None

# privet function
def append_two(card1,card2,deck):
    deck.append(card1)
    deck.append(card2)
