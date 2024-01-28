import pandas
import matplotlib.pyplot as plt

#x = [i for i in range(10)]
#y = [i for i in range(10,20)]
#plt.plot(x,y)
#plt.show()

#df = pandas.read_csv('cgv2.csv')
#print(df)
#movie_groupby_time = df.groupby('times')['movie'].value_counts()
#night_movies = movie_groupby_time['심야']

#plt.rcParams['font.family'] = 'Malgun Gothic' #한글 나오도록 설정
#night_movies.plot.pie(autopct = '%1.1f%%') #숫자 비율을 소수점 1까지 보여주기
#plt.title('심야 영화 파이그래프')
#plt.show()

#영화 너의 이름은 본 사람들 중 스낵 비율

#df = pandas.read_csv('cgv2.csv')
#moives = df.groupby('movie')['너의 이름은'].value_counts()
#snack_by_movie = movies['snack']
#snack_by_movie.plot.pie(autopct='%1.1f%%')
#plt.rcParams['font.family'] = 'Malgun Gothic'
#plt.title('너의 이름은 스낵 비율')
#plt.show()


#쌤
#df = pandas.read_csv('cgv2.csv')
#snack_by_movie = df.groupby('movie')['snack'].value_counts()
#your_name_snacks = snack_by_movie['너의 이름은']

#plt.rcParams['font.family'] = 'Malgun Gothic'
#your_name_snacks.plot.pie(autopct = '%1.1f%%')
#plt.title('너의 이름은 스낵 비율')
#plt.show()
#30대에서 시민덕희 본 사람들의 음료 비율

df = pandas.read_csv('cgv2.csv')
age_group = df.groupby('age').value_counts()
age_30_civil_df = df[df['age']==30][df['movie']=='시민덕희']
drink = age_30_civil_df['drinks'].value_counts()

plt.rcParams['font.family'] = 'Malgun Gothic'
drink.plot(kind='bar')
#drink.plot.pie(autopct = '%1.1f%%')
#age_by_movie.plot.pie(autopct = '%1.1f%%')
plt.title('30대 시민덕희 본 사람 음료 비율')
plt.show()

