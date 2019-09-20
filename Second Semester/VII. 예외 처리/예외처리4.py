#p217

l = [1, 2, 3]
try:
    print(l[1])
    print(l[2])
    print(l[4]) #IndexError: list index out of range
except IndexError as e:
    print("Index Error")
    print(e)
else:
    print("성공적으로 모든 코드를 실행")