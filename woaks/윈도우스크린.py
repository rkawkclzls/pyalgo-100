def solution(data, require_value):
    start_pointer = 0
    end_pointer = 0
    temp_sum = 0

    data_len = len(data)
    result = []

    for start_pointer in range(data_len):
        while temp_sum < require_value and end_pointer < data_len:
            temp_sum += data[end_pointer]
            end_pointer += 1
        if temp_sum == require_value:
            result.append([start_pointer, end_pointer-1])
        temp_sum -= data[start_pointer]
    return result

solution([1, 5, 4, 6, 4, 6, 7, 6, 4, 3, 1, 2], 10)