#랜덤은 내장함수가 아니다.
#import random

import random
#random.randint("시작", "끝") #정수만
#a = random.randint(1, 10000)
#print(a)

#random.choice(리스트)
#a = random.choice(['아이스 아메리카노', '라떼', '디카페인', '바닐라'])
#print(a)

#random.uniform("시작", "끝") 실수 아무거나 뽑기
#random.shuffle(리스트) 리스트가 랜덤으로 섞임

#quiz
#len()
#len([1,2,3,4,5]) #5
#len("mega") #4

#lang = input("아무 글 입력:")
#list_lang = list(lang)
#print(list_lang)
#print(len(lang))

#크리스마스 to-do-list
#크리스마스 때 할일을 리스트화 시키고
#랜덤으로 할일을 재출력하기!

#크리스마스 할일: 나홀로집에보기 유튜브보기 자기 카톡할까말까하기
#-> 자기 나홀로집에보기 카톡~ 유튜브~

import random
#list = ['나홀로집에보기', '카드쓰기', '케이크사기', '잠자기']
#list = ramdom.choice(['나홀로집에보기', '카드쓰기', '케이크사기', '잠자기'])
#print(list)

#a = random.randint(1, 45)

#쌤풀이
todo = input("크리스마스 할일:")
todolist = todo.split(",")
random.shuffle(todolist)
print(f"크리스마스 할일: {todolist}")

#2.로또번호 리스트 출력하기

#lotto = []
#방식1
#a = random.randint(1,45)
#b = random.randint(1,45)
#c = random.randint(1,45)
#d = random.randint(1,45)
#e = random.randint(1,45)
#f = random.randint(1,45)

#lotto.append(a)
#lotto.append(b)

#lotto.append(random.randint(1,45))
#lotto.append(random.randint(1,45))
#lotto.append(random.randint(1,45))
#lotto.append(random.randint(1,45))
#lotto.append(random.randint(1,45))
#lotto.append(random.randint(1,45))
#lotto.append(random.randint(1,45))

#lotto.sort()
#print(lotto)


