def hanoi_tower(n, fr, tmp, to) : # Hanoi Tower 순환 함수

    if (n == 1): # 종료 조건
        print("원판 1: %s --> %s" % (fr,to)) # 가장 작은 원판을 옮김
    else:
        hanoi_tower(n - 1, fr, to, tmp) # n-1개를 to를 이용해 tmp로
        print("원판 %d: %s --> %s" % (n, fr, to)) # 하나의 원판을 옮김
        hanoi_tower(n - 1, tmp, fr, to) # n-1개를 fr을 이용해 to로

hanoi_tower(4, 'A', 'B', 'C')