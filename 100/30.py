# 정수로 이루어진 배열이 주어집니다. 이 배열에서 정확히 한 번만 나타나는 숫자를 찾아 반환하는 코드를 작성해주세요.
# 모든 숫자는 정확히 두 번 나타나는데, 오직 하나의 숫자만 한번만 나타납니다.

# 제한 사항
# 배열의 길이는 1이상 10,000이하입니다.
# 배열의 요소는 정수입니다.

data = [2, 2, 1]
# print(data.pop(2))


# for index,i in enumerate(data):
#     print(index)
#     data2 = data
#     data2.pop(index)
#     print(data2)

# for j in range(len(data)):
#     print(j)
#     data2 = data
def solution(data):
    for index,i in enumerate(data):
        data2 = []
        for j in data:
            data2.append(j)
        data2.pop(index)
        if i not in data2:
            return i

print(solution(data))
    


    






    


        

