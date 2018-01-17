while True:
    s = input()
    if s == '-':
        break
    loop = int(input())
    for i in range(loop):
        ch = int(input())
        s = s[ch:]+s[:ch]
    print(s)