str = input("문자를 입려하세요")
length = len(str)

if length%2 == 1:
    ch1 = str[length/2]
    print("중앙글자는", ch1)
else:
    ch1 = str[length//2-1]
    ch2 = str[length//2]
    print("중앙글자는", ch1, ch2)