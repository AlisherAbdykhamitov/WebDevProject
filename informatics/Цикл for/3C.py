import math
a = int(input())
b = int(input())
for number in range(a , b + 1):
    z  = math.sqrt(number)
    if(z * z == number ):
        print(number, ' ')
