import math

def in_range_or_not(n):
    if n < 0.0 or n >= 10.0:
        return False
    elif n >= 0.0 and n < 10.0:
        return True

def print_in_range_or_not(n):
    if in_range_or_not(n) == False:
        print str(n) + " is out of range."

def avg(nth_time, summation, included, variables):
    if nth_time == (variables + 1):
        average = summation/(included + 0.0)
        return average
    else:
        n = float(raw_input("n" + str(nth_time) + ": "))
        print_in_range_or_not(n)
        if in_range_or_not(n) == True:
            summation = summation + n
            included = included + 1
        return avg(nth_time + 1, summation, included, variables)


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
    average = avg(1, 0, 0, (float(raw_input("How many floats do you want to average: "))))
    integer_part = int(average)
    even_or_not = even_or_odd(int(average))


    output(average, integer_part, even_or_not)

main()

