#In Python, function is a group of related statements that perform a specific task.
#Function Declaration

def GreetMe(name):
    print("Good Morning "+name)

def AddIntegers(a, b):
    return a+b
    #Function Call

GreetMe("Rahul Shetty")

print(AddIntegers(2, 3))

#Component	Meaning
#def	Defines a function
#GreetMe	Function name
#name	Parameter to receive the arguments passed from function call
#"Rahul Shetty"	Argument
#print()	Displays output
#return sends a result back to the place where the function was called.

#Concept	Meaning	Example from your code
#Function definition	Creates a function	def GreetMe(name):
#Parameter	Variable receiving an input	name, a, b
#Argument	Actual value passed to a function	"Rahul Shetty", 2, 3
#Function call	Executes a function	GreetMe("Rahul Shetty")
#return	Sends a result back to the caller	return a + b