import random

num = random.randint(0, 2)
print(num)

a = 1
c = True if a > num else False
print(type(c))

while a < 10:
    print(f'{a}--->执行')
    a += 1

i = 1
even = 0
odd = 0
while i <= 100:
    if i % 2 == 0:
        even += i
    else:
        odd += i
    i += 1
print(f'even:{even}-->odd:{odd}')

j = 0
while j < 10:
    if j == 5:
        print(j)
        j += 1
        continue
    else:
        print(j)
    j += 1

z = 0
while z < 3:
    y = 0
    while y < 3:
        print(f'{y}')
        y += 1
    print(f'{z}')
    z += 1


