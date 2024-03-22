def solution(data):
    str1, str2 = data
    
    # 문자열을 집합으로 변환
    set1 = set(str1)
    set2 = set(str2)
    
    # 두 집합의 합집합에서 교집합을 뺀 고유 요소들을 찾음
    unique_chars = list(set1 ^ set2)
    
    # 고유 요소들을 알파벳 순으로 정렬
    unique_chars.sort()
    
    return unique_chars