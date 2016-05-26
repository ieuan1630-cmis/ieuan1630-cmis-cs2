#Project Euler Problem 6
#The sum of the squares of the first ten natural numbers is,
#12 + 22 + ... + 102 = 385
#The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)2 = 552 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the sqaure of the sum is 3025 - 385 = 2640.
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def square_of_sum(num, summation=0):
    while num >=1:
        summation += num
        num -=1
    return summation**2

def sum_of_squares(num, summation=0):
    while num >=1:
        summation += num**2
        num -=1
    return summation


def dif_sqsum_sumsq(num):
    return square_of_sum(num) - sum_of_squares(num)

print dif_sqsum_sumsq(100)
    
