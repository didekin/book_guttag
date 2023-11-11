class Fifo:
    def __init__(self):
        self.queue = []

    def incoming(self, value):
        self.queue.append(value)

    def outgoing(self):
        if len(self.queue) == 0:
            return None
        self.queue.reverse()
        return self.queue.pop()


F = Fifo()
F.incoming(1)
F.incoming(2)
print(F.outgoing())
print(F.outgoing())
