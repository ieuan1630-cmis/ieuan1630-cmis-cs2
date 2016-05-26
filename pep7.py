#Project Euler Problem 7
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?

def prime(num, test=2):
    while test != num:
        if num % test == 0:
            return False
        test += 1
    return True

def nth_prime(n, t1=2, primes=0):
    while primes != n:
        if prime(t1) == True:
            primes +=1
        t1 +=1
    return t1 -1

print nth_prime(10001)
