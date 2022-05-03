# 베르트랑 공준은 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은
# 소수는 적어도 하나 존재한다는 내용을 담고 있다.
# 이 명제는 조제프 베르트랑이 1845년에 추측했고, 파프누티 체비쇼프가 1850년에 증명했다.
# 예를 들어, 10보다 크고, 20보다 작거나 같은 소수는 4개가 있다. (11, 13, 17, 19)
# 또, 14보다 크고, 28보다 작거나 같은 소수는 3개가 있다. (17,19, 23)
# 자연수 n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오.

# 소수 : ‘양의 약수를 두 개만 가지는 자연수’는 1과 자기 자신만을 약수로 갖는 수를 의미한다고 보면 된다!

# 에라토스테네스의 체: 소수를 판별하는 알고리즘이다. 소수들을 대량으로 빠르고 정확하게 구하는 방법이다.

# https://choheeis.github.io/newblog//articles/2020-04/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98%EC%B2%B4
# https://blog.naver.com/PostView.naver?blogId=ndb796&logNo=221233595886&redirect=Dlog&widgetTypeCall=true&directAccess=false

# - 단일 숫자 소수 여부 확인
# 어떤 수의 소수의 여부를 확인 할 때는, 특정한 숫자의 제곱근 까지만 약수의 여부를 검증하면
# O(N^1/2)의 시간 복잡도로 빠르게 구할 수 있다.
# 수가 수(N이라고 가정)를 나누면 몫이 생기는데, 몫과 나누는 수 둘 중 하나는 N 제곱근 이하이기 때문이다.

# 만약, 대량의 소수를 한꺼번에 판별해야할 경우는 '에라토스테네스의 체'를 이용한다.

import math
import sys

def is_prime(n):
    if n == 2:
        return True

    if n % 2 == 0:      # 2로 나눠지는 숫자 제거
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
                      # Math.sqrt() 함수는 숫자의 제곱근을 반환합니다.
                      # 특정 숫자의 제곱근까지만 약수의 여부를 검증하면 된다.
                      # 이유는 아직 잘 모르겠음.. 이해 안 감...
                      # https://nahwasa.com/entry/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98-%EC%B2%B4-%ED%98%B9%EC%9D%80-%EC%86%8C%EC%88%98%ED%8C%90%EC%A0%95-%EC%8B%9C-%EC%A0%9C%EA%B3%B1%EA%B7%BC-%EA%B9%8C%EC%A7%80%EB%A7%8C-%ED%99%95%EC%9D%B8%ED%95%98%EB%A9%B4-%EB%90%98%EB%8A%94-%EC%9D%B4%EC%9C%A0
        if n % i == 0:
            return False
    return True


while True:
    n = int(sys.stdin.readline())
    # 반복문으로 여러줄 입력받는 상황에서는 반드시 sys.stdin.readline()을 사용해야 시간초가 안뜸
    if n == 0:
        break

    prime_cnt = 0

    for i in range(n + 1, (2 * n) + 1):
                  # 범위 설정 : n보다 커야하기 때문에 n+1 부터 2 * n + 1 까지 설정
        if is_prime(i):
            prime_cnt += 1

    print(prime_cnt)