def countup(n):
    if n == 10:
        print "Blastoff!"
    else:
        print n
        return countup(n+1)

def main():
    return countup(int(raw_input("Pick an integer less than 10: ")))

main()
