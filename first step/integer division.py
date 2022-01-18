# 1 task
a = int(input())
print(a // 1000)

# 2 task
n, k = int(input()), int(input())
print(k // n)

# 3 task
n, k = int(input()), int(input())
print(n // k)

# 4 task
n = int(input())
print(n % 10)

# 5 task
n = int(input())
print(n % 1000 // 100)

# 6 task
a = int(input())
print(a // 100 + a // 10 % 10 + a % 10)

# 7 task
n = int(input())
a = n // 100
b = (n % 100) // 20
c = ((n % 100) % 20) // 10
d = (((n % 100) % 20) % 10) // 5
e = ((((n % 100) % 20) % 10) % 5) // 1
SUM = a + b + c + d + e
print(SUM)

# 8 task
a = int(input())
print(a // 60 % 24, a % 60)

# 9 task
a = int(input())
print(a // 2 * 2 + 2)

# 10 task
a = int(input())
print(a // 3600, str(a // 60 % 60 // 10) + str(a // 60 % 60 % 10), str(a % 60 % 60 // 10) + str(a % 60 % 60 % 10),
      sep=':')
