def solution(data):
 
    pattern = r'^[a-zA-Z0-9._+]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, data) is not None