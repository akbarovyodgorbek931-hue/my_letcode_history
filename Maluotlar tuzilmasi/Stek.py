# # Python'da list yordamida Stek
# stack = []

# # Push — O(1)
# stack.append(1)
# stack.append(2)
# stack.append(3)
# print(stack)        # -> [1, 2, 3]

# # Pop — O(1)
# top = stack.pop()
# print(top)          # -> 3
# print(stack)        # -> [1, 2]

# # Peek — O(1)
# print(stack[-1])    # -> 2

# # Bo'sh ekanligini tekshirish
# print(len(stack) == 0)   # -> False



class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
    def display(self):
        print("Top-", self.items[::-1])

s = Stack()
# s.push(1)
# s.push(2)
# s.push(3)
# s.display()

# print(s.peek())   # Top- [30, 20, 10]
# print(s.pop())     # 30
# print(s.display())  # Top- [20, 10]


def reverse_string(s):
    stack = Stack()
    for char in s:
        stack.push(char)
    result = ""
    while not stack.is_empty():
        result += stack.pop()
    return result

print(reverse_string("Yodgorbek"))