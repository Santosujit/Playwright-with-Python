
#we want to read the text file present in same hieracrhy of this file
file  = open('test.txt')  #file object has knowledge of all the contents of this .txt filke
#print(file.read()) #It will print all the contents of the .txt file

print("***************")

#print(file.read(5))  #it will print 1st 5-1 characters of the text file counting space too

#print(file.readline())   #It'll print line by line in text file
#print(file.readline())   #cursor will move to next line and print it
#But for 100 lines u can't write so many 100 readLine right

# line = file.readline() #store cotents in line object
# while line != "":     #when this condition become false, exits the loop
#     print(line)
#     line = file.readline() #it will go to next line
# file.close()

#print(file.read())  entire content of the file will be read

#readLine() vs readLines()

lines = file.readlines()  #It stores the values in a List, iteration becomes easy
for i in lines:
    print(i)

# So we saw readLine with while loop and readLines with for loop
file.close()    #always close the file which had opened or else memory leakage will happen
