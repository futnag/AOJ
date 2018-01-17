import math
a,b,C = map(int, input().split())
C = math.radians(C)
c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(C))
L = a + b + c
S = a * b * math.sin(C) / 2
h = 2 * S / a

print("%f" % S)
print("%f" % L)
print("%f" % h)