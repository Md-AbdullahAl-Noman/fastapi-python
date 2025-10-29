#loops are for iterating over a sequence (like a list, tuple, dictionary, set, or string) 
#use iterator on iterable objects
#syntax : for iterator in iterable:

my_list=[2,4,6,8,10]
for i in my_list:
    print(i)
 

 #while loop going to continue until a certain condition is met
 #continue keyword can be used to skip the current iteration and move to the next one means
#  dont execute the code below continue for this iteration
#break keyword can be used to exit the loop completely
i=0
while(i<10):
    i+=1
    if i==5:
        continue#means skip the rest of the code below and go to next iteration means start from the start of the 
        #loop
    if i==8:
        break#stop the loop completely
    print(i)