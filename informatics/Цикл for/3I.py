a = int(input())
i = 1
cnt = 0
for number in range(i, a + 1):
    if (a % number == 0):
        cnt = cnt + 1
print(cnt)
