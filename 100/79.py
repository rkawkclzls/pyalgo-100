def solution(data):
    if len(data) < 4:
        return 0  # 네 개 미만의 점으로는 사각형을 만들 수 없습니다.

    # x 좌표와 y 좌표를 분리하여 리스트에 저장합니다.
    x_coords = [point[0] for point in data]
    y_coords = [point[1] for point in data]

    # 최소 x, 최대 x, 최소 y, 최대 y를 찾습니다.
    min_x = min(x_coords)
    max_x = max(x_coords)
    min_y = min(y_coords)
    max_y = max(y_coords)

    # 최대 넓이를 계산합니다.
    max_area = (max_x - min_x) * (max_y - min_y)
    return max_area

# 예시 입력에 대한 최대 직사각형 넓이를 계산
example_inputs = [
    [(1, 1), (1, 3), (3, 1), (3, 3)],
    [(0, 0), (1, 1), (0, 2), (2, 0), (2, 2)],
    [(0, 0), (3, 0), (0, 2), (3, 2), (1, 1)]
]

# 각 입력에 대해 solution 함수를 호출하고 결과를 출력
results = [solution(data) for data in example_inputs]
results
