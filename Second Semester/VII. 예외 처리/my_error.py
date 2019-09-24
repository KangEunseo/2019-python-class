#p219
class MyError(Exception):
    pass

class OddError(Exception):
    def __init__(self, message="no Odd"):
        self.message = message

    def __str__(self):
        return self.message

n = 11
try:
    if n % 2 != 0:
        raise OddError
    else:
        print("%d , n/2 = %d" % (n, n/2))
except OddError as e:
    print("에러 발생", e)