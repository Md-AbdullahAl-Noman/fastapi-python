#set are unorder collection of unique items , they dont allow duplicate values,
# they can be in any position in memory so no indexing and thus unordered
#  and use {}

my_set={"noman",2,3,3,5,5,True}#set with multiple data types
print(my_set)#it will remove duplicate values
#adding element to set
my_set.add("al abdullah")
print(my_set)
#update method to add multiple elements to set
my_set.update([55,66])
print(my_set)
#remove by using discard method
my_set.discard(5)
print(my_set)
#remove all elements by using clear method
my_set.clear()
print("set after removing all elements",my_set)
