n = int(input("3 이상의 숫자를 입력하시오: "))
numbers = list(range(1,n+1))

count = 0
for first in numbers:
    for second in numbers:
        for third in numbers:
            if first != second and first != third and second != third:
                print(first, second, third)
                count += 1
print("Number of cases : %d" %count)