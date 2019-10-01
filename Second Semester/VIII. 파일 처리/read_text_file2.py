f1 = open("history.ama", "r", encoding="utf-8")

while True:
    data = f1.readline()
    if not data:
        break
    print(data, end="")
    # 한 줄 안에서 이름, 가격 등등 자르기
    # 총 금액 계산하고 출력하기

f1.close()