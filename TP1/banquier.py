# Import math Library
import math


def investment(original, time):
    # Calculate compound interest
    amount = original
    for i in range(time):
        amount = (amount - 1)*time
    
    return amount - 1 

print(investment(math.e, 50))