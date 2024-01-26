#data = {
# 'name': ['cho', 'son', 'lee', 'hwang', 'lee'],
#    'age': [26,31,24,28,29],
#    'position': ['cf', 'lw', 'rw', 'mf', 'mf'],
#}

#df = pandas.DataFrame(data)
#print(df)
#df.to_csv('soccer.csv',index =False)

#import pandas
import pandas
from faker import Faker
fake = Faker()

#이름:300개
#나이: 10~70 랜덤으로 300개
#커피: ['americano','latte','decaffin', 'milk latte','vanilla','mocha', 'maxim']


from random import randint, choice

nameList = []
ageList = []
coffeeList = []
coffees =  ['americano','latte','decaffin', 'milk latte','vanilla','mocha', 'maxim']
for i in range(300):
    nameList.append(fake.name())
    ageList.append(randint(10,71))
    coffeeList.append(choice(coffees))

data = {
    'name': nameList,
    'age' : ageList,
    'coffee': coffeeList,
}

df = pandas.DataFrame(data)
df.to_csv('megaCoffee.csv',index=False)