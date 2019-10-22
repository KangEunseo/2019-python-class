from order import Order
from file_manager2 import FileManager

file_manager = FileManager("history.bin")
sum = 0
history = file_manager.load()
# if len(history) == 0:
#   print("주문내역이 없습니다.")
# else:
for h in history:
    print(h)
    sum += h.price
print("내가 아마스빈에 갖다 바친 돈: "+str(sum)+"원")

o = Order()
o.order_drink()

file_manager.save(history + o.order_menu)