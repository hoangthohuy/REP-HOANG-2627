# Import math Library
import math


def investment(original, time):
    # Calculate compound interest
    amount = original
    for i in range(time):
        amount = (amount - 1)*time #mauvais algo, faut écire amont = (amount-1)*i
    
    return amount - 1 

print(investment(math.e, 50))