def dfs(node, graph, visited, recStack):
    # 현재 노드를 방문 중으로 표시
    visited[node] = True
    recStack[node] = True

    # 현재 노드의 이웃들을 확인
    for neighbor in graph[node]:
        # 이웃이 방문하지 않은 노드라면 DFS를 재귀적으로 호출
        if not visited[neighbor]:
            if dfs(neighbor, graph, visited, recStack):
                return True
        # 이웃이 현재 방문 중인 경로상에 있다면 사이클이 존재함
        elif recStack[neighbor]:
            return True
    
    # 현재 노드의 처리가 끝났으므로 방문 중 상태를 해제
    recStack[node] = False
    return False

def solution(graph):
    # 노드의 개수만큼 방문 상태를 초기화
    visited = {node: False for node in graph}
    recStack = {node: False for node in graph}
    
    # 모든 노드를 시작점으로 DFS를 시도하여 사이클 존재 여부 확인
    for node in graph:
        if not visited[node]:
            if dfs(node, graph, visited, recStack):
                return True
    return False
