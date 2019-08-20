import random

n = random.randint(1, 6)        # 1 <= x <= 6 랜덤수 x 리턴
print("결과 :", n)
n = random.randrange(1, 6+1)    # 1 <= x < 6+1 랜덤수 x 리턴
print("결과 :", n)
n = random.randint(1, 6)
print("결과 :", n)

def rolling_dice():
    n = random.randint(1, 6)
    print("6면 주사위 굴린 결과 :", n)

rolling_dice()
rolling_dice()
rolling_dice()

def rolling_dice(pip):
    n = random.randint(1, pip)
    print(pip, "면 주사위 굴린 결과 :", n)

rolling_dice(4)
rolling_dice(6)
rolling_dice(10)
rolling_dice(15)

def rolling_dice(pip, repeat):
    for r in range(1, repeat+1):
        n = random.randint(1, pip)
        print(pip, "면 주사위 굴린 결과", r, ":", n)

rolling_dice(4, 2)
rolling_dice(6, 3)
rolling_dice(20, 1)