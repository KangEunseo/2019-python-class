# 자리 랜덤하게 배치하기

import random

num = input("우리 반 아이들 중 마지막 번호는? : ")
stu_num = list(range(1,int(num)+1))

while True:
    minus_ans = input("제외할 번호를 입력하세요(없는경우 X를 입력하세요) : ")
    if minus_ans == 'X' or minus_ans == 'x' or minus_ans == "":
        break
    else:
        stu_num.remove(int(minus_ans))

print("자리 학생번호")
random.shuffle(stu_num)

for i in range (len(stu_num)):
    print(i+1, stu_num[i])