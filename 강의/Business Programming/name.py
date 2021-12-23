name =input("당신의 이름을 입력하세요:")
num = len(name)

for i in name:
    print(name[num-1], end="")
    num=num-1

vowels = "aeiouAEIOU"
result_a = ""
result_b = ""
for k in name:
    if k not in vowels:
        result_a += k
    else:
        result_b += k

print("\n")
print(result_a)
print(result_b)