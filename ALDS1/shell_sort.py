
def insertionSort(A, n, g):
    """
    A : 数列(配列)
    n : 配列の要素数
    g : ソートする要素間の感覚
    """
    global cnt
    for i in range(g, n-1):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j+g] = A[j]
            j = j - g
            cnt += 1
        A[j+g] = v

def shellSort(A, n):
    """
    A : 数列(配列)
    n : 配列の要素数
    """
    # cnt = 0
    m = 5
    G = [4,3,2,1]
    for i in range(m-1):
        insertionSort(A, n, G[i])

def main():

    N = int(input())
    data = []
    for i in range(N):
        data.append(int(input()))
    cnt = 0    

    shellSort(data, N)
    print(data)


if __name__ == '__main__':
    main()
