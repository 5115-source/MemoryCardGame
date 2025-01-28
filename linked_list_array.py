class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Append a new node with the given data to the linked list."""
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = newNode

    def print_list(self):
        """Print the linked list in a formatted way and return whether all cards are flipped."""
        current_node = self.head
        row = 0
        all_flipped = True  # Track if all cards are flipped
        print("+" + "---+" * 4)  # Top border
        while current_node:
            print(f"| {row} |", end=" ")  # Row number
            for i in range(len(current_node.data)):
                if current_node.data[i][1]:  # If card is flipped
                    # Show card value
                    print(current_node.data[i][0], end=" | ")
                else:
                    all_flipped = False
                    print("#", end=" | ")  # Show hidden card
            print("\n+" + "---+" * 4)  # Bottom border
            row += 1
            current_node = current_node.next
        return all_flipped

    def pick(self, pos):
        """Flip a card at the specified position and return its value."""
        row, col = pos
        # Validate row and column
        if row < 0 or col < 0:
            raise IndexError("Row and column must be non-negative.")
        current_node = self.head
        # Traverse to the specified row
        for _ in range(row):
            if current_node is None:
                raise IndexError("Row out of bounds.")
            current_node = current_node.next
        if current_node is None or col >= len(current_node.data):
            raise IndexError("Column out of bounds.")
        # Flip the card
        if current_node.data[col][1]:
            raise ValueError(" This card is already flipped ")

        current_node.data[col][1] = True
        print(f"Flipped card at row {row}, column {
              col}: {current_node.data[col][0]}")
        self.print_list()
        return current_node.data[col]

    def compare(self, cards):
        """Compare two flipped cards. If they don't match, flip them back."""
        if len(cards) != 2:
            raise ValueError("Exactly two cards are required for comparison.")
        if cards[0][0] != cards[1][0]:  # If cards don't match
            print("Cards do not match. Flipping them back.")
            cards[0][1] = False
            cards[1][1] = False
        else:
            print("Cards match!")
