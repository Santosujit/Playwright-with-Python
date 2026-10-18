#self keyword is mandatory for calling instance or class variable names into method
#Class variables can be called using Class name also
#instance and class variables have whole different purpose
#Class variables for different objects remain same
#However instance variables for different objects are different
#constructor name should be __init__
#new keyword is not required in Python when you create object
#Return type is not needed in Python
#Flower braces are not allowed in Python e.g. {}
#when you create object of the class, and there is no parameterised Constructor
#then Default Constructor is called by default
#To call the methods you have to come outside of the Class

class Calculator:
    num = 100  #class variables
    #default constructor

    def __init__(self, a, b):   #Two parametsrs don't calculate Self as a parameter
        self.firstNumber = a
        self.secondNumber = b
        print("I am called automatically when object is created")

    def getData(self):
        print("I am now executing as method in class")

    def Summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num


obj = Calculator(2, 3)   #run time we are passing values
obj.getData()
print(obj.Summation())

print("**************************")

obj1 = Calculator(4, 5)
obj1.getData()
print(obj1.Summation())



