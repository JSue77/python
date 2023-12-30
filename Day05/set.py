#자료 구조(data_structure)
#자료 구조는 컴퓨터 안에서 데이터를 어떻게 보관하고 다루는지에 대한 방법을 말합니다.
#이것은 마치 서류를 정리하는 서랍장과 같습니다.
#자료구조는 데이터를 어떻게 저장하고 사용할지 정하는 규칙을 제공합니다.
#파이썬에서는 주로 사용되는 몇 가지 기본 자료구조가 있습니다.

#리스트(List)
#*리스트의 생성: my_list = [1,2,3]

#3.제거
#remove, pop, clear


#세트(Set)
#coffee = ['아메리카노', '라떼', '바닐라'] #리스트
#burger = {'치즈버거', '새우버거', '불고기버거','치즈버거'} #set 중복제거 해줌
#print(burger)

#burger.add(4)
#print(burger)

#burger.remove(2) #요소가 세트에 없으면 오류 발생


#세트를 만드는 방법
#a = {}
#b = {1,2,3,4,5,6}
#c = set(1,2,3,4,5,6)

#quiz
#뉴스기사 가져와서, 단어를 리스트화 시켜, 중복제거 없이 보여주세요.

article = """The war on Europe's eastern borders is going badly for Ukraine. That means, by extension, it is going badly for Nato and the EU, which have bankrolled Ukraine's war effort and its economy to the tune of tens of billions of dollars.

This time last year, hopes were high in Nato that, supplied with modern military equipment and intensive training in Western countries, Ukraine's army could press home the advantage it had gained that autumn and push the Russians out of much of the territory they had seized. That hasn't happened.

The problem has been one of timing. Nato countries took a long time making their mind up about whether they dared send modern Main Battle Tanks like Britain's Challenger 2 and Germany's Leopard 2 to Ukraine, in case it provoked President Vladimir Putin into some sort of rash retaliation.

In the end, the West delivered the tanks, President Putin did nothing. But by the time they were ready to be deployed on the battlefield in June, Russian commanders had looked at the map and rightly guessed where Ukraine's main effort was going to be."""

words = article.split()
words.sort()
print(words)

#set(words) #set([1,2,3,1,2,3]) > 1,2,3 set([단어들])
filteredWords = list(set(words))
print(filteredWords)



