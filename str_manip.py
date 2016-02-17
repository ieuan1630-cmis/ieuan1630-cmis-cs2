def msg_box(txt): #takes text and returns it in a message box
    if len(txt) < 74:
        return "+" + ((len(txt) + 4) * "-") + "+" + "\n" + "|  " + txt + "  |" + "\n" + "+" + ((len(txt) + 4) * "-") + "+"
    else:
        #extract \n's right here
        num_line = (len(txt))/(74.0)
        return "+" + (78 * "-") + "+" + "\n" + (num_line * ("|  " + txt[:73] + "  |") + "\n" + "+" + (78 * "-") + "+"

output = "This is a load of sample text... Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation\n ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure\n dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa\n qui officia deserunt mollit anim id est laborum."

print msg_box(output)

#remove line spaces, if txt is greater than or equal to 74 characters then only have 80 top and 80 bottom, split every 74 characters and have "|  " and "  |" on either side
