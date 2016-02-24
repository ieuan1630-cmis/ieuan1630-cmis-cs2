def print_n2(txt, num_of_times, num_of_times_fixed):
    txt = txt.replace("\n", " ")
    f = num_of_times_fixed
    n = num_of_times
    if num_of_times <= 0:
        return
    else:
        n = (f - n)
        x = txt[74*n:(74*n)+74]
        print "|  " + str(x) + "  |"
        print_n2(txt, num_of_times -1, num_of_times_fixed)

def msg_box(txt): #takes text and returns it in a message box
    txt = txt.replace("\n", " ")
    if len(txt) < 74:
        return "+" + ((len(txt) + 4) * "-") + "+" + "\n" + "|  " + txt + "  |" + "\n" + "+" + ((len(txt) + 4) * "-") + "+"
    else:
        num_of_lines = len(txt)/74.0 #need to round this value to make it an integer but still reflect what i need it to say; conditional likely needed
        a = num_of_lines
        return "+" + (78 * "-") + "+" + "\n" + print_n2(txt, a, a) + "\n" + "+" + (78 * "-") + "+"

output = "This is a load of sample text... Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation\n ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor\n in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa\n qui officia deserunt mollit anim id est laborum."

print msg_box(output)

#remove line spaces, if txt is greater than or equal to 74 characters then only have 80 top and 80 bottom, split every 74 characters and have "|  " and "  |" on either side
