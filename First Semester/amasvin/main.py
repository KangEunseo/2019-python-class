from order import Order
from file_manager import FileManager

#주문내역 불러오고, 보여주기
file_manager = FileManager("history.bin")
# answer = input("주문내역을 보시겠습니까?(y or n)")
# if answer == 'y':
history = []
sum = 0

try:
    history = file_manager.load()
    for h in history:
        print(h)
        sum += h.price
    print("여태까지 내가 아마스빈에 쏟아부은 돈: "+str(sum)+"원")
except FileNotFoundError:
    print("주문내역이 없습니다.")

o = Order()
o.order_drink()

#주문내역 저장하기
file_manager.save(history + o.order_menu)