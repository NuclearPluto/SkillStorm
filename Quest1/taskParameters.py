class Calculator:
    def __init__(self, input1, input2):
        self.input1 = input1
        self.input2 = input2

    def add(self):
        return self.input1 + self.input2
    
    def subtract(self):
        return self.input1 - self.input2
    
    def multiply(self):
        return self.input1 * self.input2
    
    def divide(self):
        return self.input1 / self.input2
    
test = Calculator(10, 20)
print(test.add())
print(test.subtract())
print(test.multiply())
print(test.divide())