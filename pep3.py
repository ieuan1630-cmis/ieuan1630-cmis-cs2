#Project Euler Problem 3
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
import sys
import math
sys.setrecursionlimit(4000002)

def prime(num, test=2):
    while test != num:
        if num % test == 0:
            return False
        test += 1
    return True

def largest_prime_factor(num, test=2, highest=1):
    while highest == 1: #while no new high prime factor has been found
        if num % test == 0: #if num is divisible by test
            hi_factor = num/test #num divided by test is a high factor of num
            if prime(hi_factor) == True: #if high factor is prime
                highest = hi_factor #it is the highest prime factor
        test += 1
    return highest

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

def main():
    print largest_prime_factor(600851475143)

if __name__=="__main__":
    main()
