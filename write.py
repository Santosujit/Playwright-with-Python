
# Read file and store all the contents in a List
# Reverser the List
# Write the reversed List into the

with open("test.txt", "r") as reader:  #r specifies read mode opening of the file
                                       #reader object
                                       #if u don't write r also it treats as Read mode
    content =  reader.readlines() #it will store in a list
    reversed(content)             #List in reverse order now

    with open("test.txt", "w") as writer:   #explicitly mention w for write mode
        for line in reversed(content):
            writer.write(line)