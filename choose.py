def main(): #get input and if input is bingo return true
    x = raw_input("Type a word: ")
    return bool(x == "bingo" or x == "Bingo")

print main()
