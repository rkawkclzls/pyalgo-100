def solution(array, height):
    return len([x for x in array if x > height])

print(solution([149, 180, 192, 170], 167))

def solution(n):
    return sum(int(digit) for digit in str(n))

def solution(n):
    return sum(int(digit) for digit in str(n))

def solution(numbers, direction):
    if direction == "right":
        return [numbers[-1]] + numbers[:-1]
    else:  
        return numbers[1:] + [numbers[0]]

from collections import deque

l = [1, 2, 3, 4, 5, 6, 7]
d = deque(l)

d.rotate(2)
print(d)

d.rotate(-2)
d

print(dir(d))

dir(d)

# 'append'
# 'appendleft'

# 'clear'
# 'copy'
# 'count'

# 'extend'
# 'extendleft'

# 'index'
# 'insert'

# 'maxlen' # 이 기능도 정말 많이 사용합니다. LRU 알고리즘 같은 곳에서 많이 사용합니다.

# 'pop'
# 'popleft'

# 'remove'
# 'reverse'

# 'rotate'
from collections import deque

def solution(numbers, direction):
    numbers = deque(numbers)
    if direction == 'right':
        numbers.rotate(1)
    else:
        numbers.rotate(-1)
        return list(numbers)

def solution(my_string):
    for char in my_string:
        if not char.isdigit():
            my_string = my_string.replace(char, ' ')
    numbers = my_string.split()
    return sum(map(int, numbers))

my_string = 'aAb1B2cC34oOp'

# 1. findall로 숫자만 뽑는다.
# 2. sub로 문자를 지운다
# 3. split으로 모든 문자를 split기준으로 삼고 sum한다.

import re

s = 'aAb1B2cC34oOp'
re.split('[a-zA-Z]', s)

def solution(babbling):
    count = 0
    for word in babbling:
        if word.count('aya') <= 1 and word.count('ye') <= 1 and word.count('woo') <= 1 and word.count('ma') <= 1:
            if word.replace('aya', '').replace('ye', '').replace('woo', '').replace('ma', '') == '':
                count += 1
    return count

import re

def solution(babbling):
    count = 0
    for word in babbling:
        if not re.search(r'(aya.*aya|ye.*ye|woo.*woo|ma.*ma)', word) and re.fullmatch(r'(aya|ye|woo|ma)*', word):
            count += 1
    return count