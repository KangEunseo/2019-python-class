#202쪽
class DeletableClass:
    def __del__(self):
        print("delete")

d=DeletableClass()
del d

#203쪽
class Person:
    def __init__(self, name, age, height):
        self.name=name
        self.age=age
        self.height=height
        print(self.name+"이/가 나타났습니다.")

    def __str__(self):
        return "Person 설명, 이름은 "+self.name+", 키는 "+str(self.height)
    
    def __len__(self):
        return len(self.name)

    def __getitem__(self, key):
        if key == "name":
            return self.name
        if key == "age":
            return self.age
        return None
    
    def __del__(self):
        print(self.name+"이/가 사라졌습니다.")

p=Person("강은서", 17, 161)
print(p)
print(len(p))
print(p["name"])
print(p["age"])
print(p["weight"])
del p
p=Person("양수빈", 19 , 170)