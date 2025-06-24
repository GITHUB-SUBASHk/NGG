import random

class SmartAI:
    def __init__(self, low, high):
        self.low = low
        self.high = high
        self.first = True

    def guess(self):
        if self.low > self.high:
            return None
        if self.first:
            self.first = False
            return random.randint(self.low, self.high)
        return (self.low + self.high) // 2

    def observe(self, guess, hint):
        if hint == "higher":
            self.low = guess + 1
        elif hint == "lower":
            self.high = guess - 1

    def to_dict(self):
        return {'low': self.low, 'high': self.high, 'first': self.first}

    @staticmethod
    def from_dict(data):
        ai = SmartAI(data['low'], data['high'])
        ai.first = data.get('first', False)
        return ai
