def solution(data):
    # 마지막 '.'의 위치를 찾습니다.
    dot_index = data.rfind('.')
    
    # '.'이 없거나 파일명의 마지막에 위치한 경우 빈 문자열을 반환합니다.
    if dot_index == -1 or dot_index == len(data) - 1:
        return ''
    
    # '.' 다음에 오는 문자열(파일 확장자)을 반환합니다.
    return data[dot_index + 1:]