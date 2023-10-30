class Stack:
    def __init__(self):
        self.stack = []

    def push(self, n):
        self.stack.append(n)

    def peek(self):
        if len(self.stack) == 0:
            return "None"
        x = self.stack.pop()
        self.push(x)
        return x

    def pop(self):
        if len(self.stack) == 0:
            return "None"
        return self.stack.pop()


s1 = Stack()
s2 = Stack()
s1.push(1)
s1.push(2)
s2.push("F")
print(s1.stack)
print(s2.stack)
print(s1.peek())
print(s1.stack)
s1.pop()
s1.pop()
print(s1.pop())



