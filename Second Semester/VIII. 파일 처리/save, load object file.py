#p239
import pickle

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return("이름: "+self.name+"\n나이: "+str(self.age))

per1 = Person("정유경", 18)
print(per1)

f = open("object.bin", "wb")
pickle.dump(per1, f)    #per1 객체를 f 파일에 저장
f.close()

f = open("object.bin", "rb")
person = pickle.load(f)
f.close()

print(person)

# f.write(per1.name)
# f.write("\t")
# f.write(per1.age)
# f.write("\n")
# while True:
#     data = f.readline()
#     if not data:
#         break
#     l = data.split()
#     per2 = Person(l[0], l[1])
#     print(per2)

# object list
p1 = Person("정유경", 18)
p2 = Person("정재현", 23)
p3 = Person("강하늘", 33)
people1 = [p1, p2, p3]

f = open("people.bin", "wb")
pickle.dump(people1, f)
f.close()

f = open("people.bin", "rb")
people2 = pickle.load(f)
f.close()
for item in people2:
    print(item)