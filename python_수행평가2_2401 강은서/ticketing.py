# 2401 강은서
from ticket import Ticket
from student import Student
import sys

# Ticketing 클래스
class Ticketing(Student, Ticket):

    # Ticketing 객체 생성자
    def __init__(self):
        pass
    
    # 티켓팅하는 함수
    def ticketing(self):
        # 티켓 명단 세팅
        self.setList()
        # 학생 한 명 추가(현재 학생이 한 명도 없는 상태)
        self.addStuent()
        # 학생 명단 세팅
        self.setStudents()
        # 학생 명단 출력
        self.getStudents()

        # 반복문
        while(True):
            self.gostop = input("티켓팅을 시작하시겠습니까?(예:y, 아니오:n) ")
            # 티켓팅 시작할건지 질문, y나 Y 입력시 티켓팅 시작
            if(self.gostop == "y" or self.gostop == "Y"):
                # 티켓 명단 출력
                self.getList()
                # 선택할 티켓 번호 입력
                self.what = int(input("선택하신 티켓의 번호를 입력하세요: "))
                # 선택한 티켓이 명단에 있을 경우
                if(self.what <= len(self._tlist)):
                    # 선택한 티켓의 개수가 1개 이상일 경우
                    if(self._firstPeoples[self.what-1] > 0):
                        # 학생 명단 출력
                        self.getStudents()
                        self.temp1 = input("이름을 입력하세요: ")
                        self.temp2 = input("학번을 입력하세요: ")
                        # 학생 이름과 학번이 일치하는지 확인
                        if(self.temp1 in self.std_name and self.temp2 == self.std_num[self.std_name.index(self.temp1)]):
                            print("[학생 확인 완료] 티켓이 예매 되었습니다. 담당 선생님에게 수령하세요.")
                            # 티켓 선착 인원 1명 줄이기
                            self._firstPeoples[(self.what-1)] -= 1
                            # 티켓 명단 세팅
                            self.setList()
                        # 학생 이름과 학번 일치하지 않는 경우
                        else:
                            # 학생 추가할건지 질문, y나 Y 입력시 학생 추가
                            self.temp = input("학생 정보 확인이 불가능합니다. 학생을 추가하시겠습니까?(예:y, 아니오:n) ")
                            if(self.temp == "y" or self.temp == "Y"):
                                # 학생 추가
                                self.addStuent()
                                # 학생 명단 세팅
                                self.setStudents()
                                # 학생 명단 출력
                                self.getStudents()
                                print("학생 정보 추가가 완료되었습니다.")
                            else:
                                print("티켓팅 초기 화면으로 돌아갑니다.")
                                # 건너뛰고 while문 처음부터 실행
                                continue
                    # 선택한 티켓의 개수가 0개일 경우
                    else:
                        print("티켓 수량이 매진되었습니다.")
                        # 티켓 삭제
                        self.deleteTicket()
                        # 티켓 명단 세팅
                        self.setList()
                        # 티켓팅 초기 화면으로 돌아갈건지 질문, y나 Y 입력시 contine문 실행
                        self.temp = input("티켓팅 초기 화면으로 돌아가시겠습니까?(예:y, 아니오:n) ")
                        if(self.temp == "y" or self.temp == "Y"):
                            # 건너뛰고 while문 처음부터 실행
                            continue
                        else:
                            print("티켓팅을 종료합니다.")
                            # 티켓팅 종료
                            sys.exit()
                # 선택한 티켓이 명단에 없을 경우
                else:
                    # 티켓 추가할건지 질문, y나 Y 입력시 티켓 추가
                    self.temp = input("존재하지 않는 티켓입니다. 티켓을 추가하시겠습니까?(예:y, 아니오:n) ")
                    if(self.temp == "y" or self.temp == "Y"):
                        # 티켓 추가
                        self.addTicket()
                        # 티켓 명단 세팅
                        self.setList()
                    else:
                        # 건너뛰고 while문 처음부터 실행
                        continue
            else:
                print("티켓팅을 종료합니다.")
                # 티켓팅 종료
                sys.exit()