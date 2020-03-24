a = int(input())
A = []
for number in range(a):
    b = int(input())
    A.append(b)

for number in range(len(A)):
    if(A[number] % 2 == 0):
        print(A[number])