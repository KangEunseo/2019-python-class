# from repeater import *
import repeater as re

s = input("반복할 문자를 입력하세요 : ")
n = input("반복 횟수를 입력하세요 : ")
# repeater.repeat(s, int(n))
# repeater.repeat(2)
# repeater.once(2)
re.repeat(s, int(n))
re.repeat(s)
re.once(s)