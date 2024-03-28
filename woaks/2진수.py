
#### 3번
def solution(n, arr1, arr2):
    result = []
    for i, j in zip(arr1, arr2):
        result.append(bin(i | j)[2:].zfill(n).replace('1', '#').replace('0', ' '))
    return result

#### 2번
def solution(record):
    user = {}
    answer = []

    for log in record:
        split_data = log.split(' ')

        if split_data[0] == 'Enter':
            pass
        elif split_data[0] == 'Leave':
            pass
        elif split_data[0] == 'Change':
            pass