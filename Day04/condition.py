# 1.조건문
# if문

# toeic = int(input("토익 점수 입력:"))
# if toeic > 900: #비교연산자를 통해 조건이 부합하면
# print("축하합니다. 장려금이 나옵니다.")
# print("끝")

# 중첩 if문
# if toeic > 800:
# print("축하합니다.")
# if toeic > 900:
# print("장려금이 나옵니다!")

# elif, else 문
# shopping = int(input("구매 금액:"))

# if 50000 > shopping and shopping >= 30000:
# print("주차권 1시간!")
# elif 70000 > shopping and shopping >= 50000: #이게 아니면
# print("주차권 2시간!")
# elif 100000 > shopping and shopping >=70000:
# print("주차권 3시간!")
# elif shopping >=100000:
# print("주자권 종일")
# else:
# print("주차권 없음")

# 수학점수를 입력 받고
# 100~90: A
# 90~80: B
# 80~70: C
# 과락입니다.

# score = int(input("수학 점수:"))

# if 100 > score and score >= 90:
# print("A")
# elif 90 > score and score >=80:
# print("B")
# elif 80 > score and score >=70:
# print("C")
# else:
# print("과락입니다.")


# score1 = int(input("수학 점수:"))
# score2 = int(input("영어 점수:"))
# score3 = int(input("국어 점수:"))
# total = (score1 + score2 + score3)/ 3

# if 100 > total and total >= 90:
# print("A")
# elif 90 > total and total >=80:
# print("B")
# elif 80 > total and total >=70:
# print("C")
# else:
# print("과락입니다.")

# 숫자를 입력했을 때 홀수이면 홀수, 짝수이면 짝수
# %, //

# num = int(input("숫자 입력:"))
# print(f"{num % 2 }")  #2 -> 0, 3->1, 4->0, 5->1, 6->0, 7->1

# if num % 2 == 0:
# print("짝수 입니다.")
# else:
# print("홀수 입니다.")

# 양의 짝수, 양의 홀수, 0, 음의 짝수, 음의 홀수를 나타내는 프로그램
#num = int(input("숫자 입력"))

#if num > 0:  # 양수
   #if num % 2 == 0:
       # print("양의 짝수")
    #else:
       # print("양의 홀수")
#elif num == 0:
    #print("0")
#else:
    #if num % 2 == 0:
       # print("음의 짝수")
    #else:
        #print("음의 홀수")

# elif num == 0:
# else


