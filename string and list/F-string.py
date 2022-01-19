# 1 task
print(f'Мое имя {input()}!')

# 2 task
print(f'Hello {input().upper()}. You are {input()} years old.')

# 3 task
print(f'{input()}, вам исполнится 77 лет в {int(input()) + 77}')

# 4 task
z = int(input())
print(f'{z} сек - это {z//60} мин. {z%60} сек.')

# 5 task
a, b = map(int,input().split())
print(f'Разрешение экрана: {a} x {b}.')
print(f'Общее количество пикселей = {a * b}.')

# 6 task
a= int(input())
b= int(input())
print(f'{a} / {b} = {a / b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} % {b} = {a % b}')

# 7 task
a, b, c = int(input()), int(input()), int(input())
print(f'Vector A({a}, {b}, {c})')
print(f'Vector B({a + 5}, {b + 5}, {c + 5})')

# 8 task
a, b = float(input()), int(input())
print(f'''Current dollar rate is {a}. You want buy {b} dollars
You must pay {a * b}''')