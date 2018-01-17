

cache = {}
def change(n, currency=[500,100,50,10,5,1]):

    if (n, len(currency)) in cache:
        return cache[(n, len(currency))]
    
    if len(currency) == 1:
        cache[(n, len(currency))] = 1
        return 1
    
    cnt = 0
    for i in range(n // currency[0] + 1):
        cnt += change(n - i * currency[0], currency[1:])
    cache[(n, len(currency))] = cnt
    return cnt

def main():
    n = int(input())
    print(change(n))

if __name__ == "__main__":
    main()






