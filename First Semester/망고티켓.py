#2401 강은서
import sys

# Student 클래스
class Student:
    std_name = []
    std_num = []
    std_total = -1
    _students = []

    def __init__(self, name, num):
        self.std_name.append(name)
        self.std_num.append(num)
        self.std_total += 1

    def addStuent(self):
        self.std_name.append(input("추가할 학생의 이름을 입력하세요: "))
        self.std_num.append(input("추가할 학생의 학번을 입력하세요: "))
        self.std_total += 1
    
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
    
    def setStudents(self):
        self._students.clear()
        for i in range(len(self.std_name)):
            self._students.append(str(i+1)+"   이름: "+self.std_name[i]+" | 학번: "+self.std_num[i])

    def getStudents(self):
        for i in range(len(self._students)):
            print(self._students[i])

# Ticket 클래스
class Ticket:
    _tnames = ["월드 IT쇼 2019"]
    _tinfos = ["날짜: 2019.04.24 ~ 2019.04.27"]
    _firstPeoples = [3]
    _teachers = ["함기훈"]
    t_total = 0
    _tlist = []

    def __init__(self, t_name, t_info, t_firstPeople, t_teacher):
        self._tnames.append(t_name)
        self._tinfos.append(t_info)
        self._firstPeoples.append(int(t_firstPeople))
        self._teachers.append(t_teacher)
        self.t_total += 1

    def addTicket(self):
        self._tnames.append(input("추가할 티켓의 이름을 입력하세요: "))
        self._tinfos.append(input("추가할 티켓의 정보를 입력하세요: "))
        self._firstPeoples.append(int(input("추가할 티켓의 선착 인원을 입력하세요(반드시 정수로 입력하세요): ")))
        self._teachers.append(input("추가할 티켓의 담당 선생님을 입력하세요: "))
        self.t_total += 1

    def deleteTicket(self):
        self.temp = input("삭제할 티켓의 이름을 입력하세요: ")
        for i in range(len(self._tnames)):
            if (self.temp == self._tnames[i]):
                self.t_total -= 1
                del self._tnames[i]
                self.t_name = self._tnames[i-1]
                del self._tinfos[i]
                self.t_info = self._tinfos[i-1]
                del self._firstPeoples[i]
                self.t_firstPeople = self._firstPeoples[i-1]
                del self._teachers[i]
                self.t_teacher = self._teachers[i-1]
        print("티켓이 삭제되었습니다.")

    def setList(self):
        self._tlist.clear()
        for i in range(len(self._tnames)):
            self._tlist.append(str(i+1)+"   티켓 이름: "+self._tnames[i]+" | 티켓 정보: "+self._tinfos[i]+\
                " | 선착 인원: "+str(self._firstPeoples[i])+" | 담당 선생님: "+self._teachers[i])

    def getList(self):
        for i in range(len(self._tlist)):
            print(self._tlist[i])

# Ticketing 클래스
class Ticketing(Student, Ticket):
    def __init__(self):
        pass
    
    def ticketing(self):
        self.setList()
        self.addStuent()
        self.setStudents()
        self.getStudents()

        while(True):
            self.gostop = input("티켓팅을 시작하시겠습니까?(예:y, 아니오:n) ")
            if(self.gostop == "y" or self.gostop == "Y"):
                self.getList()
                self.what = int(input("선택하신 티켓의 번호를 입력하세요: "))
                if(self.what <= len(self._tlist)):
                    if(self._firstPeoples[self.what-1] > 0):
                        self.getStudents()
                        self.temp1 = input("이름을 입력하세요: ")
                        self.temp2 = input("학번을 입력하세요: ")
                        if(self.temp1 in self.std_name and self.temp2 == self.std_num[self.std_name.index(self.temp1)]):
                            print("[학생 확인 완료] 티켓이 예매 되었습니다. 담당 선생님에게 수령하세요.")
                            self._firstPeoples[(self.what-1)] -= 1
                            self.setList()
                        else:
                            self.temp = input("학생 정보 확인이 불가능합니다. 학생을 추가하시겠습니까?(예:y, 아니오:n) ")
                            if(self.temp == "y" or self.temp == "Y"):
                                self.addStuent()
                                self.setStudents()
                                self.getStudents()
                                print("학생 정보 추가가 완료되었습니다.")
                            else:
                                print("티켓팅 화면으로 돌아갑니다.")
                                continue
                    else:
                        print("티켓 수량이 매진되었습니다.")
                        self.deleteTicket()
                        self.setList()
                        self.temp = input("티켓팅 초기 화면으로 돌아가시겠습니까?(예:y, 아니오:n) ")
                        if(self.temp == "y" or self.temp == "Y"):
                            continue
                        else:
                            print("티켓팅을 종료합니다.")
                            sys.exit()
                else:
                    self.temp = input("존재하지 않는 티켓입니다. 티켓을 추가하시겠습니까?(예:y, 아니오:n) ")
                    if(self.temp == "y" or self.temp == "Y"):
                        self.addTicket()
                        self.setList()
                    else:
                        continue
            else:
                print("티켓팅을 종료합니다.")
                sys.exit()

Test = Ticketing()
Test.ticketing()