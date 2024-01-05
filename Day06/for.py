#제어문
#조건문
#-if [코드 실행할지 말지 조정]
#반복문
#-for 문[코드를 n번 실행]
import random

#for문 - range()
#for x in range(20): #몇 번 돌리고 싶은지
#    print(f"{x}. 새해 복 많이 받으세요.")

#미니퀴즈
#유저한테 양의 정수(N)을 입력 받고,
#0~n까지의 합을 나타내는 프로그램

#n = int(input("정수를 입력하세요."))
#for x in range(n)

#쌤풀이
#num = int(input("number 입력:")) + 1
#sum = 0
#for i in range(num):
#    sum = sum + i
#    print(sum)

#0~100 사이에서 유저에게 입력 받은 n의 배수의 합을 구하시오.
#2 = > 0~100, 2의 배수의 합
#3 = > 0~100, 3의 배수의 합

#num = int(input("number 입력:"))
#sum = 0
#for i in range(1,100):
   # sum = sum + (num * num)
   # print(sum)

#쌤풀이
#n = int(input("정수 입력:"))
#sum = 0
#for x in range(101):
   #if x % n == 0:
       #sum += x
#print(sum)

#가우스 법칙
#n = int(input("정수 입력:"))
#sum = (n * (n -1))/2
#print(sum)

#for x in range(100):
    #if x % 3 == 0 and x % 5 == 0:
       # print(x)

#두모르간 법칙
#for x in range(100):
    #if not(x % 3 !=0 or x % 5!= 0):
        #print(x)

#for x in 문자열, 리스트, ...
#for x in 'megacoffe':
    #print(x)  #m e g a c o f f ee

#for x in 'mega':
   # if x.isupper():
      # text += x.upper()
   # else:
      #  text += x.lower()
    #print(text)

#모음 제거 프로그램
#bus -> bs
#megacoffee - > mgcff

#1. if spell == 'a' or spell == 'e' or spell or
vowles = ['a','e','i','o','u']
#3. in 연산자

#text = ''
#word = input("영단어 입력:")
#for spell in word:
    #if spell == 'a' or spell == 'e' or spell =='i' or spell =='o' or spell == 'u':
        #text += text
        #pass
    #else:
        #text += spell

#text = ''
#word = input("영단어 입력:")
#for spell in word:
    #if vowles.count(spell) > 0:
        #pass
    #else:
        #text += spell
#print(text)

#리스트
#for x in []

#nation = ['미국', '일본', '중국', '영국', '프랑스']
#for x in nation:
    #print(x) #미국 일본 중국 영국 프랑스

#quiz
#1. num = [] 랜덤 정수(0~10000)를 100개 채우기
#2. num의 평균값 도출하기

#1번
#import random
#num = []
#for i in range(100):
#    num.append(random.randint(1,10001))

#2번 -1)
#for i in num:
#    sum = 0
#    sum += i
#    print(sum/100)

#2번 -2)
#print(sum(num)/len(num))


#3번 - 정수 랜덤 [] 10개 채워주고 - > 리스트의 값의 제곱할 리스트도 보여주기
#랜덤 리스트
#제곱 리스트

#import random
#num = []
#for i in range(10):
   # num.append(random.randint(1, 10001))
   # print(num)

#1. 빈 리스트 만들기
#2. 빈 리스트에 랜덤한 숫자 열개 채우기

#num = []
#import random
#for i in range(10):
#num.append(random.randint(1,101))

#3. 원래 리스트의 제곱한 리스트 만들기
#double_num = []
#for i in num:
    #double_num.append(i**2)
#print(num)
#print(double_num)

#for 변수 in enumerate(n)
#이 함수는 리스트, 문자열 등을 순회하면서, 각 요소의 인덱스와 값을 동시에 얻을 수 있게 해줍니다.

#for index, item in enumerate("askdkdskdkdkdk"):
    #print(index, item)

#break 문 : 종료하고 루프 밖으로 나오는 것
for n in range(1,10):
    if n == 5:
        break
        print(n)

#continue 문
#현재 반복의 나머지 부분을 건너뛰고 다음 반복으로 즉시 넘어갑니다.
