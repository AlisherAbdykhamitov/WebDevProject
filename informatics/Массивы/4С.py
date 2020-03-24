A = []
a = int(input())
for number in range(0, a):
    b = int(input())
    A.append(b)

cnt = 0
for number in range(len(A)):
    if(A[number] > 0):
        cnt = cnt + 1
print(cnt)
