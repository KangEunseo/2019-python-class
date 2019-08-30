from coffee import Coffee
from bubbletea import Bubbletea

class Order:
    _menus = [Coffee("아메리카노", 1800), Bubbletea("딸기요거트", 3500)]
    def __init__(self):
        self.order_menu = []
        self.order = None

    def show_menu(self):
        print("0: 아메리카노 1800원, 1: 딸기요거트 3500원")

    def sum_price(self):
        sum = 0
        for drink in self.order_menu:
            sum += drink.price

        return sum

    def order_drink(self):
        #<반복>
        while(True):
            # 메뉴 보여주기
            self.show_menu()
            # 주문받기
            # 음료 선택
            self.order = input("음료를 선택하세요: ")
            #  음료 객체 생성
            if self.order == "": #메뉴 선택 안하고 그냥 엔터치면 주문 끝
                break
            drink = Order._menus[int(self.order)]
            #  음료 옵션 정하기
            drink.order()
            # 주문한 음료 리스트에 추가하기
            self.order_menu.append(drink)
        #</반복>
        for drink in self.order_menu:
            print(drink)
        #금액 합계 구하기
            print("총금액: "+str(self.sum_price())+"원")