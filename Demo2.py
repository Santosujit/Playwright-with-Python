values = [1, 2, "rahul", 4, 5]
# List is data type that allows multiple values and can be different data types
#Its just like ArrayList
#Count from zeroth index
#List is square braces
# A list is created using square brackets [].

print("-------------------------List----------------------------")

print(values[0])  # 1

print(values[3])  # 4
print(values[-1])  #5 ,This -1 to print the last value in List
print(values[1:3])  # 2 rahul ,This is kind of substring, 1 to 3, excluding 3
values.insert(3, "shetty")   #[1, 2, 'rahul', 'shetty', 4, 5],on 3rd index it inserted
print(values)
values.append("End")  #[1, 2, 'rahul', 'shetty', 4, 5, 'End'], at the end append function will add value
print(values)

print("Update")
values[2] = "RAHUL" #Updating, this is how u update in Python
print(values)

print("Delete")
del values[0] #This is how you delete in Python

print(values)

# Tuple - Same as LIST Data type but immutable,meaning can't be updated or changed
#Tuple are with round braces
#List with square braces

print("-------------------------Tuple----------------------------")

val = (1, 2, "rahul", 4.5)

print(val[1]) #2

#val[2] = "RAHUL" you can't update value in Tuple its immutable

print(val)

# List = Mutable → You can modify elements after creation.
# Tuple = Immutable → You cannot reassign, add, or remove elements directly after creation.
# Syntax → Lists use [], while tuples generally use ().

print("-------------------------Dictionary----------------------------")

# Dictionary is like Hashmap, key-Value pair
# A dictionary stores data as key-value pairs.
# Dictionaries use curly braces {}.
# Each key is associated with a value.
# Keys are unique within a dictionary.
# Important: If the key already exists,
# assigning a new value updates the existing value instead of adding a duplicate key.
# Get all keys	car.keys()
# Get all values	car.values()

dic = {"a": 2, 4:"bcd", "c": "Hello world"}  #if string in key or value, put in double quote ""
print(dic.keys())  #print all keys
print(dic.values())  #print all values

print(dic[4])   #Its key-value pair not indexes
print(dic["c"])
print(dic)

#
dict = {}

dict["firstname"] = "Rahul"

dict["lastname"] = "shetty"

dict["gender"] = "Male"

print(dict)
print(dict["lastname"])















