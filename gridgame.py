import random
def at_point(x1, y1, x2, y2):
    if x1 == x2 and y1 == y2:
        return True
    else:
        return False
def draw_map(w, h, px, py, rx, ry, gx, gy):
    out = ""
    y = 0
    while y < h:
        x = 0
        while x < w:
            if at_point(px, py, x, y):
                #print px, py, x, y
                out += "@"
            elif at_point(rx, ry, x, y):
                out += "#"
            elif at_point(gx, gy, x, y):
                out += "+"
            else:
                out += "."
            x += 1
        out += "\n"
        y += 1
    return out

def main():
    a = True
    w = 40
    h = 20

    px = w / 2
    py = h / 2
    t = 3

    rx = random.randrange(0, w)
    ry = random.randrange(0, h)

    gx = random.randrange(0, w)
    gy = random.randrange(0, h)
    j = 10

    while a:
        print draw_map(w, h, px, py, rx, ry, gx, gy)
        if random.random() > 0.5:
            if rx > px:
                rx -= 1
            elif rx < px:
                rx += 1
        else:
            if ry > py:
                ry -= 1
            elif ry < py:
                ry += 1
            
        rx += random.randint(-1,1)
        ry += random.randint(-1,1)
        if j % 10 == 0:
            gx = random.randrange(0,w)
            gy = random.randrange(0,h)
        j += 1
        if at_point(px, py, gx, gy):
            a = False
            print "You win!"
        elif at_point(px, py, rx, ry):
            a = False
            print "You lose!"
        else:
            cmd = raw_input(": ")
            if cmd == "a":
                px -= 1
            elif cmd == "d":
                px += 1
            elif cmd == "w":
                py -= 1
            elif cmd == "s":
                py += 1
            elif cmd == "t" and t > 0:
                py = h/2
                px = w/2
                t -= 1
            elif cmd == "q":
                a = False
                print "You quit!"
    return

main()
