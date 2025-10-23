import random
def create_card(rank:str, suite:str)->dict:

    card = {
        'rank': rank,
        'suite': suite,
        # function to get value of card
        'value':_card_value(rank)
    }
    return card

def compare_cards(p1_card:dict, p2_card:dict)-> str:
    p1_value = p1_card['value']
    p2_value = p2_card['value']
    if p1_value > p2_value:
        return 'p1'
    elif p1_value < p2_value:
        return 'p2'
    elif p1_value == p2_value:
        return  'WAR'
def create_deck()->list[dict]:
    deck = []
    suites = ['H','C','D','S']
    rank = ['J','Q','K','A','2','3','4','5','6','7','8','9','10']

    for suite in suites:
        for degree in rank:
            card = create_card(degree,suite)
            deck.append(card)
    return deck


def shuffle(deck:list[dict])-> list[dict]:
    for i in range(1000):
        index1 = 0
        index2 = 0
        while index1 == index2:
            index1 = random.randint(0, len(deck)-1)
            index2 = random.randint(0, len(deck)-1)
        # swap cards
        deck[index1], deck[index2] = deck[index2], deck[index1]
    return deck





# private function
def _card_value(rank:str) -> int | None:
    if rank.isdigit():
        return int(rank)
    elif rank == 'J':
        return 11
    elif rank == 'Q':
        return 12
    elif rank == 'K':
        return 13
    elif rank == 'A':
        return 14
