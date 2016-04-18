import math

def in_range_or_not(n):
    if n < 0.0 or n >= 10.0:
        return False
    elif n >= 0.0 and n < 10.0:
        return True

def print_in_range_or_not(n):
    if in_range_or_not(n) == False:
        print str(n) + " is out of range."


def avg(n0, n1, n2, n3, n4):
    summation = 0
    included = 0
    if in_range_or_not(n0) == True:
        summation = summation + n0
        included = included + 1
    if in_range_or_not(n1) == True:
        summation = summation + n1
        included = included + 1
    if in_range_or_not(n2) == True:
        summation = summation + n2
        included = included + 1
    if in_range_or_not(n3) == True:
        summation = summation + n3
        included = included + 1
    if in_range_or_not(n4) == True:
        summation = summation + n4
        included = included + 1
    avg = summation/(included + 0.0)
    return avg


def even_or_odd(n):
    if float(n/2) == n/2.0:
        return "even"
    elif float(n/2) != n/2.0:
        return "odd"
    

def output(avg, integer_part, even_or_odd):
    print """The average is {}
The integer part of the average is {}.
The integer part is {}.""".format(avg, integer_part, even_or_odd)



def main():
    print """This program will ask you for 5 integer or float values.
It will calculate the average of all values from 0 inclusive to 10 exclusive.
It will print out whether the resulting average is even or odd.
"""
    n0 = float(raw_input("n0: "))
    print_in_range_or_not(n0)
    n1 = float(raw_input("n1: "))
    print_in_range_or_not(n1)
    n2 = float(raw_input("n2: "))
    print_in_range_or_not(n2)
    n3 = float(raw_input("n3: "))
    print_in_range_or_not(n3)
    n4 = float(raw_input("n4: "))
    print_in_range_or_not(n4)
    average = avg(n0, n1, n2, n3, n4)
    integer_part = int(average)
    even_or_not = even_or_odd(int(average))


    output(average, integer_part, even_or_not)

main()

