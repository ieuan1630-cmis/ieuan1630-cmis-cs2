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

def largest_palindrome_from_3digitproducts(test=999):
    large_num = test * (test-1)
    if palindrome(str(large_num)) == True:
        return large_num
    else:
        return largest_palindrome_from_3digitproducts(test-1)

print largest_palindrome_from_3digitproducts()


