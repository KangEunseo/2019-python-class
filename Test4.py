# 주차요금 계산
import sys

print("주차시간을 입력하세요.(단위:분)", end=' >> ')
time=int(input())
money=0

if 0<time and time<30+1:
  money=2000
elif time>24*60:
  print("24시간을 넘길 수 없습니다.")
  sys.exit()
else:
  money=2000
  for i in range(31, time+1, 10):
    money+=1000

if money>25000:
  money=25000

print(str(money)+"원")