while 1:
    n = int(input())
    if n == 0:
        break
    else:
        data = list(map(int, input().split()))
        mean = sum(data) / n
        temp = 0
        for i in data:
            temp += (i - mean) ** 2
        print((temp/n)**0.5)