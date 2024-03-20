def solution(data):
    # 빈도수 계산
    frequency = {}
    for char in data:
        if char.isalpha():  # 알파벳만 고려
            frequency[char] = frequency.get(char, 0) + 1

    # 빈도수 내림차순, 알파벳 오름차순으로 정렬
    sorted_chars = sorted(frequency.items(), key=lambda x: (-x[1], x[0]))

    # 결과 문자열 생성
    result = ''.join([char[0] for char in sorted_chars])

    return result