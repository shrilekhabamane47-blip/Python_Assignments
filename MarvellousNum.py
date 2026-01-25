import math
def ChkPrime(num):  
    if num <= 1:
        return False
    #for i in range(2, int(num**0.5) + 1):
    for i in range(2, int(math.sqrt(num)) + 1) :
        if num % i == 0:
            return False
    return True
