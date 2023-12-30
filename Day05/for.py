# 제어문(control stagement)
# 프로그램이 위에서 아래로 순차적 진행
# 1) 조건문 [해당 코드를 실행 할지 말지]
# 2) 반복문 [해당 코드를 n번 반복]

#for x in range(10): #기본 0~9번째까지 반, 10에 끝이남
    #print(x)
    #print("밖에 눈와")

#for x in range(2,10):
  # print(x)

#for x in range(101): #짝수만 출력
    #if x % 2 == 0:
        #print(x)

#3과 5의 공배수만 나타내려면
#for x in range(101):
    #if x % 3 == 0 and x % 5 == 0:
        #or if x % 15 == 0
      #  print(x)


#for i in 'snow':
  # print(i)

#for i in ['apple','banana', 'kiwi']:
   # print(i)


#1. 영단어를 입력했을 때, BbbbB
# -> 대문자 소문자로, 소문자는 대문자로 bBBBb

#2. 영단어를 입력했을 때 모음이 빠진 영단어로 보여주기
# - >apple > ppl

#word = input("영어 단어:")
#for word in ():
        #if word.isupper:
            #print(word.lower)
        #elif word.islower:
            #print(word.upper)

#샘풀이
word = input("영단어 입력:")
text = ''
for i in word:
    if i.isupper():
        text += i.lower()
    else:
        text += i.upper()
print(text)
