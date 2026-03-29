class Number:
    def __init__(self, value):
        self.value = value
    def __add__(self, other):
        return Number(self.value + other.value)
    def display(self):
        print("Value:", self.value)
num1 = Number(10)
num2 = Number(20)
num3 = num1 + num2
num3.display()
        