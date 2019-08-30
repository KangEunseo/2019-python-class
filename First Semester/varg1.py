# 가변인수

print("♡")
print("♡", "♪")
print("♡", "♪", "♣")
print("♡", "♪", "♣", "♠")
print("♡", "♪", "♣", "♠", "★")

def p(*args):
    string = ""
    for a in args:
        string += a
    print(string)

p("♡")
p("♡",  "♪", "♣")

def 안녕(*name):
    for n in name:
        print("안녕, "+n)

안녕("가연아", "수빈아", "정윤아", "채린아")

def p(space, space_num, *args): #가변인수는 무조건 뒤에만 사용 가능
        string = args[0]
        for i in range(1, len(args)):
                string += (space * space_num) + args[i]
        print(string)

p(",", 3, "♥", "♪", "§")
p(" ", 2, "☆", "배", "지", "냐", "☆", "H", "B", "D" , "~", "♬")
p("!!!", 1, "훙") #훙만 출력