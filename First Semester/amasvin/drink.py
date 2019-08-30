class Drink:
    _cups = ["레귤러", "점보"]
    _ices = ["0%", "50%", "100%", "150%"]
    _sugars = ["0%", "50%", "100%", "150%"]

    def __init__(self, name, price):
        self.name=name
        self.price=price
        self.cup=0
        self.ice=2
        self.sugar=2
    
    def __str__(self):
        return "이름: "+self.name+"\t가격: "+str(self.price)+\
            "원\t컵: "+Drink._cups[self.cup]\
            +"\t얼음량: "+Drink._ices[self.ice]\
            +"\t당도: "+Drink._sugars[self.sugar]

    def set_cup(self):
        self.cup=input("컵을 선택하세요(0: 레귤러, 1: 점보) ")
        if self.cup=="":
            self.cup=0
        else:
            self.cup=int(self.cup)
        
        if self.cup==1:
            self.price+=300

    def set_ice(self):
        self.ice=input("얼음량을 선택하세요.(0:0%, 1:50%, 2:100%, 3:150%) ")
        if self.ice=="":
            self.ice=2
        else:
            self.ice=int(self.ice)

    def set_sugar(self):
        self.sugar=input("당도를 선택하세요.(0:0%, 1:50%, 2:100%, 3:150%) ")
        if self.sugar=="":
            self.sugar=2
        else:
            self.sugar=int(self.sugar)

    def order(self):
        self.set_cup()
        self.set_ice()
        self.set_sugar()