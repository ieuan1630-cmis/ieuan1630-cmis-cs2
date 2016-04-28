#Project Euler Problem 1
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.



def main(n, summation):
    if n == 0:
        return summation
    else:
        if n % 3 == 0 or n % 5 == 0:
            summation += n
        return main(n-1, summation)

print main(10, 0)
