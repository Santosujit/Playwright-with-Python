greeting = "Good Morning"
a = 4   #No Semicoln at the ene dof statements like used in  Java
#In Python if-else statement there is no {} like in java so indentation matters a lot
if a > 2:    #u v to give a colon
    print(" Condition matches")
    print("second line")
else:        #u v to give a colon
    print("condition do not match")

print("if else condition code is completed") #this statement is independent of if-else
                                             #It will be printed anyway


#for loop
print("----------for loop---------")

obj= [2, 3, 5, 7, 9]
for i in obj:
    print(i*2)


# sum of First Natural numbers 1+2+3+4+5 = 15
print("Sum of 1st 5 Natural Numbers")
#range(i,j) -> i to j-1
summation = 0
for j in range(1, 6):
    summation = summation + j
print(summation)

print("*******************************")

In your below example, range(1, 10, 5) means:
#Start = 1: Begin with 1.
#Stop = 10: Stop before reaching 10.
#Step = 5: Increase the value by 5 each time.

for k in range(1, 10, 5):    #It'll print 1 to 10-1, 1 increasing each time by 5
    print(k)
    print("**************SKIPPING FIRST INDEX*****************")

for m in range(10):     #If you don't give 1st index, Python 'll take it as Zero
    print(m)













