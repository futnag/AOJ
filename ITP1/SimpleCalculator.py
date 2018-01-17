while 1:
    a = input().split()
    if a[1] == "+":
        print(int(a[0]) + int(a[2]))
    elif a[1] == "-":
        print(int(a[0]) - int(a[2]))
    elif a[1] == "*":
        print(int(a[0]) * int(a[2]))
    elif a[1] == "/":
        print(int(a[0]) // int(a[2]))

    if a[1] == "?":
        break