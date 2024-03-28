from collections import Counter

def solution(array, n):
    value = Counter(array).get(n)
    return 0 if value == None else value