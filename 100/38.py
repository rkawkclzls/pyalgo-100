def solution(url):
    # 초기 딕셔너리 설정
    result = {'protocol': '', 'domain': '', 'path': '', 'query': ''}

    # 프로토콜 추출
    protocol_end = url.find("://")
    if protocol_end != -1:
        result['protocol'] = url[:protocol_end]
        url = url[protocol_end+3:]
    else:
        # 프로토콜이 없는 경우 예외 처리
        return result

    # 도메인과 나머지 부분 분리
    path_start = url.find("/")
    query_start = url.find("?")

    if path_start == -1 and query_start == -1:
        # 도메인만 있는 경우
        result['domain'] = url
    elif path_start == -1:
        # 쿼리스트링은 있지만 경로가 없는 경우
        result['domain'] = url[:query_start]
        result['query'] = url[query_start+1:]
    else:
        # 도메인 추출
        if query_start == -1 or path_start < query_start:
            result['domain'] = url[:path_start]
            url = url[path_start:]
        else:
            result['domain'] = url[:query_start]
            url = url[query_start:]

        # 경로와 쿼리스트링 분리
        if query_start != -1 and path_start < query_start:
            query_start = url.find("?")
            result['path'] = url[:query_start]
            result['query'] = url[query_start+1:]
        else:
            result['path'] = url

    return result
