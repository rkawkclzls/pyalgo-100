def process_deque_commands(deque, commands):
    # commands 리스트를 순회하며 명령을 처리
    for direction, distance in commands:
        # '왼쪽' 명령 처리
        if direction == '왼쪽':
            if len(deque) < distance:
                # 데큐의 길이가 이동 거리보다 짧으면 모든 처리를 중단
                return deque
            else:
                # 왼쪽에서 distance만큼 요소 제거
                deque = deque[distance:]
        # '오른쪽' 명령 처리
        elif direction == '오른쪽':
            if len(deque) < distance:
                # 데큐의 길이가 이동 거리보다 짧으면 모든 처리를 중단
                return deque
            else:
                # 오른쪽에서 distance만큼 요소 제거
                deque = deque[:-distance]
    return deque

# 예시 입력
deque1 = [1, 2, 3, 4, 5]
commands1 = [('왼쪽', 2), ('오른쪽', 1)]

deque2 = [1, 2, 3, 4, 5, 6]
commands2 = [('오른쪽', 3), ('왼쪽', 2)]

# 예시 출력
print(process_deque_commands(deque1, commands1))
print(process_deque_commands(deque2, commands2))
