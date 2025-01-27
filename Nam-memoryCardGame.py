import random
from linked_list_array import LinkedList


def main():
    # Build a shuffled deck of cards
    deck = []
    for i in range(1, 10):
        deck.append([i, False])  # [card value, flipped state]
        deck.append([i, False])
    random.shuffle(deck)

    # Distribute the cards into the linked list in groups of 3
    llist = LinkedList()
    while len(deck) > 0:
        append_list = []
        for _ in range(3):
            if deck:
                append_list.append(deck.pop())
        llist.append(append_list)

    # Game loop
    while True:
        print("\nCurrent Board:")
        all_flipped = llist.print_list()  # Print the current state of the game
        if all_flipped:
            print("Congratulations! You've matched all the cards!")
            break
        try:
            # Get player input for card positions
            print("\nPick the first card:")
            card1 = pick_card(llist)
            card2 = pick_card(llist)

            llist.compare([card1, card2])
        except (ValueError, IndexError) as e:
            print(f"Error: {e}. Please try again.")


def pick_card(llist):
    """Helper function to pick a card and handle input validation."""
    while True:
        try:
            input_str = input(
                "Enter the row and column of the card you want to pick (e.g., '1 2'): ")
            # Split input and convert to integers
            row, col = map(int, input_str.split())
            pos = [row, col]  # Store row and column in a list
            return llist.pick(pos)
        except (ValueError, IndexError) as e:
            print(f"Invalid input: {e}. Please try again.")


if __name__ == "__main__":
    main()
