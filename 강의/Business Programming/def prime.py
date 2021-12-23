def is_prime(n):
    for i in range(2, n):
        if (n%i ==0):
            return False
    return True

n = int(input('정수를 입력하시오: '))
print(is_prime(n))

if(is_prime(n)==True):
    y=" "
    while (n>0):
        y=str(n%2)+y
        n=n//2
    print(y)