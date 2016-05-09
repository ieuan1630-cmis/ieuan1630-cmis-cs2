#Project Euler Problem 3
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
import sys
sys.setrecursionlimit(4000002)

def prime(num, test=2, factors=0):
    while test != num:
        if num % test == 0:
            factors +=1
            return False
        test += 1
    return True

def largest_prime_factor(num, test=2, highest=1):
    while test != num:
        if prime(test) == True: #if test is prime
            if num % test == 0: #and num is divisible by it
                highest = test  #make that number the new highest prime factor
        test += 1
    return highest


print largest_prime_factor(600851475143)

def prime_recursion(num, test=2, factors=0):
    if test == num:
        if factors == 0:
            return True
        else:
            return False
    else:
        if num % test == 0:
            factors +=1
        return prime_recursion(num, test+1, factors)
    pass

def largest_prime_factor_recursion(num, test=2, highest=1):
    if test == num:
        return highest
    elif prime_recursion(test) == False:
        return largest_prime_factor_recursion(num, test+1, highest)
    else: #prime(test) == True
        if num % test == 0:
            highest = test
            return largest_prime_factor_recursion(num, test+1, highest)
        else:
            return largest_prime_factor_recursion(num, test+1, highest)
    pass
