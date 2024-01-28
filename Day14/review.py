import pandas
import random
from faker import Faker
fake = Faker('ko_KR')


ageList = [20,30,40,50]
gender = ['m','f','f','f','f'] #2:8
#genderPer = [20,80] #choices : genderPer 단순 고를 때 choice
itemList = ['바디워시', '선크림', '스킨', '로션', '샴푸', '스낵', '향수', '헤어제품']
timeList = ['아침', '점심', '저녁', '밤']

data = {
    'name': [fake.name() for i in range(100)],
    'age': [random.choice(ageList) for i in range(100)],
    'gender': [random.choice(gender) for i in range(100)],
    'item': [random.choices(itemList) for i in range(100)],
    'time': [random.choices(timeList) for i in range(100)],
}

df = pandas.DataFrame(data)
df.to_csv('olive.csv', encoding='utf-8-sig',index=False)
