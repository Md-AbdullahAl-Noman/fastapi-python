#list is a collection of data lets say storing multiple data in a single variable
my_list=["noman",22,3.5,True]#list with multiple data types
people_list=["noman","abdullah","rahim","karim"]#list with string data types
#indexing in list
print(people_list[1])#accessing 2nd element
#slicing means accessing specific range of elements
#negative indexing
print(people_list[-2])
print(people_list[1:4])#accessing from index 1 to index 3,4 is excluded means till index 3
#append method to add element at the end of the list
my_list.append("its me")
print(my_list)
#insert method to add element at specific index
people_list.insert(1,"Sunzim")
print(people_list)
#remove means remove the item itself not the index
my_list.remove(22)
print(my_list)
#pop method removes the item at specific index
people_list.pop(2)
print(people_list)
#len method to find the length of the list
print(len(people_list))
#sort method to sort the list in ascending order
my_list.sort()#it will give error because my_list has multiple data types