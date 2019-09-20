f = open("file.txt", "w")

try:
    f.write("Hello World!\n")
    f.write(100)
except NameError:
    print("이름 에러")
except TypeError:
    print("타입 예외 발생(100은 쓸 수 없음)")
except:
    print("모르는 에러")
finally:
    f.close()