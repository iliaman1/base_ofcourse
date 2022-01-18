# 1 task
a = int(input())
print(a > 0)

# 2 task
a = int(input())
print(a % 2 == 0)

# 3 task
a = int(input())
print(a % 6 == 0)

# 4 task
a = int(input())
print(a % 9 != 0)

# 5 task
a = int(input())
print(a % 10 == 2)

# 6 task
a, b = map(int, input().split())
print(a % 7 == 0 and b % 7 == 0)

# 7 task
a, s, d = map(int, input().split())
print(a == s == d)

# 8 task
a = int(input())
print(a > 5 and a <= 19)

# 9 task
a, b = input(), input()
print(a == 'awesome' or b == 'awesome')

# 10 task
a, b, c = map(int, input().split())
print(a == b or a == c or b == c)

# 11 task
a = int(input())
print(a // 10 > 0 and a // 10 <= 9)

# 12 task
a, b, c = map(int, input().split())
print(a ** 2 == b ** 2 + c ** 2 or b ** 2 == a ** 2 + c ** 2 or c ** 2 == a ** 2 + b ** 2)
