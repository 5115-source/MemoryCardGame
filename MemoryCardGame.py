""" 

1 # # # 0
# 3 # # #
# # 1 3 #
# 0 # # #

Use a Stack for the shuffled deck (game board after the cards are shuffled) of 4x5 cards using a stack to store them and then "print" from


might use queue for computer instructions: 

flip chosen card 1, 
flip chosen card 2, 
compare the newly flipped cards,
only reflip if they don't match

Use another data type for storing the game board and the card states

Use a stack of cards to check each "index" one by one and see if we need to update the given card to a true or false flip state

"""

#Main method
import random

#Linked list class
class Node:
    def __init__(self, data=None):
        # Data stored in the node
        self.data = data
        # Reference to the next node in the singly linked list
        self.next = None


def main():
    #Need to create a more instructive introduction
    print("Welcome to the memory card game!")
    
    deck = deckBuilder()
    #print(deck)

    #win = False

    head = None
    
    
    #while win != True:
    
    #While the deck still has cards create and print the game board
    while deck:
        gameBoard(head, deck)
        
    inputChecker(deck)
    
#Build a "shuffled" stack of cards that has 2 of each number in it (0-9 each number occurs twice)
def deckBuilder():
    deck = []
    
    """#fill the deck with cards and a flipped state of false
    for i in range(10):
        #Using a stack to add a pair of each number to the deck
        deck.append((i, False))
        deck.append((i, False))
    random.shuffle(deck)
    return(deck)"""
    
    # List of symbols that will be use for pairs of cards
    symbols = ['!', '@', '#', '$', '%', '<', '&', '*', '>', '+']

    #Using a stack to add a pair of each symbol to the deck
    number = 20
    for symbol in symbols:
        #Need to adjust to get the numbers in order and have the symbols in random order
        deck.append((symbol, number))
        number -= 1
        deck.append((symbol, number))
        number -= 1
    random.shuffle(deck)
    #For troubleshooting
    print(deck)
    return(deck)

def gameBoard(head, deck):
    currentCard = Node(deck.pop())
    currentCard.next = head
    
    cardNumber = len(deck) + 1
    if isinstance(currentCard.data[1], int):
        if cardNumber > 9:
            print(f"{cardNumber}", end = " ")
        else:
            print(f" {cardNumber}", end = " ")
    else: 
        print(f" {currentCard.data[0]}", end = " ")
        
    #If length of the stack is divisible by 5 start a new row
    if len(deck) % 5 == 0:
        print()
        
#Unfinished
def inputChecker(deck):
    card1 = input("What is the number of the first card you want to flip?")
    #Update that card to have a flipped state of true
    
    card2 = input("What is the number of the second card you want to flip?")
    #Update that card to have a flipped state of true

    return deck


#If there is a main method, run it
if __name__ == "__main__":
    main()