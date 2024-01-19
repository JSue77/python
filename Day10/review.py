#1. 랜덤(1~100)을 이용해서 길이가 10인거 구현하고 출력 후, 여기서 홀수/짝수 나누고 출력하기

import random
numList = []
for i in range(10):
    numList.append(random.randint(1,101))
print(numList)

oddList = []
evenList = []
for i in numList:
    if i % 2 == 0:
        evenList.append(i)
    else:
        oddList.append(i)

#numList = [random.randint(1,101) for i in range(10)] 최적화


#2. 랜덤(1~30) 리스트를 뽑고, 1~10은 '토끼' 20~30 '호랑이'

numList = [random.randint(1:31) for i in range(10)]
zooList = []
for i in numList:
    if 1 <= i and i < 10:
        zooList.append('🐇')
    elif 11 <= and i <20:
        zooList.append('호랑이')
    else:
        zooList.append('개')

print(numList)
pirtn(zooList)

#3.

def makeList(m,n):
   return [random.randint(m,n+1) for i in range(5)]

lambda m,n : [random.randint(m,n+1) for i in range(5)]

