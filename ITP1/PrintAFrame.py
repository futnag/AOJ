while 1:
    h, w = map(int, input().split())
    if h == w == 0:
        break
    else:
        for i in range(h):
            if i == 0:
                print("#"*w)
            elif i == h-1:
                print("#"*w)
            else:
                print("#" + "."*(w-2) + "#")
        print()