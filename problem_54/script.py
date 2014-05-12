#!env/bin/python

import helpers as h
from pokereval.card import Card
from pokereval.hand_evaluator import HandEvaluator

# http://www.suffecool.net/poker/evaluator.html

#+--------+--------+--------+--------+
#|xxxbbbbb|bbbbbbbb|cdhsrrrr|xxpppppp|
#+--------+--------+--------+--------+

#p = prime number of rank (deuce=2,trey=3,four=5,...,ace=41)
#r = rank of card (deuce=0,trey=1,four=2,five=3,...,ace=12)
#cdhs = suit of card (bit turned on based on suit of card)
#b = bit turned on depending on rank of card

#High Card: Highest value card.
#One Pair: Two cards of the same value.
#Two Pairs: Two different pairs.
#Three of a Kind: Three cards of the same value.
#Straight: All cards are consecutive values.
#Flush: All cards of the same suit.
#Full House: Three of a kind and a pair.
#Four of a Kind: Four cards of the same value.
#Straight Flush: All cards are consecutive values of same suit.
#Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

faces = {'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14}
suits = {'S': 1,
    'H': 2,
    'D': 3,
    'C': 4}

def get_winner(l1,l2):
    hands = {'A': [], 'B': []}
    for card in l1:
        v = card[0]
        if v in faces:
            v = faces[v]
        else:
            v = int(v)
        s = suits[card[1]]
        hands['A'].append(Card(v,s))
    for card in l2:
        v = card[0]
        if v in faces:
            v = faces[v]
        else:
            v = int(v)
        s = suits[card[1]]
        hands['B'].append(Card(v,s))

    evaluator = HandEvaluator.Five
    rank1 = evaluator.evaluate_rank(hands['A'])
    rank2 = evaluator.evaluate_rank(hands['B'])

#    hole1 = hands['A'][0:2]
#    hole2 = hands['B'][0:2]
#    board1 = hands['A'][2:]
#    board2 = hands['B'][2:]
#    score1 = HandEvaluator.evaluate_hand(hole1,board1)
#    score2 = HandEvaluator.evaluate_hand(hole2,board2)
    if rank1 < rank2:
        return 1
    else:
        return 0




    

f = open('poker.txt','r')
c = 0
for x in f:
    l = x.replace('\n','').split(' ')
    l1 = l[0:5]
    l2 = l[5:]
    c += get_winner(l1,l2)
print c

f.close()
    
