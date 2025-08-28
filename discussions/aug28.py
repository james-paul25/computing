#data types
#numeric data types (int = (1,2), float = (1.22, -1.3), complex = (combination of numnbers, unofficial data types))
#stringg data type =  (str = collection of characters)

var1 = 1 #numeric
var2 = 'string' #string

print(type(var1))

#list = versatile data structure, can be mixed by any data types

myHobby = ['cubing', 'coding']
print("list: ", myHobby)

#array = import array first, stick to one data type
import array

myArray = array.array("i", [1, 2, 3])
print("my array: ", myArray)

#tuples = fixed collection, cannot be changed
myHobbies = ('coding', 'cubing', 1)
print("tuples: ", myHobbies)

#set = collection of unique, unordered elements, cannot use indexing, {} or set function
fruits = {"apple", "banana", "apple"}
numbers = set([1,2,3])
print("set: ", fruits)
print("set numbers: ", numbers)

#mapping data types
# dict = dictionaries enclosed in {}

#boolean type = bool = true or false


