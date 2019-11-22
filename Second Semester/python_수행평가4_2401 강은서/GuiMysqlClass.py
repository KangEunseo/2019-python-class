import pymysql
import smtplib
from email.mime.text import MIMEText

host = 'localhost'
user = 'root'
password = 'mirim2'
db = 'python'

# CREATE TABLE member(
#     pnum INT AUTO_INCREMENT PRIMARY KEY,
#     pname VARCHAR(10) NOT NULL,
#     tel VARCHAR(15) DEFAULT '',
#     address VARCHAR(20) DEFAULT ''
# );

# CREATE TABLE animal(
#     anum INT AUTO_INCREMENT PRIMARY KEY,
#     akind VARCHAR(15) NOT NULL,
#     astate VARCHAR(20) NOT NULL,
#     agender VARCHAR(10) DEFAULT '',
#     amail VARCHAR(100) DEFAULT ''
# );

class SQL:
    def __init__(self): #db 커넥트
        self.conn = pymysql.connect(host=host, user=user, password=password, db=db, charset='utf8')
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)

    def selectp(self, pnum): #member 테이블에서 pname 받아오기
        sql = "SELECT pname FROM member WHERE pnum=%s"
        self.curs.execute(sql, pnum)

        pname = self.curs.fetchone()
        return pname['pname']

    def selectpnum(self): #member 테이블에서 튜플 수 받아오기
        sql = "SELECT COUNT(*) FROM member"
        self.curs.execute(sql)

        num = self.curs.fetchone()
        return num['COUNT(*)']

    def insertp(self, pname, tel, address): #member 테이블 값 삽입하기
        sql = """INSERT INTO member(pnum, pname, tel, address) VALUES (0, %s, %s, %s)"""
        self.curs.execute(sql, (pname, tel, address))
        self.conn.commit()

    def inserta(self, akind, astate, agender, amail): #animal 테이블 값 삽입하기
        sql = """INSERT INTO animal(anum, akind, astate, agender, amail) VALUES (0, %s, %s, %s, %s)"""
        self.curs.execute(sql, (akind, astate, agender, amail))
        self.conn.commit()

    def selecta(self): #animal 테이블에서 전체 값 받아오기
        sql = "SELECT * FROM animal"
        self.curs.execute(sql)

        alist = self.curs.fetchall()
        return alist

    def selectakind(self, anum): #animal 테이블에서 akind 받아오기
        sql = "SELECT akind FROM animal WHERE anum=%s"
        self.curs.execute(sql, anum)

        akind = self.curs.fetchone()
        return akind['akind']

    def selectastate(self, anum): #animal 테이블에서 astate 받아오기
        sql = "SELECT astate FROM animal WHERE anum=%s"
        self.curs.execute(sql, anum)

        astate = self.curs.fetchone()
        return astate['astate']

    def selectagender(self, anum): #animal 테이블에서 agender 받아오기
        sql = "SELECT agender FROM animal WHERE anum=%s"
        self.curs.execute(sql, anum)

        agender = self.curs.fetchone()
        return agender['agender']

    def selectamail(self, anum): #animal 테이블에서 amail 받아오기
        sql = "SELECT amail FROM animal WHERE anum=%s"
        self.curs.execute(sql, anum)

        amail = self.curs.fetchone()
        return amail['amail']

    def sendmail(self, pmail, contact): #메일 보내기
        s = smtplib.SMTP('smtp.gmail.com', 587)          # 세션 생성
        s.starttls()                                     # TLS 보안 시작
        s.login('jbogry7@gmail.com', 'qtylfcuyakyehdij') # 로그인 인증

        msg = MIMEText('분양 신청합니다! ['+contact+"]로 연락 주시면 감사하겠습니다.") # 보낼 메시지 설정
        msg['Subject'] = 'Pit a Pet - 분양 문의입니다.'

        s.sendmail("jbogry7@gmail.com", pmail, msg.as_string()) # 메일 보내기
        s.quit() # 세션 종료