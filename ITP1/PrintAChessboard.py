import sys
while 1:
    h, w = map(int, input().split())
    if h == w == 0:
        break
    else:
        for i in range(h):
            for j in range(w):
                if (i + j)%2 == 0:
                    sys.stdout.write("#")
                else:
                    sys.stdout.write(".")
            print()
        print()