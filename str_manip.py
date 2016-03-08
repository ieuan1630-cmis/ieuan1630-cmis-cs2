def print_n2(txt, num_of_times, num_of_times_fixed):
    txt = txt.replace("\n", " ")
    f = num_of_times_fixed #in this case equal to number of lines in msgbox
    n = num_of_times #n is the number of times left to go
    if num_of_times <= 0: #if all lines of txt are printed the bottom of msgbox is returned
        return "+" + (78 * "-") + "+" #bottom of message box
    else:
        n = (f - n) #n is redefined as the difference between the total number of times the recursion will occur (in this msgbox case this is equal to the number of lines of text), and the line number it is on; this then represents the number of times that have already passed (e.g. 3rd line of txt)
        x = txt[74*int(n):(74*int(n))+74] #n from above is used to select write slice of txt
        print "|  " + str(x) + "  |" #selection of txt is printed in between msg box edges
        return print_n2(txt, num_of_times -1, num_of_times_fixed)

def print_n3(txt, num_of_times, num_of_times_fixed): #like print_n2 but works for text not divisible by 74
    num_of_lines = num_of_times
    a = num_of_lines
    if a - int(a) == 0.0:
        return print_n2(txt, num_of_times, num_of_times_fixed)
    else:
        txt = txt.replace("\n", " ")
        f = num_of_times_fixed  #in this case equal to number of lines in msgbox
        n = num_of_times #n is the number of times left to go
        if num_of_times <= 0: #if all lines of txt are printed the bottom of msgbox is returned
            return "+" + (78 * "-") + "+" #bottom of message box
        elif num_of_times <= 1.0 and num_of_times > 0:
            n = (f - n) #n is redefined as the difference between the total number of times the recursion will occur (in this msgbox case this is equal to the number of lines of text), and the line number it is on; this then represents the number of times that have already passed (e.g. 3rd line of txt)
            x = txt[74*int(n):(74*int(n))+74] #n from above is used to select write slice of txt
            xtra_spaces = 74 - len(x)
            print "|  " + str(x) + (xtra_spaces * " ") + "  |"
            return print_n3(txt, num_of_times -1, num_of_times_fixed)
        else:
            n = (f - n) #n is redefined as the difference between the total number of times the recursion will occur (in this msgbox case this is equal to the number of lines of text), and the line number it is on; this then represents the number of times that have already passed (e.g. 3rd line of txt)
            x = txt[74*int(n):(74*int(n))+74] #n from above is used to select write slice of txt
            print "|  " + str(x) + "  |" #selection of txt is printed in between msg box edges
            return print_n3(txt, num_of_times -1, num_of_times_fixed)

def msg_box(txt): #takes text and returns it in a message box
    txt = txt.replace("\n", " ")
    if len(txt) < 74:
        return "+" + ((len(txt) + 4) * "-") + "+" + "\n" + "|  " + txt + "  |" + "\n" + "+" + ((len(txt) + 4) * "-") + "+"
    else:
        print "+" + (78 * "-") + "+" # top of message box
        num_of_lines = len(txt)/74.0 #num of lines is equal to the length of text divided by 74 cos "|  " + 74characters + "  | = 80 character wide screen
        a = num_of_lines #to shorten num_of_lines for plugging into function print_n3, it is stored in other variable "a"
        return str(print_n3(txt, a, a))

output = "This is a load of sample text... Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation\n ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor\n in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa\n qui officia deserunt mollit anim id est laborum slfsjlfksdjflsj;."

print msg_box("text < 74 characters \n\n works")
print msg_box("so does text divisible by 74   \n\n\n\njjjgfgfjkgjjjjjjjjjjjjjjhhhhhhhhhhhggggggggggggggggggghhhhhhhhhh jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjkkkkkkl")
print msg_box(output)

user_input = raw_input("Copy and paste some text in here: ")
print msg_box(user_input)
