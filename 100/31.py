# 비트 치환 문제

# 문제 설명

# 정수 N이 주어집니다. 이 정수의 비트 표현에서 모든 1을 A로, 
# 모든 0을 B로 치환하여 결과를 문자열로 변환하는 코드를 작성

# 제한 사항
# 주어진 수 N은 0이상 1000이하의 정수입니다.

data = 9

def solution(data):
    binary = bin(data)[2:]
    new = binary.replace('1','A')
    new = new.replace('0','B')
    return new

print(solution(data))
