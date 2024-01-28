import pandas
import matplotlib.pyplot as plt
import seaborn as sns

df = pandas.read_csv('cgv2.csv')
#times drinks
#1.시간과 음료를 그룹핑
#grouping = df.groupby(['times','drinks'])
#2.크기 계산
#sizeGroup = grouping.size()
#print(sizeGroup)
#3.테이블화
#table = sizeGroup.unstack(fill_value=0)
#print(table)

#plt.rcParams['font.family'] = 'Malgun Gothic'
#sns.heatmap(table, cmap='coolwarm')
#plt.xticks(rotation=45) #x축 글씨 45도 돌리기
#plt.yticks(rotation=45) #y축 글씨 45도 돌리기
#plt.show()

grouping_2 = df.groupby(['movie','snack'])
sizeGroup = grouping_2.size()
table = sizeGroup.unstack(fill_value=0)

plt.rcParams['font.family'] = 'Malgun Gothic'
sns.heatmap(table, cmap='coolwarm')
plt.xticks(rotation=45) #x축 글씨 45도 돌리기
plt.yticks(rotation=45) #y축 글씨 45도 돌리기
plt.show()