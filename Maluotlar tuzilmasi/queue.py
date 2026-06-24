class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
    def display(self):
        print("Old- ", self.items, "_Orqaga")

# ishlatish
# q = Queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# q.display()

# print(q.peek())  
# print(q.dequeue)
# q.display()



# q=Queue()
# q.enqueue("Ali")
# q.enqueue("Bob")
# q.enqueue("Sara")

# while not q.is_empty():
#     print(f"ximat korsatilmoqchi: {q.dequeue()}")