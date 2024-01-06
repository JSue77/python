#문법적 설탕(syntactic sugar)
#Comprehesion

#a = []
#for i in range(101):
    #a.append(i)

#num = [i for i in range(101)] #0~100까지
#print(num)

#num = [i for i in range(101)]
#double_num = [i**2 for i in range(10)]
#three_num = [i + 3 for i in range(10)]
#print(three_num)

#comprehesion + condition
#even_list = [i for i in range(10) if i % 2 == 0]
#print(even_list)

#유저에게 정수의 범위를 물어보고
#두 숫자의 정수를 입력받고
#해당 범위 정수까지의 공배수의 리스트를
#만드는 프로그램

#a = int(input("정수의 범위:"))
#b = int(input("첫 번째 정수:"))
#c = int(input("두 번째 정수:"))
#d = []
#num = [i for i in range(a) if i % (b * c) == 0]
#print(num)

#a = 3
#b = 5
#num = [i for i in range(1001) if i % a == 0 and i % b == 0]
#num = [i for i in range(1001) if i % (a * b) == 0]
#num = [i for i in range(1,1001,a * b)]
#print(num)

#word = ['coffee', 'cookie', 'sandwich']
#count_word = [len(i) for i in word]
#print(count_word)

article = """They suggest he wanted to scale back No 10's original plans.
They also indicate Mr Sunak was not sure they would stop Channel crossings.
They also suggest he was reluctant to fund reception centres to accommodate migrants instead of using hotels or private housing because "hotels are cheaper".
As prime minister, under pressure from his party, Mr Sunak has made the Rwanda plan one of his top priorities.
The scheme to send some asylum seekers to Rwanda for processing and potentially resettlement, in order to deter people from crossing the English Channel in small boats, was first announced by then-Prime Minister Boris Johnson in April 2022.
"""

#word_list = article.split()
#six_bigger_word_list = [i for i in word_list if i.isalpha() and len(i) >= 6]
#six_bigger_word_list.sort()
#print(six_bigger_word_list)

#newNews = news.split()
#count_news = [i for i in newNews if len(i) > 6]
#newNews.append(count_news)
#print(count_news)

#컴프리헨젼 심화 조건부 심화
#[i for i in range(101)]
#print([i if i % 2 == 0 else 'A' for i in range(101)])


#[i if i i.isalum == '3','6','9' :'😱' i in range(101)])
#print([i for i in range(101) and i if i i.isalum() = '3','6','9' print('😱')])

#print(['😀'if i % 2 == 0 else i for i in range(1,101)])

#print(['😱' if str(i % 10) in '369' or str(i // 10) in '369' else i for i in range(1,101)])


#소문자 변환: 5글자 이하는 소문자화, 5글자 이상이면 대문자화
article = """They suggest he wanted to scale back No 10's original plans.
They also indicate Mr Sunak was not sure they would stop Channel crossings.
They also suggest he was reluctant to fund reception centres to accommodate migrants instead of using hotels or private housing because "hotels are cheaper".
As prime minister, under pressure from his party, Mr Sunak has made the Rwanda plan one of his top priorities.
The scheme to send some asylum seekers to Rwanda for processing and potentially resettlement, in order to deter people from crossing the English Channel in small boats, was first announced by then-Prime Minister Boris Johnson in April 2022.
"""
#word_list = article.split()
#six_bigger_word_lsit = [i for i in word_list if i.isalpha()]
#six_bigger_word_list.sort()

#list = [i.upper() if len(i) >= 5 else i.lower() i in six_bigger_word_list]
#no_repeat_list = [i for i in list if list.count() == 1]
#print(no_repeat_list)

#중첩 루프 컴프리헨션(Nested Loop Comprehesion)
#컴프리헨션 내에서 두 개 이상의 반복문을 중첩하여 사용할 수 있습니다. 이는 여러 개의 리스트나 다른 반복 가능한 객체들 간의 조합으로 생성하는데 유용합니다.

#
#[i+j for i in range(3) for j in range()]
#
#[i+j for i in 'abc' for j in '123']
##1) i:a  J:1
#2) i:a, J:2
#3) i:a, J:3

#구구단 #['2*1 =2', '2*2=4'...]
#a = [i = i * j for i in range(2,10) for j in range(2,10)]

#정답
print([f"{i} * {j} = {i * j}" for i in range(2,10) for j in range(2,10)])

#함수와의 결합
#내장함수 사용

#word = ["apple", "banana", "cherry"]
#lengthis = [len(word) for word in words]

#[C] * 9/5 + 32

#celsius = [0,10,20,30,40]
#[i for i in celsius]
#print([i * 9/5 + 32 for i in celsius])

print([i for i in range(1,101) if i % 2 == 0])
