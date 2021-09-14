def sum_range(begin, end, step = 1):
    sum = 0
    for n in range(begin, end, step):
        sum += n
    return sum

print("sum =", sum_range(1,10))
print("sum =", sum_range(1, 10, 2))

print("sum =", sum_range(step=3, begin=1, end=10))
print("game", end=" ")