def solution(data):
    korean_numbers = {
        0: '',
        1: '일',
        2: '이',
        3: '삼',
        4: '사',
        5: '오',
        6: '육',
        7: '칠',
        8: '팔',
        9: '구'
    }
    
    korean_units = {
        1: '',
        10: '십',
        100: '백',
        1000: '천',
        10000: '만'
    }
    
    result = ''
    unit = 1
    while data > 0:
        number = data % 10
        if number > 0:
            result = korean_numbers[number] + korean_units[unit] + result
        data //= 10
        unit *= 10

    return result