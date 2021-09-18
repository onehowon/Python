a = [1,2,3,4]
result = []
for num in a:
    result.append(num * 3)

# 리스트의 a의 값을 하나씩 num으로 받아 3을 곱해 리스트 result에 넣는다.
result = [num * 3 for num in a]
print(result)

# 리스트 a의 값 중에서 2로 나눈 나머지가 0인 수만 3을 곱해 리스트 result에 넣는다.
result = [num * 3 for num in a if num % 2 == 0]
print(result)