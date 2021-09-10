class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def div(self):
        return abs(self.a - self.b)

    def multi(self):
        return self.a * self.b

    def mod(self):
        return self.a / self.b
