
def binary_search(A, key):
    left = 0
    right = len(A)

    while left < right:
        mid = (left + right) // 2
        if (A[mid] == key):
            return 1
        elif (key < A[mid]):
            right = mid
        else:
            left = mid + 1
    return 0

def main():
    n = int(input())
    s = list(map(int, input().split()))
    q = int(input())
    t = list(map(int, input().split()))

    res = 0
    for i in t:
        a = binary_search(s, i)
        res += a

    print(res)

if __name__ == "__main__":
    main()
    
    
    
    
    
    