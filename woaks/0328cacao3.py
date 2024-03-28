import re

s = 'aabbaccc'
for i in range(1, len(s)//2+1):
    패턴 = f'[a-z]{{{i}}}'
    print(패턴)

import re

s = 'aabbaccc'
for i in range(1, len(s)//2+1):
    패턴 = f'[a-z]{{{i}}}'
    print(패턴)
    패턴 = re.compile(패턴)
    print(패턴.findall(s))

import re

def solution(s):
    if len(s) == 1:
        return 1
    문자열길이 = []

    for 표현식 in range(1, len(s)//2+1):
        ss = f'[a-z]{{{표현식}}}'
        패턴 = re.compile(ss)
        압축문자열 = ''
        잘라진문자열 = 패턴.findall(s)
        count = 1
        for i in range(len(잘라진문자열)-1):
            if 잘라진문자열[i] == 잘라진문자열[i+1]:
                count += 1
            else:
                if count > 1:
                    압축문자열 += f'{count}{잘라진문자열[i]}'
                    count = 1
                else:
                    압축문자열 += f'{잘라진문자열[i]}'
            if i == len(잘라진문자열)-2:
                if count > 1:
                    if 잘라진문자열[i] == 잘라진문자열[i+1]:
                        압축문자열 += f'{count}{잘라진문자열[i]}'
                else:
                    압축문자열 += f'{잘라진문자열[i+1]}'

        if len(s) % 표현식 != 0:
            압축문자열 += s[-(len(s) % 표현식):]
        문자열길이.append(len(압축문자열))
    return min(문자열길이)