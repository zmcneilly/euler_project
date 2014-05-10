#!env/bin/python

import helpers as h

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

def get_winner(l1,l2):
    lv1 = [n[0] for n in l1]
    ls1 = [n[1] for n in l1]
    results = {}
    values = {
        '1' : 13,
        '2' : 12,
        '3' : 11,
        '4' : 10,
        '5' : 9,
        '6' : 8,
        '7' : 7,
        '8' : 6,
        '9' : 5,
        'T' : 4,
        'J' : 3,
        'Q' : 2,
        'K' : 1,
        'A' : 0}
    suits = {
        'C' : 0,
        'D' : 1,
        'H' : 2,
        'S' : 3}
    for l in [l1,l2]:
        rf = True
        fsuit = None
        sf = True
        foak = True
        fh = True
        f = True
        s = True
        toak = True
        tp = True
        op = True
        hc = 0
        for c in l:
            cad = list('00000000000000')
            card[values[c[0]]] = '1'
            suit = list('0000')
            suit[suits[c[1]]] = '1'
            if values[c[0]] > 4:
                rf = False
            if fsuit != None and fsuit != c[1]:
                rf = False
                f = False
            elif fsuit == None:
                fsuit = c[1]
            if 
            




    

f = open('poker.txt','r')

for x in f:
    l = x.replace('\n','').split(' ')
    l1 = l[0:5]
    l2 = l[5:]
    get_winner(l1,l2)


f.close()
    
