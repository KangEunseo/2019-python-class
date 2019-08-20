# from foods.drinks import milk
# milk.drink()

# from foods.drinks.milk import drink
# drink()

#import의 끝이 폴더가 되면 안 된다, 모듈이나 함수여야함. => 모듈, 함수
#from은 폴더가 된다고 해도 ㅇㅈ => 폴더, 모듈
import foods.drinks.milk
foods.drinks.milk.drink()

from foods.drinks import milk as m
m.drink()