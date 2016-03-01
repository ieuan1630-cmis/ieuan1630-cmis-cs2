import time

#response collecting function
def response(prompt, allowed):
    resp = input(prompt)
    #check to see if response is in the set of allowed responses
    if resp in allowed:
        #return it if it is
        return resp
    else:
        #call response() again if it is not
        print('Your answer must be one of the following:\n' + ", ".join(allowed))
        return response(prompt, allowed)


#the list of questions
questions = [
    "1 == 1",
    "1 == 0",
    "1 != 1",
    "1 != 0",
    "0 > 1",
    "4 >= 5",
    "5 >= 5",
    "0 < 1",
    "1 >= 0",
    "1 <= 0",
    "not 1 == 1",
    "not 1 == 0",
    "not 1 != 1",
    "not 1 != 0",
    "not 0 > 1",
    "not 4 >= 5",
    "not 5 >= 5",
    "not 0 < 1",
    "not 1 >= 0",
    "not 1 <= 0",
    "1 == 1 and 1 != 1",
    "1 == 1 and 1 > 0",
    "1 != 1 and 1 == 0",
    "5 < 10 and 5 > 4" 
    "1 == 1 or 1 != 1",
    "1 == 1 or 1 > 0",
    "1 != 1 or 1 == 0",
    "5 < 10 or 5 > 10",     
    "not (1 == 1) and 1 != 1",
    "1 == 1 and not (1 > 0)",
    "not (1 != 1 and 1 == 0)",
    "1 == 1 or not (1 != 1)",
    "not (1 == 1) or 1 > 0",
    "not (1 != 1 or 1 == 0)",
    "not (5 < 10 or 5 > 10)",     
    "2 * 3 == 6",
    "2 * 3.5 >= 7.5",
    "3 / 2 == 1.5",
    "3.0 / 2.0 == 1.5",
    "3 / 2.0 == 1.5",
    "5 / 2 == 2.5",
    "5.0 / 2.0 == 2.5",
    "5.0 / 2 >= 2.5",
    "4 / 3 == 1.3333333333333333333333333333333333333333333333",
    "(2 * 6 == 12) and (5.0 / 2.0 < 2.6)",
    "not 4 % 2 == 0",
    "not 4 % 3 != 0",
    "2 * 3 == 6 and 2 * 3.5 >= 7.5",
    "3 / 2 == 1.5 or 3.0 / 2.0 == 1.5",
    "3 / 2.0 == 1.5 and 5 / 2 == 2.5",
    "5.0 / 2.0 == 2.5 or 5.0 / 2 >= 2.5",
    "4 / 3 == 1.3333333333 and ((2 * 6 == 12) and (5.0 / 2.0 < 2.6))",
    "not (4 % 2 == 0 or 4 % 3 != 0)",
    ]

#score keeping variables
correct = 0
incorrect = 0

#Display some instructions and wait
print("Type t for True.")
print("Type f for False.")
input("Hit 'enter' to begin")

#start the timer
start = time.time()
print("The clock has started!!")

#go through the list of questions
for q in questions:
    #display question and get answer
    answer = response(q + ": ", ['t','f']) == 't'
    result = eval(q)
    #compare answer to actual result
    if answer == result:
        print("That's right!")
        correct += 1
    else:
        print("That's wrong!")
        incorrect += 1
    print(q + " is " + str(result) + "\n\n")
end = time.time()

#Display results
print("Your time was: ", end - start, " seconds")
print("You got ", correct, " correct.")
print("You got ", incorrect, " incorrect.")
if incorrect > 0:
    print("Try again!!!")
else:
    print("You passed!!!")
