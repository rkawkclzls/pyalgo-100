# 비트 반전 정수
# 문제 설명

# 정수 N이 주어집니다. 이정수의 이진 표현에서 모든 비트를 반전시킨 후,
# 그 결과를 다시 정수로 변환하여 반환하는 코드를 작성해주세요

# 제한 사항
# 주어진 수 N은 0이상 1000이하의 정수입니다.
# N의 이진 표현은 10자리로 표현됩니다.(앞에 필요한 경우 0을 채웁니다.)

data = 9

def solution(data):
    binary = (bin(int('1'*10,2) - data))
    return (int(binary,2))

print(solution(data))
