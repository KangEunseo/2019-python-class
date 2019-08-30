# 2401 강은서

# Ticket 클래스
class Ticket:
    _tnames = ["월드 IT쇼 2019"]
    _tinfos = ["날짜: 2019.04.24 ~ 2019.04.27"]
    _firstPeoples = [3]
    _teachers = ["함기훈"]
    t_total = 0
    _tlist = []

    # Ticket 객체 생성자
    def __init__(self, t_name, t_info, t_firstPeople, t_teacher):
        self._tnames.append(t_name)
        self._tinfos.append(t_info)
        self._firstPeoples.append(int(t_firstPeople))
        self._teachers.append(t_teacher)
        self.t_total += 1

    # 티켓 추가하는 함수
    def addTicket(self):
        self._tnames.append(input("추가할 티켓의 이름을 입력하세요: "))
        self._tinfos.append(input("추가할 티켓의 정보를 입력하세요: "))
        self._firstPeoples.append(int(input("추가할 티켓의 선착 인원을 입력하세요(반드시 정수로 입력하세요): ")))
        self._teachers.append(input("추가할 티켓의 담당 선생님을 입력하세요: "))
        self.t_total += 1

    # 티켓 삭제하는 함수
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

    # 티켓 명단 세팅하는 함수
    def setList(self):
        self._tlist.clear()
        for i in range(len(self._tnames)):
            self._tlist.append(str(i+1)+"   티켓 이름: "+self._tnames[i]+" | 티켓 정보: "+self._tinfos[i]+\
                " | 선착 인원: "+str(self._firstPeoples[i])+" | 담당 선생님: "+self._teachers[i])

    # 티켓 명단 출력하는 함수
    def getList(self):
        for i in range(len(self._tlist)):
            print(self._tlist[i])