# 야구게임
import random

choice_num = list(range(1, 11))
com_num = ["0", "0", "0"]
com_num[0] = str(random.randrange(1, 9, 1))
com_num[1] = com_num[0]
com_num[2] = com_num[0]

while (com_num[0] == com_num[1]):
    com_num[1] = str(random.randrange(1, 9, 1))
while (com_num[0] == com_num[2] or com_num[1] == com_num[2]):
    com_num[2] = str(random.randrange(1, 9, 1))

try_num = 0
strike_count = 0
ball_count = 0

print("숫자야구게임을 시작합니다 !!!")
print("---------------------------")

while ( strike_count < 3 ):
    num = str(input("숫자 3자리를 입력하세요 : "))

    strike_count = 0
    ball_count = 0

    for i in range(0, 3):
        for j in range(0, 3):
            if(num[i] == str(com_num[j]) and i == j):
                strike_count += 1
            elif(num[i] == str(com_num[j]) and i != j):
                ball_count += 1
    print(strike_count, " Strike ", ball_count, " Ball")
    try_num += 1
    
print("---------------------------")
print(try_num, "번 만에 정답을 맞추셨습니다.")