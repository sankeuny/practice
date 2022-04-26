a = int(input("올라가 : "))
b = int(input("내려가 : "))
v = int(input("나무 길이 : "))

cnt = 0     # 올라가는데 걸리는 일수
high = 0    # 올라간 높이
if a >= b:
    while True:
        cnt += 1
        high += a
        if high >= v:
            break
        high -= b
    print(cnt)
else:
    print('잘못된 입력값입니다.')