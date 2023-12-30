#조건문 챌린지!

#1.알파벳 탐지기!
#word = input("문자 한 개를 입력해 주세요!")
#if word.isalpha():
    #print("알파벳 입니다.")
#else:
    #print("알파벳이 아닙니다.")

#2. 홀수? 짝수?
#num = int(input("숫자 하나 입력:"))
#if num % 2 == 0:
    #print("짝수")
#else:
    #print("홀수")

#3. UP-Down 게임
#랜덤 함수를 이용해서 임의의 정수를 뽑고, 5번의 기회로 맞혀보세요! 숫자가 너무 높으면 Down, 낮으면 UP, 정답이면 정답

#import random
#pick = []
#num = random.randint(1,100)
#print(num)

#a = pick.append(random.randint(1,100))
#b = pick.append(random.randint(1,100))
#c = pick.append(random.randint(1,100))
#d = pick.append(random.randint(1,100))
#e  =pick.append(random.randint(1,100))
#pick.sort()

if a > num:
    print("down")
else:
    print("up")

if b > num:
     print("down")
else:
    print("up")
if c > num:
    print("down")
else:
    print("up")
if d > num:
    print("down")
else:
    d < num:
    print("")
 e > num:
    print("up")



#4. 점수에 따른 등급과 피드백
score1 = int(input("국어 점수:"))
score2 = int(input("영어 점수:"))
score3 = int(input("수학 점수:"))
total = (score1 + score2 + score3)/3

if 100 >= total < 90:
    print("A")
if 90 >= total <80:
    print("B")
if 80 >= total < 70:
    print("C")
else:
    "과락입니다."

#쌤풀이
#1. 알파벳
alpha = input("문자:")
if alpha.isalpha():
    print("알파벳입니다.")
else:
    print("알파벳이 아닙니다.")

#2. 홀짝
num = int(input("정수 입력:"))
if num % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")

#3. 1.랜덤 숫자 뽑기 -> 2. 정수 맞추기 - > 2-1. 맞추면 끝(정답입니다) -> 2-2. 다시(5번)  #반복문
import random

#answer = random.randint(1,20)
#a = int(input("숫자 입력"))
#if a < answer:
    print("Up!")
#elif a > answer:
    print("Down")
#else:
    print("정답입니다.")

b = int(input("숫자 입력"))
if b < answer:
    print("Up!")
elif b > answer:
    print("Down")
else:
    print("정답입니다.")

c = int(input("숫자 입력"))
if c < answer:
    print("Up!")
elif c > answer:
    print("Down")
else:
    print("정답입니다.")

d = int(input("숫자 입력"))
if d < answer:
    print("Up!")
elif d > answer:
    print("Down")
else:
    print("정답입니다.")

e = int(input("숫자 입력"))
if e < answer:
    print("Up!")
elif e > answer:
    print("Down")
else:
    print("정답입니다.")

a = int(input("숫자 입력"))
if a < answer:
    print("Up!")
elif a > answer:
    print("Down")
else:
    print("정답입니다.")

#4. 평균 점수
#kor = int(input("국어 점수:"))
#math = int(input("수학 점수:"))
#eng = int(input("영어 점수:"))
#avg = (kor + math + eng) /3

#if avg > 90:
    #print("A")
#elif avg >80:
   # print("B")
#elif avg > 70:
    #print("C")
#else:
   # print("F")

#5. 음료 판매 시스템
#menu = ['1.아메리카노 - 3000원', '2.레몬에이드 - 4000원', '3.카페라떼 - 3500원']
#list = int(input("음료 번호(1~3번, 투입금액:"))

#if list == menu[0]:
    #print(f"음료는 {menu[0]이고, 잔액은 3000원 - }")


#쌤풀이
drinkings = int(input("1.아메리카노[3000] 2.레몬에이드[4000] 3.카페라떼[3500] 선택하세요:"))
money = int(input("금액을 투입하세요."))

#아메리카노 고른 상태
if drinkings == 1:
    if 3000 > money:
        print("금액이 부족합니다.")
    else:
        print("아메리카노 한잔과 잔돈 {money - 3000} 입니다.")

elif drinkings ==2:
    if 4000 > money:
        print("금액이 부족합니다.")
    else:
        print("레몬에이드 한 잔과 잔돈은 {money - 4000} 입니다.")


elif drinkings ==3:
    if 3500> money:
        print("금액이 부족합니다.")
    else:
        print("카페라떼 한 잔과 잔돈은 {money - 3500} 입니다.")

else:
    print("번호를 잘못 입력하였습니다.")


# 두번째 방법
menu = ['아메리카노', '레몬에이드', '카페라떼']
price = [3000, 4000, 3500]
drinkings = int(input("1.아메리카노[3000] 2.레몬에이드[4000] 3.카페라떼[3500] 선택하세요:")) -1
money = int(input("금액을 투입하세요."))

if price[drinkings] > money:
    print("투입 금액이 부족합니다.")
else:
    print("선택하신 메뉴는 {menu[drinkings]} 잔돈: {money - price[drinkings]}")


