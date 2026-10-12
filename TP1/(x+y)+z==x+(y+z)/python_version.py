import random
num_of_cases_not_equal = 0
for i in range(1000000):

    # Generate three random numbers between 0 and 1 (result 82,2%)
    x= random.random()
    y= random.random()
    z =random.random()

    # Generate three random numbers between 1 and 1000000 (result 100%)
    # x= random.randint(1, 1000000)
    # y= random.randint(1, 1000000)
    # z= random.randint(1, 1000000)
    value1 = (x+y)+z

    

    value2 = x+(y+z)
   
    

    if value1 == value2:
        num_of_cases_not_equal += 1

print(f'Percentage of cases where the two values are equal: {num_of_cases_not_equal/1000000*100}%')