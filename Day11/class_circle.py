#class Circle:
#    def __init__(self, r):
#        self.radius = r
#    def get_area(self):
#        return 3.14 * self.radius**2
#    def get_round(self):
#        return 3.14 * self.radius *2

#a = Circle(10)
#print(a.get_area())
#print(a.get_round())

#class triangle:
#    def __init__(self,r,h):
#        self.area = r
#        self.height = h
#    def get_area(self,r,h):
#        return (r * h) % 2


#class triangle:
#    def __init__(self):
#        self.base = base
#        self.height = h
#    def get_area(self):
#        return self.base * self.height * 0.5
#    def get_round(self):
#        return self.base * 3
#class squre:
#    def __init__(self,s):
#        self.side = s
#    def get_area(self):
#        return.self.side * self.side

#1. 은행계좌 클래스
#BankAccount
#def __init__(self, num, name, balance):
#    self.num = num
#    self.name = name
#    self.balance = balance
#def deposit(self):
#    return balance + {money}

#def withdrwal(self):
#    return balance - {money}

#def check(self):
#    return balance

#deposit = ("2345", "Ann", "2000")
#print(deposit(2000))

#쌤

#clss Account:
#    def __init__(self,n,o,b)
#        self.number = n
#        self.owner = o
#        self.balance = b

#    def deposit(self,money):
#        self.balance += money

#    def withdral(self,money):
#        if(self.balance < money):
#            print('잔고가 부족합니다.')
#        else:
#            self.balance -= money
#            print('출금이 되었습니다.')
#    def checkBalance(self):
#        pirnt(f"잔액은 {self.balance} 남았습니다.")

#jeon = Account(n:100, o:'jeon', b:100000)

#jeon.deposit(50000)
#jeon.checkBalance()
#jeon.withdral(500000)
#jeon.checkBalance()


#class ShoppingCart:
#    def __init__(self,list,money):
#        self.list = [list]
#        self.money = money
#    def add(self):
#      self.append([list])
#    def delete(self):
#        self.remove([list])

#a = ShoppingCart("사과",2000)
#a.add("배",1000)


#쌤
class Cart:
    def __init__(self):
        self.itemList = []
        self.total = 0
    #item - dict 형태
    def addItem(self, item):
        print(f"{item['name']}이 추가 되었습니다.")
        self.itemList.append(item)
    def removeItem(self):
        for index, item in enumerate(self.itemList):
            print(f"{index}.{item}")
        num = int(input("삭제할 상품의 번호를 선택하세요."))
        self.itemList.pop(num)
        print('삭제되었습니다.')

    def totalAmount(self):
        total = 0
        for i in self.itemList:
            total += i['price']
            print(f'총 금액은 {total}입니다.')

myCart = Cart()
myCart.addItem({'name':'샴푸', 'price':5000})
myCart.addItem({'name':'린스', 'price':10000})
myCart.addItem({'name':'트리트먼트', 'price':8000})
myCart.addItem({'name':'에센스', 'price':7000})
myCart.removeItem()
myCart.totalAmount()
