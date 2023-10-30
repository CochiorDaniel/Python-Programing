class Queue:
    def __init__(self):
        self.queue = []

    def push(self, n):
        self.queue.append(n)

    def peek(self):
        if len(self.queue) == 0:
            return "None"
        x = self.queue[0]
        return x

    def pop(self):
        if len(self.queue) == 0:
            return "None"
        return self.queue.pop(0)


q1 = Queue()
q2 = Queue()
q1.push(1)
q1.push(2)
q1.push(3)
q2.push("A")
q2.push("B")
q2.push("C")
print(q1.queue)
print(q2.queue)
print(q2.peek())
print(q2.queue)
q2.pop()
q2.pop()
q2.pop()
print(q2.pop())
print(q2.peek())
