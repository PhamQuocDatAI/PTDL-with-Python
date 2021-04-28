import random


sum = 10
data = []
while True:
    count = int(input('Nhap count: '))
    low = int(input('Nhap low: '))
    high = int(input('Nhap high: '))
    if (sum - count) > 0:
        for x in range(count):
            a = random.uniform(low, high)
            data.append(a)
    else:
        for x in range(sum):
            a = random.uniform(low, high)
            data.append(a)
    sum -= count

print(data)

  