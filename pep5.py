#Project Euler Problem 5
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def div_1to20(test):
    t1 = 20
    while t1 >= 11:
        if test % t1 != 0:
            return False
        else:
            t1 -=1
    return True

#print div_1to20(2520)


def small_pos_div1to20(test=2520):
    while div_1to20(test) == False:
        #print test
        test +=20
    return test

print small_pos_div1to20()
