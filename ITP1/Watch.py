# Getting Started - Watch
s = int(input())
m = s%3600/60
h = s//3600
s = s%60
print("%d:%d:%d" % (h, m, s))