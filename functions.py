#use def to define a function
#name of the funciton and parentheses are mandatory to define a function
#then a colon :
#the parameters can be confusing so we can explicitly the arguments while calling the function
def calculations(max,min):
    print(f"the maximum is {max} and minimum is {min}")

#calling the function
# call(1,10)#but this can be confusing as 1 is assigned to max and 10 to min
#to avoid confusion we can explicitly mention the parameters while calling the function
calculations(min=1,max=10)

###functions calling other functions
def my_total_salary_per_year(salary):
    return salary*12

def identity(name,age,salary_per_month):
    totalSalary=my_total_salary(salary_per_month)
    print(f"Hello {name}, your age is {age} and your total salary is {totalSalary}")

identity("Abdullah",25,50000)