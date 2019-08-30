# 115쪽 혼자해보기

def star(space, *num):
    for i in num:
        print(space*i)

star("♬", 3)
star("♡", 1, 2, 3)



# 116쪽

def fn(a, b, c, d, e):
    print(a, b, c, d, e)

fn(1, 2, 3, 4, 5)
fn(10, 20, 30, 40, 50)
fn(5, 6, 7, 8, 9)
fn(a=1, b=2, c=3, d=4, e=5)
fn(e=5, d=4, c=3, b=2, a=1)
fn(1, 2, c=3, e=5, d=4)
# fn(d=4, e=5, 1, 2, 3) 에러



# 117쪽

def fn(a, b, c, *d):
    print(a, b, c, d)

# fn(c=3, b=2, a=1, 4, 5)
# fn(1, 2, c=3, 4, 5)
# fn(4, 5, a=1, b=2, c=3)


# 118쪽

def star(mark, repeat, space, space_repeat, line):
    for i in range(1, line):
        str = (mark * repeat)
        for j in range(2, repeat):
            str = str + (space * space_repeat) + (mark * repeat)
        print(str)

star("*", 2, "+", 3, 5)
star("☆", 5, "+", 3, 5)

def star2(mark, repeat, space, space_repeat, line):
    string = (mark * repeat) + (space * space_repeat) + (mark * repeat)
    for n in range(line):
        print(string)

star("*", 2, "+", 3, 5)
star("☆", 5, "+", 3, 5)

# 119쪽
def hello(msg="안녕하세요"):
        print(msg+"!")

hello("오랜만이에요")
hello("박찌훙")
hello()

def hello2(name="무명", msg="안녕하세요"):
        print(name+"님, "+msg+"!")

hello2("라꽌린", "오랜만이에요")
hello2()
hello2("곽가연")

def hello3(name, msg="안녕하세요"):
        print(name+"님, "+msg+"!")

hello3("김민지", "오랜만이에요")
hello3("김봄이")

def fn2(a, b=[]):
        b.append(a)
        print(b)

fn2(3)
fn2(5)
fn2(10)
fn2(7, [1])

def gugudan(dan=2):
        for i in range(9+1):
                print("{} x {} = {}".format(dan, i, dan*i))

gugudan(3)
gugudan()

# 125쪽

def sum(*numbers):
        sum_value = 0
        for number in numbers:
                sum_value += number
        
        return sum_value

result = sum(1, 3)
print("1 + 3 =", result)
print("1 + 3 + 5 + 7 =", sum(1, 3, 5, 7))

# 126쪽

def min(*numbers):
        min_value = numbers[0]
        for number in numbers:
                if min_value > number:
                        min_value = number
        
        return min_value

print("min(923, 529, 2033) =", min(923, 529, 2033))

def max(*numbers):
        max_value = numbers[0]
        for number in numbers:
                if max_value < number:
                        max_value = number

        return max_value

print("max(923, 529, 2033) =", max(923, 529, 2033))

# 127쪽

def multi_num(multi, start, end):
        result = []
        for n in range(start, end):
                if n % multi == 0:
                        result.append(n)
        return result

print("multi_num(17, 1, 200) =", multi_num(17, 1, 200))
print("multi_num(3, 1, 100) =", multi_num(3, 1, 100))

def min_max(*args):
        min = args[0]
        max = args[0]
        for arg in args:
                if min > arg:
                        min = arg
                if max < arg:
                        max = arg
                
        return min, max

print("min_max(2033, 529, 923, 87, 2017) =", min_max(2033, 529, 923, 87, 2017))
min_value, max_value = min_max(2033, 529, 923, 87, 2017)
print("최저값 :", min_value)
print("최대값 :", max_value)