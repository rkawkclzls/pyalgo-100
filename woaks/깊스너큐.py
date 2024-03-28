# 깊스너큐(깊이 우선 탐색은 스택, 너비 우선 탐색은 큐)
def BFS(self):
    # 너비우선탐색, BFS(Breadth First Search)
    # Queue 이용
    result = []
    queue = [self.root]

    while queue:
        current = queue.pop(0)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
        result.append(current.data)

    return result
