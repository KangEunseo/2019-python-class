# 일주일에 얼마나 일하는지, 몇 주 일하는지, 시급 얼마인지 입력하면 총 알바비 계산
# 주 15시간 이상이면 주휴수당 지급 (주휴수당은 5일 일한 것에 1일치 급여 더 지급)

week = int(input("한 달에 몇 주 일해? >> "))
hour = int(input("일주일에 몇 시간 일해? >> "))
hourMoney = int(input("시급 얼마받아? >> "))
if hour >= 15:
    week += (week/5)
salary = week * hour * hourMoney
print("알바비는", salary, "원")