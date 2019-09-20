# 버스정류장에 도착할 버스 번호 옆에 (여유/보통/혼잡)을 봤을 것이다.
# 보통 25석 전후 ( 0 이상 10 미만: 여유 | 10 이상 20 미만: 보통 | 20 이상: 혼잡)
# 정류장마다 탑승, 하차 인원 입력

sum = 0

while True:
    in_people = input("탑승객 수는? >> ")
    if (in_people == ""):
        break
    in_people = int(in_people)
    out_people = input("하차객 수는? >> ")
    out_people = int(out_people)
    sum += in_people - out_people

print("버스에 있는 사람 수는", sum, "명")

if(0 <= sum < 10):
    print("여유")
elif(10 <= sum < 20):
    print("보통")
elif(20 <= sum):
    print("혼잡")