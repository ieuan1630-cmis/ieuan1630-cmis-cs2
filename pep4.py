#Project Euler Problem 4
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

def palindrome(test):
    while len(test) > 2:
        if test[0] == test[(len(test)-1)]:
            test = test.rstrip(test[(len(test)-1)])
            test = test.lstrip(test[0])
        else:
            return False
    if test[0] == test[(len(test)-1)]:
        return True

#print palindrome(str(98089))

def largest_palindrome_from_3digitproducts():
    hi_p = 0
    t1 = 999
    t2 = 999
    while t2 >=1:
        test = t1*t2
        if palindrome(str(test)) == True and test > hi_p:
            hi_p = test
        t2 -=1
    t1 -=1
    if t1 == 0:
        return hi_p

def largest_palindrome_from_3digitproductsr(test=999): #with recursion (doesn't work yet) (semantic error cos only 999*999 and 999*998 not 999*997)
    large_num = test * test
    large_num2 = test * (test-1)
    if palindrome(str(large_num)) == True:
        return large_num
    elif palindrome(str(large_num2)) == True:
        return large_num2
    else:
        return largest_palindrome_from_3digitproductsr(test-1)

print largest_palindrome_from_3digitproducts()

"""
print 9*9 #highest square #digits involved 1
print 9*8 #new number times highest #because old digits finished, add new digit
print 8*8 #new squared #multiply involved digit by all involved hi to low
print 9*7 #new digit times highest
print 8*7#new times next highest
print 9*6#new2 times highest
print 7*7#new squared #new2 now new
print 8*6#new times next highest
print 9*5#
print 7*6
print 8*5
print 6*6
print 9*4
print 7*5
print 8*4
print 6*5
print 7*4
print 9*3
print 5*5
print 8*3
print 6*4
print 7*3
print 5*4
print 9*2
print 6*3
print 8*2
print 4*4
print 5*3
print 7*2
print 6*2
print 4*3
print 5*2
print 9*1
print 3*3
print 8*1
print 4*2
print 7*1
print 6*1
print 3*2
print 5*1
print 4*1
print 2*2
print 3*1
print 2*1
print 1*1 """