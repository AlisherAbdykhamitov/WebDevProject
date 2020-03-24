a = []

for i in range(int(input())):
    a.append(int(input()))

result = sum(x > y for x, y in zip(a[1:], a))
print(result)