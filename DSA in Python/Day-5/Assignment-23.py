#DSA-Tryout
'''BEST Question solved till now!!'''
import random
other=['J','K','Q','A']
deck=['C','D','H','S']
def generate_cards_per_type(card_type):
    l=[card_type+str(i) for i in [j for j in range(2,11)]+other]
    return l
    
def generate_card_deck():
    l=[]
    for i in deck:
        l.extend(generate_cards_per_type(i))
    return l

def shuffle_card_deck(cards_list):
    '''
        Alternative way of shuffling cards deck is:
        random.shuffle(cards_list)
    '''
    '''As per the given question: '''
    new_cards_list=cards_list.copy()
    while(new_cards_list):
       r1 = random.choice(new_cards_list)
       new_cards_list.remove(r1)
       r2 = random.choice(new_cards_list)
       new_cards_list.remove(r2)
       i1=cards_list.index(r1)
       i2=cards_list.index(r2)
       cards_list[i1]=r2
       cards_list[i2]=r1
    return cards_list
       
def cardSort(val):
    i=deck.index(val[0])*20
    if val[1:] in other:
        j=other.index(val[1:])+11
    else:
        j=int(val[1:])
    return (i+j)
    
def sort_cards_of_each_player(card_list):
    card_list.sort(key=cardSort, reverse=True)
    return card_list
def allocate_cards_to_players(cards_list):
    dictionary={
        'player1': [],
        'player2': [],
        'player3': [],
        'player4': []
    }
    for index,value in enumerate(cards_list):
        dictionary['player'+str((index%4)+1)].append(value)
    return dictionary

def prepare_cards():
    cards_list = generate_card_deck()
    new_cards_list = shuffle_card_deck(cards_list)
    dictionary= allocate_cards_to_players(new_cards_list)
    
    for i in range(1,5):
        dictionary['player'+str(i)]=sort_cards_of_each_player(dictionary['player'+str(i)])
    # print(dictionary['player3'])
    
    ''' Card-SA is at the highest priority. Hence it always remains at the 0th index of all the deck'''
    for i in range(1,5):
        # print(dictionary['player'+str(i)][0])
        if "SA" in dictionary['player'+str(i)]:
            return 'player'+str(i)

first_player=prepare_cards()
print(first_player)
'''Used for testng purpose'''
# # print("The first player is:",first_player)
# # print(generate_cards_per_type('C'))
# cards_list = generate_card_deck()
# # print(cards_list)
# new_cards_list = shuffle_card_deck(cards_list)
# # print(new_cards_list)
# dictionary= allocate_cards_to_players(new_cards_list)
# # print(dictionary)
# # print(dictionary['player1'])
# sorted_cards = sort_cards_of_each_player(['H9', 'H6', 'SK', 'SQ', 'D3', 'S7', 'C4', 'H3', 'S9', 'S8', 'C5', 'D9', 'D6'])

# print("sorted: "+str(sorted_cards))
