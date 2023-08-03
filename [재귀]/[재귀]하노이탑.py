def hanoi(num, from_start, temp, to):
    if num == 0:
        return
    hanoi(num-1, from_start, to, temp)
    print(num,'이 ', from_start,'에서 ', to,'로 갑니다.')
    hanoi(num-1, temp, from_start, to)

hanoi(3, 'A', 'B', 'C')