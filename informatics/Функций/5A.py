from functools import reduce
def min4(a, b, c, d):
    arr=(a,b,c,d)
    return reduce(lambda x,y: min(x, y), arr)
a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(min4(a, b, c, d))