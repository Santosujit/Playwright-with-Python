from OopsDemo import Calculator

#Inheritance is where child class access all the variable and methods
#of Parent class without creating any object of parent class inside child class

class ChildImpl(Calculator):     #ChildImpl class is inheriting Calculator class
                                #thats why the above import statement
                                #or else How this class will know where the Calculator is
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 2, 10)  #in child class calling of parent class constructor
                                                # shud b the 1st statement
                                                #here we are calling the parent class parameterised
                                               #constructor explicitly


    def getCompleteData(self):
        return self.num2 + self.num + self.Summation()


obj = ChildImpl()
print(obj.getCompleteData())


