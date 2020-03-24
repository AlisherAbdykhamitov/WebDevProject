n = int(input())
value = 1
if(n == 1):
    print("YES")
else:
    b = False
    while value <= n:
        value *= 2
        if value == n:
            b = True
    if b == True:
        print("YES")
    else:
        print("NO")
