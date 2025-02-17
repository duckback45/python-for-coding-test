

def solution(n,array):
    # 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
    d = [0] * 100

    # 다이나믹 프로그래밍(Dynamic Programming) 진행 (보텀업)
    d[0] = array[0]
    d[1] = max(array[0], array[1])
    for i in range(2, n):
        d[i] = max(d[i - 1], d[i - 2] + array[i])

    return (d[n - 1])
# 계산된 결과 출력


if __name__ == "__main__" :
    print(solution(5, [1,5,5,3,9]))

