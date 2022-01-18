# 1 task
import math

a = int(input())
print(math.ceil(a / 10))

# 2 task
import math

a = int(input())
print(math.ceil(a / 4))

# 3 task
import math

a, b, c = int(input()), int(input()), int(input())
print(math.ceil(a / 2) + math.ceil(b / 2) + math.ceil(c / 2))

# 4 task
import math

a, b, c = map(int, input().split())
P = (a + b) * 2
S = c * P
print(math.ceil(S / 16))
