#function:
def print_n(txt, num_of_times):
    txt = txt.replace("\n", " ")
    n = num_of_times
    x = "count"*n
    if num_of_times <= 0:
        return
    print txt + str(n) + str(x)
    n = n-1
    print_n(txt, num_of_times -1)

def print_n2(txt, num_of_times):
    txt = txt.replace("\n", " ")
    lines_to_be_printed = (len(txt))/74.0
    l = lines_to_be_printed
    n = num_of_times
    x = "count"*n
    if num_of_times <= 0:
        return
    print txt + str(n) + str(x)
    n = n-1
    print_n(txt, num_of_times -1)

#variables:
num_line = 5
n = num_line
txt = "This is a load of sample text... Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation\n ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor\n in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa\n \n \n \n \n \n qui officia deserunt mollit anim id est laborum."

#testing:
#print "Hello" + (int(num_line) * "Hello")
#print ((int(n)) * ("|  " + txt[(74*n):(74*n+73)] + "  |"))
#print
print_n("derp\n\nhello", 15)
print_n2("spam", 7)
print
print
print
#print_n(txt, 3)
#print txt.replace("\n", " ")

#thinking:
#---need to extract "\n" - to do this can replace "\n" with " "
#idea works; need right equation; need to set n1 = 0
#need to use recursion to get n increase each time starting with 0, and maybe this will then require two variables so that one can be decreasing to zero to make the recursion end and the other will be increasing so that the next set of text is printed (of course I also then need the correct equation for that)

