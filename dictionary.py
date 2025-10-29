#dictionary is a collection of key value pairs
#use {} to create dictionary
#dictionary is mutable means we can change the value of the key
#dictionary is unorder collection of data
#dictionary is mutable means we can change the value of the key
my_dict1={
    "name":"Abdullah",
    "age":22,
    "city":"Copenhagen"
}
print(my_dict1)
#get the keys only
for key in my_dict1.keys():#or values() to get only values of the dictionaries
    print("key:",key)
#accessing value using key
print(my_dict1["name"])
#adding new key value pair
my_dict1["country"]="Denmark"
print(my_dict1)
#to use new dictionary without modifying the original dictionary we can use copy() method
my_dic2=my_dict1.copy()
my_dic2["name"]="Noman"
print(my_dic2)
print(my_dict1)
#loop key value by using items() as items method returns key value pair
for key,value in my_dict1.items():
    print(f"key: {key} and value: {value}")