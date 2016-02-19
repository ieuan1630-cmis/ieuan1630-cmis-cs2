def print_n(text, num_of_times):
    if num_of_times <= 0:
        return
    print text
    print_n(text, num_of_times -1)

num_line = 5
n = num_line
txt = "This is a load of sample text... Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation\n ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor\n in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa\n qui officia deserunt mollit anim id est laborum."

print "Hello" + (int(num_line) * "Hello")
print ((int(n)) * ("|  " + txt[(74*n):(74*n+73)] + "  |"))
print
print_n(txt, 2)

#idea works; need right equation; need to set n1 = 0

