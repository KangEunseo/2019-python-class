import tkinter
import tkinter.font
import tkinter.ttk
import re
from GuiMysqlClass import SQL

class programManager():
    window = tkinter.Tk() #GUI 창 생성

    window.title("Pit a Pet") #GUI title 지정
    window.geometry("700x500") #GUI 창 크기 지정
    window.resizable(False, False) #GUI 창 크기 못 바꾸게 하기

    def __init__(self): #최초 실행 창
        self.clear()

        img = tkinter.PhotoImage(file="img/logo.png")
        label = tkinter.Label(self.window, image=img)
        label.place(x=250, y=60)

        global font
        font = tkinter.font.Font(family="맑은 고딕", size="12")

        signInBtn = tkinter.Button(self.window, width=22, borderwidth=0, cursor="heart", command=self.signInf,
                                  text="로그인", bg="white", pady=5, font=font, activebackground="ivory")
        signInBtn.place(x=248, y=290)

        signUpBtn = tkinter.Button(self.window, width=22, borderwidth=0, cursor="heart", command=self.signUpf,
                                  text="회원가입", bg="white", pady=5, font=font, activebackground="ivory")
        signUpBtn.place(x=248, y=345)

        self.window.mainloop()

    def signInf(self): #로그인 폼
        self.clear()

        font_ = tkinter.font.Font(family="맑은 고딕", size="15", weight="bold")
        tkinter.Label(text="로그인", font=font_, fg="light coral").place(x=340, y=80)

        global inpnum
        tkinter.Label(text="회원번호", font=font).place(x=260, y=165)
        inpnum = tkinter.Entry(self.window, width=20)
        inpnum.place(x=350, y=170)

        global inpname
        tkinter.Label(text="이름", font=font).place(x=260, y=205)
        inpname = tkinter.Entry(self.window, width=20)
        inpname.place(x=350, y=210)

        signInBtn = tkinter.Button(self.window, width=10, borderwidth=0, cursor="heart", command=self.signIn,
                                   text="로그인", bg="pink", font=font, activebackground="ivory")
        signInBtn.place(x=260, y=300)

        signUpBtn = tkinter.Button(self.window, width=13, borderwidth=0, cursor="heart", command=self.signUpf,
                                   text="회원가입", bg="white", font=font, activebackground="ivory")
        signUpBtn.place(x=370, y=300)

    def signIn(self): #로그인
        sql = SQL()

        if (inpnum.get().isdigit() == False):
            tkinter.Label(text="회원번호를 숫자로 입력해주세요!", fg="red", width=40).place(x=298, y=190)
        else:
            if (sql.selectpnum() < int(inpnum.get())):
                tkinter.Label(text="존재하지 않는 회원번호입니다!", fg="red", width=40).place(x=292, y=190)
            if(inpname.get() == None or inpname.get() == ''):
                tkinter.Label(text="이름을 입력하세요!", fg="red", width=40).place(x=260, y=230)
            else:
                global pname
                pname = sql.selectp(int(inpnum.get())) #입력한 번호에 해당하는 튜플의 이름 DB에서 받아오기

                if pname == inpname.get(): #DB에 있는 이름이랑 입력한 이름이 같은지 확인
                    self.clear()
                    tkinter.Label(text="로그인이 완료되었습니다.", font=font).place(x=260, y=200)
                    tkinter.Button(self.window, width=10, borderwidth=0, cursor="heart", command=self.main,
                                   text="확인", bg="white", font=font, activebackground="ivory").place(x=305, y=240)
                else:
                    self.clear()
                    tkinter.Label(text="유저를 찾을 수 없습니다. 다시 시도하세요.", font=font).place(x=200, y=200)
                    tkinter.Button(self.window, width=10, borderwidth=0, cursor="heart", command=self.signInf,
                                   text="로그인", bg="white", font=font, activebackground="ivory").place(x=305, y=240)

    def signUpf(self): #회원가입
        self.clear()

        font_ = tkinter.font.Font(family="맑은 고딕", size="15", weight="bold")
        tkinter.Label(text="회원가입", font=font_, fg="light coral").place(x=333, y=80)

        global pname
        tkinter.Label(text="이름", font=font).place(x=260, y=145)
        pname = tkinter.Entry(self.window, width=20)
        pname.place(x=350, y=150)

        global tel
        tkinter.Label(text="전화번호", font=font).place(x=260, y=185)
        tel = tkinter.Entry(self.window, width=20)
        tel.place(x=350, y=190)

        global address
        tkinter.Label(text="주소", font=font).place(x=260, y=225)
        address = tkinter.Entry(self.window, width=20)
        address.place(x=350, y=230)

        signInBtn = tkinter.Button(self.window, width=10, borderwidth=0, cursor="heart", command=self.signInf,
                                   text="로그인", bg="white", font=font, activebackground="ivory")
        signInBtn.place(x=260, y=300)

        signUpBtn = tkinter.Button(self.window, width=13, borderwidth=0, cursor="heart", command=self.signUp,
                                   text="회원가입", bg="pink", font=font, activebackground="ivory")
        signUpBtn.place(x=370, y=300)

    def signUp(self):  #회원가입
        if(pname.get() == None or pname.get() == ''):
            tkinter.Label(text="이름을 입력하세요!", fg="red", width=20).place(x=330, y=169)
        else:
            sql = SQL()
            sql.insertp(str(pname.get()), str(tel.get()), str(address.get())) #입력한 내용들 member DB에 넣기
            self.clear()
            tkinter.Label(text="회원가입이 완료되었습니다. 회원번호는 "+str(sql.selectpnum())+"입니다.", font=font).place(x=180, y=200)
            tkinter.Button(self.window, width=10, borderwidth=0, cursor="heart", command=self.signInf,
                            text="로그인", bg="white", font=font, activebackground="ivory").place(x=305, y=240)

    def main(self): #로그인 시 실행되는 메인 화면
        self.clear()

        tkinter.Button(self.window, width=7, borderwidth=0, cursor="heart", command=self.heartP,
                        text="관심♥", bg="white", font=font, activebackground="ivory").place(x=23, y=30)

        tkinter.Label(text=pname+"님", font=font, fg="light coral").place(x=520, y=33)
        logoutBtn = tkinter.Button(self.window, width=10, borderwidth=0, cursor="heart", command=self.__init__,
                                   text="로그아웃", bg="white", font=font, activebackground="ivory")
        logoutBtn.place(x=580, y=30)
        
        frame = tkinter.Frame(self.window)
        scrollbar = tkinter.Scrollbar(frame)
        scrollbar.pack(side="right", fill="y")
        self.listbox = tkinter.Listbox(frame, yscrollcommand=scrollbar.set, width=55, font=font)
        sql = SQL()
        list = sql.selecta() #animal 테이블에서 값 받아오기
        count = 0
        for i in list:
            self.listbox.insert(count, (str(i['anum'])+" - "+str(i['akind'])+" / "+str(i['astate'])+
                                   " / "+str(i['agender'])))
            count = count + 1
        self.listbox.bind('<<ListboxSelect>>', self.read)
        self.listbox.pack(side="left")
        scrollbar["command"] = self.listbox.yview
        frame.place(x=100, y=140)

        tkinter.Button(self.window, width=7, borderwidth=0, cursor="heart", command=self.writef,
                       text="글쓰기", bg="pink", font=font, activebackground="ivory").place(x=605, y=435)

    def heartP(self): #관심동물
        self.clear()
        tkinter.Label(text="아직 구현되지 않은 기능입니다.", font=font).place(x=260, y=200)
        tkinter.Button(self.window, width=10, borderwidth=0, cursor="heart", command=self.main,
                       text="확인", bg="white", font=font, activebackground="ivory").place(x=305, y=240)

    def writef(self):
        self.clear()
        
        font_ = tkinter.font.Font(family="맑은 고딕", size="15", weight="bold")
        tkinter.Label(text="글쓰기", font=font_, fg="light coral").place(x=340, y=80)

        global akind
        tkinter.Label(text="동물 종류", font=font).place(x=260, y=125)
        akind = tkinter.Entry(self.window, width=20)
        akind.place(x=350, y=130)

        tkinter.Label(text="분양 종류", font=font).place(x=260, y=165)
        self.chVar = tkinter.IntVar()
        self.astate1 = tkinter.ttk.Radiobutton(text="임시보호", variable=self.chVar, value=1)
        self.astate2 = tkinter.ttk.Radiobutton(text="입양", variable=self.chVar, value=2)
        self.astate3 = tkinter.ttk.Radiobutton(text="임시보호 & 입양", variable=self.chVar, value=3)
        self.astate1.place(x=350, y=170)
        self.astate2.place(x=440, y=170)
        self.astate3.place(x=350, y=190)

        tkinter.Label(text="성별", font=font).place(x=260, y=215)
        self.radVar = tkinter.IntVar()
        self.agender1 = tkinter.ttk.Radiobutton(text="암컷", variable=self.radVar, value=1)
        self.agender2 = tkinter.ttk.Radiobutton(text="수컷", variable=self.radVar, value=2)
        self.agender1.place(x=350, y=220)
        self.agender2.place(x=420, y=220)

        global amail
        tkinter.Label(text="메일 주소", font=font).place(x=260, y=258)
        amail = tkinter.Entry(self.window, width=20)
        amail.place(x=350, y=260)

        tkinter.Button(self.window, width=10, borderwidth=0, cursor="heart", command=self.write,
                                   text="작성완료", bg="pink", font=font, activebackground="ivory").place(x=340, y=300)

    def write(self):
        if akind.get() == None or akind.get() == '':
            tkinter.Label(text="동물 종류를 입력하세요!", fg="red", width=20).place(x=347, y=169)
        else:
            gender = self.genderChecked()
            state = self.stateChecked()
            sql = SQL()
            sql.inserta(str(akind.get()), state, gender, str(amail.get())) #입력한 내용 animal DB에 넣기

            self.main()

    def read(self, none): #게시물 보기 -> 입양 신청
        value = str(self.listbox.curselection())
        number = re.findall("\d+", value)[0]
        self.clear()

        sql = SQL()

        font_ = tkinter.font.Font(family="맑은 고딕", size="15", weight="bold")
        tkinter.Label(text="게시글", font=font_, fg="light coral").place(x=340, y=80)

        tkinter.Label(text="동물 종류 : " + sql.selectakind(number), font=font).place(x=260, y=125)

        tkinter.Label(text="분양 종류 : " + sql.selectastate(number), font=font).place(x=260, y=165)

        tkinter.Label(text="성별 : " + sql.selectagender(number), font=font).place(x=260, y=215)

        self.pmail = tkinter.Label(text="메일 주소 : " + sql.selectamail(number), font=font)
        self.pmail.place(x=260, y=258)

        tkinter.Button(self.window, width=10, borderwidth=0, cursor="heart", command=self.main,
                                   text="홈으로", bg="white", font=font, activebackground="ivory").place(x=260, y=300)

        tkinter.Button(self.window, width=10, borderwidth=0, cursor="heart", command=self.applyf,
                       text="입양신청", bg="pink", font=font, activebackground="ivory").place(x=370, y=300)

    def applyf(self):
        self.clear()

        font_ = tkinter.font.Font(family="맑은 고딕", size="15", weight="bold")
        tkinter.Label(text="입양 신청", font=font_, fg="light coral").place(x=340, y=80)

        global contact
        tkinter.Label(text="연락처", font=font).place(x=260, y=195)
        contact = tkinter.Entry(self.window, width=20)
        contact.place(x=350, y=200)

        tkinter.Button(self.window, width=10, borderwidth=0, cursor="heart", command=self.apply,
                       text="신청하기", bg="pink", font=font, activebackground="ivory").place(x=340, y=300)

    def apply(self):
        self.clear()
        tkinter.Label(text="아직 구현되지 않은 기능입니다.", font=font).place(x=260, y=200)
        tkinter.Button(self.window, width=10, borderwidth=0, cursor="heart", command=self.main,
                       text="확인", bg="white", font=font, activebackground="ivory").place(x=305, y=240)
        # sql = SQL()
        # sql.sendmail(self.pmail, str(contact.get()))

    def clear(self): #GUI 창에 있는 위젯들 제거
        mylist = self.window.place_slaves()
        for i in mylist:
            i.destroy()

    def stateChecked(self): #radio버튼 값 받아오기
        astate = ""
        if self.radVar.get() == 1:
            astate = "임시보호"
        elif self.radVar.get() == 2:
            astate = "입양"
        elif self.radVar.get() == 3:
            astate = "임시보호 & 입양"

        return astate

    def genderChecked(self): #radio버튼 값 받아오기
        agender = ""
        if self.radVar.get() == 1:
            agender = "암컷"
        elif self.radVar.get() == 2:
            agender = "수컷"

        return agender