#groupby
import pandas

df = pandas.read_csv('cgv2.csv')
#groupby_snack = df.groupby('snack').value_counts()
#print(groupby_snack) #스낵 기준으로 그룹핑

#groupby_movies = df.groupby('movie')
#wongka = groupby_movies.get_group('웡카')
#print(wongka)

#group_by_snack = df.groupby('snack') #class가 됨
#movies_by_snack = group_by_snack['movie'].value_counts()
#print(movies_by_snack)  #스낵별로 영화와의 상관관계를 알고 싶어

#group_by_times = df.groupby('times')
#drinks_by_times = group_by_times['drinks'].value_counts()
#print(drinks_by_times)

#group_by_times = df.groupby('times')
#payment_by_times = group_by_times['payment'].value_counts()
#print(payment_by_times)

#apply #적용
#50대이면서 심야에 봤으면 어르신 이벤트를 만들고 해당 됨을 추가
#axis : 축, K; 가중치

def isElderAndNight(row):
    if row['age'] == 50 and row['times'] == '심야':
        return '이벤트 대상😀'
    else:
        return '아님😑'

df['elder_event'] = df.apply(isElderAndNight, axis=1)
print(df)

#'웡카'를 보고 캬라멜 팝곤을 사면 이벤트 대상

#def isCaramel(row):
#    if row['movie'] == '웡카':
#        return '이벤트 대상😀'
#    else:
#        return '아님😑'
#df['wongka_event'] = df.apply(isCaramel, axis=1)
#print(df)

#쌤
def wongkaEvent(row):
    if row['movie'] == '웡카' and row['popcorn'] == '카라멜':
        return '이벤트 대상🍪'
    else:
        return '아님😑'
df['wongkaEvent'] = df.apply(wongkaEvent,axis=1)
print(df)


print(df[df['movie']=='웡카'])
print(df[df['elder_event']=='이벤트 대상😀'])
print(df[df['elder_event']=='이벤트 대상😀'][df['wongkaEvent']=='이벤트 대상🍪'])