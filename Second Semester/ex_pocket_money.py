# 국어, 영어, 자바, 수학, 파이썬, JSP
# 총점, 평균 구하기
# 용돈 구하기 ( 90점 이상 - 10만원, 80점 이상 8만원, 70점 이상 7만원, 60점 이상 6만원, 그 이하 5만원 )

score1 = int(input("국어 점수를 입력하세요 >> "))
score2 = int(input("영어 점수를 입력하세요 >> "))
score3 = int(input("자바 점수를 입력하세요 >> "))
score4 = int(input("수학 점수를 입력하세요 >> "))
score5 = int(input("파이썬 점수를 입력하세요 >> "))
score6 = int(input("JSP 점수를 입력하세요 >> "))
sum = score1 + score2 + score3 + score4 + score5 + score6
avg = sum/6
print("총점:", sum)
print("평균:", round(avg, 2))

if avg >= 90:
    print("90점 이상, 용돈 10만원")
elif avg >= 80:
    print("80점 이상, 용돈 8만원")
elif avg >= 70:
    print("70점 이상, 용돈 7만원")
elif avg >= 60:
    print("60점 이상, 용돈 6만원")
elif avg < 60:
    print("60점 미만, 용돈 5만원")