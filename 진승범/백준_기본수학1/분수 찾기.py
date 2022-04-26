

# 이와 같이 나열된 분수들을 1/1 → 1/2 → 2/1 → 3/1 → 2/2 → … 과 같은 지그재그 순서로 차례대로
# 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.
#
# X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.

x = int(input("숫자를 입력하세요. : "))

line = 0        # 줄수
nu = 0       # 줄 수 까지의 총 갯수
while x > nu:
    line = line + 1         # line+=1
    nu = nu + line    # maxnu+=line

print("line : ", line)
print("nu : ", nu)


# 짝수라인은 시작점에서 끝점으로 갈수록 분자가 1씩 늘어가고 분모가 1씩 감소하며
# 홀수라인은 시작점에서 끝점으로 갈수록 분자가 1씩 줄어들고 분모가 1씩 늘어난다.
gap = nu - x
print("gap : ", gap)
if line % 2 == 0:       # 사선 라인이 짝수번째 일 때 : 오른쪽 위에서 왼쪽 아래로
    top = line - gap    # 분자
    under = gap + 1     # 분모
else :                  # 사선 라인이 홀수번째 일 때 : 왼쪽 아래에서 오른쪽 위로로    top = gap + 1       # 분자
    top = gap + 1       # 분자
    under = line - gap  # 분모

print(top,"/",under)

