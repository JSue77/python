import pandas
#데이터 관리와 분석을 위해 특별히 설계된 라이브러리. 엑셀의 상위 관리 버전
#series, dataframe

#data = {
#    'name': ['아메리카노', '라떼', '바닐라', '모카','민트'],
#    'price': [2500, 3000, 3500, 4000, 4000]
#}
#str(123) #123을 문자열로 바꿔줘
#a = pandas.DataFrame(data) #데이터를 데이터 프레임화 시켜줘
#a.to_csv('megacoffee.csv', encoding='utf-8-sig',index=False)

from faker import Faker

fake = Faker('ko_KR')
print(fake.name())
import random

data = {
    'name':[fake.name() for i in range(500)], #0-499
    'age': [random.randint(20,61) for i in range(500)]
}

a = pandas.DataFrame(data)
a.to_csv('people.csv', encoding='utf-8-sig',index=False)