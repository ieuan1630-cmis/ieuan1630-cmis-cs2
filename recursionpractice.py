import math

def countup(n):
    if n == 10:
        print "Blastoff!"
    else:
        print n
        return countup(n+1)

def main():
    return countup(int(raw_input("Pick an integer less than 10: ")))

#main()

def countup_from(start, end):
    if start == end:
        print "Finished"
    else:
        print start
        return countup_from(start + 1, end)

def countdown_from(start, end):
    if start == end:
        print "Finished"
    else:
        print start
        return countdown_from(start - 1, end)

def countup_from_back_to(start, start_changing, end, times): #doesn't work
    if times > 0 and start_changing == start:
        print start
    elif start_changing == end:
        print end
        return countup_from_back_to(start, start_changing - 1, end, times + 1)
    else:
        print start_changing
        return countup_from_back_to(start, start_changing + 1, end, times + 1)


def adder(running_total=0):
    n = raw_input("Next number: ")
    if n == "":
        print "The sum is {}".format(running_total)
    else:
        n = float(n)
        running_total += n
        print "Running Total: {}".format(running_total)
        return adder(running_total)

#adder()

def biggest(biggest_num=None):
    n = raw_input("Next: ")
    if n == "":
        print "The biggest number is {}".format(biggest_num)
    else:
        n = float(n)
        if n > biggest_num:
            biggest_num = n
        return biggest(biggest_num)

#biggest()

def smallest(smallest_num=float("inf")):
    n = raw_input("Next: ")
    if n == "":
        print "The smallest number is {}".format(smallest_num)
    else:
        n = float(n)
        if n < smallest_num:
            smallest_num = n
        return smallest(smallest_num)

#smallest()

def power(x, nth, result):
    if nth == 0:
        print result
    else:
        if result == 0:
            result = x
            return power(x, nth - 1, result)
        else:
            result = result * x
            return power(x, nth - 1, result)

#power(2, 3, 0)

def power(x, n):
    if n == 0:
        return (0,1)
    else:
        x = x*
        return power(x, n-1)



