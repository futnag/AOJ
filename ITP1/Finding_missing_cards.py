N = int(input())
S = ["S"]
H = ["H"]
C = ["C"]
D = ["D"]
for i in range(N):
    s, n = input().split()
    if s == "S":
        S.append(int(n))
    elif s == "H":
        H.append(int(n))
    elif s == "C":
        C.append(int(n))
    else:
        D.append(int(n))

def finder(d):
    for j in range(1, 14):
        if j not in d:
            print(d[0], j)

finder(S)
finder(H)
finder(C)
finder(D)