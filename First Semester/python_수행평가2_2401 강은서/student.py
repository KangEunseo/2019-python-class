# 2401 강은서

# Student 클래스
class Student:
    std_name = []
    std_num = []
    std_total = -1
    _students = []

    # Student 객체 생성자
    def __init__(self, name, num):
        self.std_name.append(name)
        self.std_num.append(num)
        self.std_total += 1

    # 학생 추가하는 함수
    def addStuent(self):
        self.std_name.append(input("추가할 학생의 이름을 입력하세요: "))
        self.std_num.append(input("추가할 학생의 학번을 입력하세요: "))
        self.std_total += 1
    
    # 학생 삭제하는 함수
    def deleteStudent(self):
        self.temp = input("삭제할 학생의 이름을 입력하세요: ")
        for i in range(len(self.std_name)-1):
            if (self.temp == self.std_name[i]):
                self.std_total -= 1
                del self.std_name[i]
                self.name = self.std_name[i-1]
                del self.std_num[i]
                self.num = self.std_num[i-1]
                print("학생이 삭제되었습니다.")
    
    # 학생 명단 세팅하는 함수
    def setStudents(self):
        self._students.clear()
        for i in range(len(self.std_name)):
            self._students.append(str(i+1)+"   이름: "+self.std_name[i]+" | 학번: "+self.std_num[i])
    
    #학생 명단 출력하는 함수
    def getStudents(self):
        for i in range(len(self._students)):
            print(self._students[i])