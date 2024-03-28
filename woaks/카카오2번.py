from collections import Counter

def solution(N, stages):
    total_len = len(stages)
    player = Counter(stages)

    answer = {} # key 값으로 stage를 만들고, value로 실패율 => sorted를 실패율 기준으로
    
    for i in range(1, N + 1):
        answer[i] = 0

    for i in answer:
        if player[i] != 0 and total_len != 0:
            answer[i] = player[i] / total_len
        else:
            answer[i] = 0
        total_len -= player[i]

    return answer

solution(5, [2, 1, 2, 6, 2, 4, 3, 3])

answer = {1: 0.125, 2: 0.42857142857142855, 3: 0.5, 4: 0.5, 5: 0}
sorted(answer, key=lambda x:(-answer[x], x))