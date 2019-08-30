def gugudan(n):
    print(n,"단을 출력합니다.")
    for i in range(1, 9+1):
        print(n, "x", i, "=", n*i)

if __name__ == '__main__':  # 이 모듈 자체로만 실행할 때, 호출
    gugudan(3)