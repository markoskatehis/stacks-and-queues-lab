import random

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def select_and_announce_winner(self):
        """
        Randomly selects a winner from the queue.
        Dequeues all customers up to AND including the winner.
        Returns the name of the winning customer.
        """
        if self.is_empty():
            return None

        winner = random.choice(self.items)

        removed = []
        while True:
            customer = self.dequeue()
            removed.append(customer)
            if customer == winner:
                break

        return winner
