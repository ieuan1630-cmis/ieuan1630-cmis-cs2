def main(): #get input and if input is bingo return true
    x = raw_input("Type a word: ")
    return bool(x == "bingo" or x == "Bingo")

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

def JK():
    in_the_house = raw_input("Is jk in the house? ")
    if in_the_house == "YES" or in_the_house == "Yes" or in_the_house == "yes":
        return "That's right"
    else:
        return "You're blind dumbo, of course he's in the house"

print JK()
