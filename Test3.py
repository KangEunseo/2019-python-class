# 전화번호부

Tel={"강은서":"010-4202-7249", "양수빈":"010-1111-2222", "윤수빈":"010-2222-3333",
    "원채연":"010-3333-4444"}

name=input("이름을 입력하세요. : ")
for i in Tel:
  if name in i:
    print(i+" : "+Tel[i])