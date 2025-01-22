""" 

1 # # # 0
# 3 # # #
# # 1 3 #
# 0 # # #

Use a Stack for the shuffled deck (game board after the cards are shuffled) of 4x5 cards using a stack to store them and then "print" from


queue for computer instructions: 

flip chosen card 1, 
flip chosen card 2, 
compare the newly flipped cards,
only reflip if they don't match

Use another data type for storing the game board and the card states

Use a stack of cards to check each "index" one by one and see if we need to update the given card to a true or false flip state

"""

#Main method
import random


def main():
    
    #Build a "shuffled" stack of cards that has 2 of each number in it (0-9 each number occurs twice)
    deck = []
    
    #fill the deck with cards and a flipped state of false
    for i in range(9):
        #Using a list:
        #deck += [(i, False)] * 2
        
        #Using a stack:
        deck.append([(i, False), (i, False)])
        
    random.shuffle(deck)

    #Introduce the game
    
    #Lay out the cards one by one form the stack
    
    #ETC

#If there is a main method, run it
if __name__ == "__main__":
    main()