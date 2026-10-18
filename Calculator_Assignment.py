# Objective: Create a basic calculator class to perform addition, subtraction, multiplication,
# and division.
# Instructions:
# Create a class named BasicCalculator.
# Define a constructor that initializes two numbers. Use numbers 10 & 5
# Implement methods for:
# Addition
# Subtraction
# Multiplication
# Division
# Each method should return the result of the operation.
# Create an instance of the BasicCalculator class and demonstrate the functionality of each method.
# Example Output:
# Addition: 10 + 5 = 15
# Subtraction: 10 - 5 = 5
# Multiplication: 10 * 5 = 50
# Division: 10 / 5 = 2.0

class BasicCalculator():
    def __init__(self):  #self refers to the newly created calculator object.
        self.num1 = 10
        self.num2 = 5
    def Addition(self):
        return(self.num1+self.num2)
    def Substraction(self):
        return self.num1 - self.num2
    def Multiplication(self):
        return self.num1 * self.num2
    def Division(self):
        return self.num1 / self.num2

# self refers to the current object of a class.
# It allows an object to access its own variables (attributes) and methods.
# Class = A blueprint for creating calculators.
# Object = An actual calculator created from that blueprint.
# self = A reference to the particular calculator object being used.
# self refers to the newly created calculator object.
# Important: You write self.num1 inside the class,
# but you use calculator.num1 outside the class to access the same attribute.
# calculator1 = BasicCalculator(10, 5)
# calculator2 = BasicCalculator(20, 30)
# Think of self as saying:
# self = calculator1: Use calculator1's data.
# self = calculator2: Use calculator2's data.
# self refers to the current object.
# self.variable lets you store or access data belonging to that object.
# Python automatically passes the calling object as self when you call an instance method.
#self is like this keyword we used in java

# The object calling the method determines what self refers to.


calculator = BasicCalculator()

print(f"Addition:{calculator.num1}+{calculator.num2}={calculator.Addition()}")
print(f"Addition:{calculator.num1}-{calculator.num2}={calculator.Substraction()}")
print(f"Addition:{calculator.num1}*{calculator.num2}={calculator.Multiplication()}")
print(f"Addition:{calculator.num1}/{calculator.num2}={calculator.Division()}")

# The letter f before the quotation marks indicates an f-string (formatted string literal).
# It allows you to insert Python variables, attributes, expressions
# and expressions directly into a string using curly braces {}.