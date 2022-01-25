# 1 task
age = int(input())
print(age + 1)

# 2 task
a, b = map(int, input().split())
print(a + b)

# 3 task
suma = int(input())
k = suma // 3 * 2
p = suma // 3 // 2
print(p, k, p)

# 4 task
x, y, z = map(int, input().split())
print(x * 3 + y * 5 + z * 12)

# 5 task
a, b, c = map(int, input().split())
print(2 * a * b * c)

# 6 task
a, b, c, d = map(int, input().split())
print((a + b + c + d) / 4)

# 7 task
a = int(input())
s = int(input())
d = int(input())
z = int(input())
x = int(input())
c = int(input())
print((z * 3600 + x * 60 + c) - (a * 3600 + s * 60 + d))

# 8 task
a, b = map(int, input().split())
print((a + b - 1) - a, (a + b - 1) - b)

# 9 task
a, b = int(input()), int(input())
c = abs(a) + abs(b)
print(c)

# 10 task
a, b = map(float, input().split())
print(abs(a - b))

# 11 task
li = []
a, s, d, z, x = map(int, input().split())
li.append(a)
li.append(s)
li.append(d)
li.append(z)
li.append(x)
print(max(li))

# 12 task
a, b, c = int(input()), int(input()), int(input())
print(max(a + b + c, a * b * c, (a + b) * c, a * (b + c)))

# 13 task
a = float(input())
print(round(a, 2), round(a, 3))
