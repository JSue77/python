import pandas

df = pandas.read_csv('cgv2.csv')
print(df.index) #몇개 행
print(df.columns) #몇개 열
print(df.values) #데이터 알려주기
print(df.describe()) #숫자형에 대해서 알려주는 것
print(df['snack']) #[해당 열 보여주기]
print(df[['movie', 'drinks']])
print(df[df['movie'] == '웡카']) #영화 웡카 본 사람들 보여주기
print(df[df['snack'] == '나초']) #나초 먹은 사람들 보여주기
print(df[df['snack']=='나초'] [df['movie']=='웡카']) #나초 먹으면서 '웡카' 본 사람들

#신용카드 and 조조 and 웡카, 30대
print(df[df['payment']=='신용카드'] [df['times']=='조조'] [df['movie']=='웡카'] [df['age']==30])