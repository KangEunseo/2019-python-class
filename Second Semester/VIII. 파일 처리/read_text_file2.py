f1 = open("history.ama", "r", encoding="utf-8")
sum = 0

while True:
    data = f1.readline()
    if not data:
        break
    print(data, end="")
    l = data.split()    # 화이트 스페이스 : \t, \n, 띄어쓰기 있는 걸 다 자름
    sum += int(l[1])
    print("총 금액 : %d원" % sum)
    # 한 줄 안에서 이름, 가격 등등 자르기
    # 총 금액 계산하고 출력하기

f1.close()