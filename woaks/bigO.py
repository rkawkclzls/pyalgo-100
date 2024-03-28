# 빅오표기법
# O(1)
n = 100
print((n + 1) * n) / 2


# O(n)
n = 100
for i in range(n):
    print(i)


# O(n)
n = 100
x = 1
z = 0
for i in range(n):
    print(i)
    x = x + 100
    z = 1 + i


# O(n)
n = 100
for i in range(n):
    for j in range(5):
        print(j)


# O(n^2)
n = 100
for i in range(n):
    for j in range(n):
        print(j)