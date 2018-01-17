

n = int(input())

minv = int(input())
maxv = -2000000000
for i in range(1, n):
    d = int(input())
    maxv = max(maxv, d - minv)
    minv = min(minv, d)

print(maxv)

print("hello")






# end
