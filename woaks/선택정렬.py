def 최솟값_인덱스_리턴_함수 (리스트):
    최솟값인덱스 = 0
    for 증가값 in range(0, len(리스트)):
        if 리스트[증가값] < 리스트[최솟값인덱스]:
            최솟값인덱스 = 증가값
    return 최솟값인덱스

def 선택정렬(리스트):
    최종결과값 = []
    while 리스트:
        최솟값_인덱스_저장 = 최솟값_인덱스_리턴_함수(리스트)
        최솟값 = 리스트.pop(최솟값_인덱스_저장)
        최종결과값.append(최솟값)
    return 최종결과값

주어진리스트 = [199, 22, 33, 12, 32, 64, 72, 222, 233]

print(선택정렬(주어진리스트))