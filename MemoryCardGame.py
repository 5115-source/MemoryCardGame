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
import random

#Linked list class
class Node:
    def __init__(self, data=None):
        # Data stored in the node
        self.data = data
        # Reference to the next node in the singly linked list
        self.next = None


def main():
    #ChatGPT helped with instructions and understanding python formatting and problem solving
    print("The memory card game, also known as Concentration, is a card-matching game where all cards are laid face down.")
    print("You will take turns flipping over two cards at a time, trying to find matching pairs.")
    print("The goal is to remember the locations of cards to match them and collect pairs until all cards are matched.")
    print("Once you match all the cards and have none flipped upside down you win!\n")
    
    deck = deckBuilder()
    head = None
    gameRunning = True
    
    #Assemble gameboard
    while deck:
        gameBoard(head, deck)
    
    while gameRunning == True:
        inputChecker(deck)
        #gameBoard(head, deck)
        
    #if all cards are flipped stop the game and add a congratulations message
    
#Build a "shuffled" stack of 20 cards that has 2 of each symbol in it in it
def deckBuilder():
    deck = []
    
    # List of 2 of each symbol that will be used as pairs of cards
    symbols = ['!', '@', '#', '$', '%', '<', '&', '*', '>', '+', 
               '!', '@', '#', '$', '%', '<', '&', '*', '>', '+']
    random.shuffle(symbols)

    #List of numbers from 1 - 20
    numbers = list(range(1, 21))

    for symbol in symbols:
        deck.append((symbol, numbers.pop()))
    
    return(deck)

def gameBoard(head, deck):
    currentCard = Node(deck.pop())
    currentCard.next = head
    
    cardNumber = currentCard.data[1]
    if isinstance(cardNumber, int):
        if cardNumber > 9:
            print(f"{cardNumber}", end = "  ")
        else:
            print(f" {cardNumber}", end = "  ")
    else: 
        print(f" {currentCard.data[0]}", end = "  ")
        
    #If length of the stack is divisible by 5 start a new row
    if len(deck) % 5 == 0:
        print("\n")
        
#Unfinished
def inputChecker(deck):
    cardFlip1 = input("What is the number of the first card you want to flip?")
    while not cardFlip1.isdigit() or not 1 <= int(cardFlip1) <= 20:
        cardFlip1 = input("Sorry that wasn't an integer number between 1-20. What is the number (1-20) of the first card you want to flip?")
    
    cardFlip2 = input("What is the number of the second card you want to flip?")
    while not cardFlip2.isdigit() or not 1 <= int(cardFlip2) <= 20:
        cardFlip2 = input("Sorry that wasn't an integer number between 1-20. What is the number (1-20) of the second card you want to flip?")

    #Flip both cards
    
    #Display the gameboard

    if cardFlip1 != cardFlip2:
        #Flip the cards back
        #Display the gameboard
        print()

    return deck


#If there is a main method, run it
if __name__ == "__main__":
    main()