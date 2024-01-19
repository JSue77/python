#reduce: 누적
from functools import reduce

numList = [1,2,3,4,5]
result = reduce(lambda acc,cur: acc+cur, numList) #acc: 누적 cur:현재값
factorial = reduce(lambda acc,cur: acc*cur,numList)
print(result)
print(factorial)

#map(how,what)
#filter(how,what)
#reduce(how(acc,cur),what)


#def megastudy(call-back 함수): {}
#f(x) = x + 10
# => f(1) = 11
# => f(2) = 12...
#f(g(x)) = ~~  g(x): call-back함수
#eggs = [] recipe = 콜백함수

def eggCooking(eggs, index, recipe):
    recipe(eggs[index])
    print('요리완료!')

eggs = ['🥚','🥚','🥚' ]

def makeSandwith(egg):
    egg = '🥪'
def makeCake(egg):
    egg = '🍰'
def makeFry(egg):
    egg = '🍳'


eggCooking(eggs, index:0, makeCake)
print(eggs)

















