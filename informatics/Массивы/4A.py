A = []
a = int(input())
if(a > 0):
    for number in range(0 , a):
        b = int(input())
        A.append(b)
    for number in range(len(A)):
        if(number % 2 == 0):
            print(A[number])