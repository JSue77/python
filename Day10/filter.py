# map(): 변경!
#x = [1,2,3,4,5]

#newList = list(map(lambda x: x+20,x))
#print(newList)

#filter(): 거름
#newList1 = list(filter(lambda x: x > 3, x))
#print(newList1)

#evenList = list(filter(lambda x: x % 2 == 0, x))
#print(evenList)

numList = [1,2,3,4,5,6,7,8,9,10]
notthreeList = list(filter(lambda x: x % 3 != 0,numList))
print(notthreeList)

squareList = list(filter(lambda x: x**2 > 25, numList))
print(squareList)

overList = list(filter(lambda x: x**2 > 25, numList))
print(overList)

fruits = ['shinemusket', 'mandarin', 'peach', 'apple', 'strawberry', 'banana', 'orange']

#fruitsList = list(filter(lambda x: len(x) > 6, fruits))

#over6fruits = list(filter(lambda x: len(x) >= 6, fruits))
#print(over6fruits)

#sfruits = list(filter(lambda x: 's' in x, fruits))
#filter(lambda x: x.count('s') > 0, fruits)
#print(sfruits)

#단어 갯수가 짝수이고 a가 2개 이상 포함

a= list(filter(lambda x: len(x) % 2 == 0 and x.count('a') >=2, fruits))
print(a)
