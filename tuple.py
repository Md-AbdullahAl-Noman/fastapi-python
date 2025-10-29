#tuples are like lists but they are immutable 
#use () to create tuples
#tuples items can be accessed by index like lists
#tuples supports slicing too
#tuples are faster than lists because of immutability
#use tuples when data is not supposed to be changed

my_tuple=("noman","is ",100)
print(my_tuple[1])#accessing 2nd element
print(my_tuple[-1])#accessing last element using negative indexing
print(my_tuple[0:2])#slicing from index 0 to index 1
# my_tuple.[0]="abdullah"#this will give error because tuples are immutable