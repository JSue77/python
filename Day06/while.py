#while

#1.
#a = 1 #무한루프
#while a < 10:
   # print(a)
   # a += 1 #끝내는 방법

#2.
#while True:
    #num = int(input("숫자를 입력(0은 종료):"))
    #if num == 0:
        #break
    #print('웨딩 사진 잘 찍으세요~')

#3. up & down game 만들기
# -1) 0~100 랜덤한 숫자 뽑기
# 2) 유저가 맞출 때까지 게임 진행
# 1] 유저 > 랜덤: down 출력 후 다시 맞추기
# 2] 유저 < 랜덤: up 출력 후 다시 맞추기
# 3] 유저 == 랜덤: 정답입니다!
# 때려맞춘 숫자 출력

#try_num = 0
#import random
#answer = random.randint(1,101) #1~101
#print(answer)
#while True:
#    user_number = int(input("정답 맞추기:"))
#    if user_number > answer:
#        print("down")
#        try_num += 1
#    elif user_number < answer:
#        print("up")
#        try_num +=1
#    else:
#        print("정답입니다~!")
 #       break

#유저가 0을 입력할때까지 여러 정수를 입력받고,
#정수의 총 합을 구하는 프로그램

#while True:
   # user = int(input"정수 입력:")
    #if user == 0
    #break

   # sum = 0
    #sum = sum += user
   # print(sum)

#쌤풀이

#sum = 0
#while True:
  #  user_number = int(input("숫자 입력:"))
   # if user_number == 0:
      #  print(sum)
      #  break
    #sum += user_number

#일본 여행 todolist
#1. 먹고 싶은 리스트
# -1) 먹고 싶은 것은:
#2. 가고 싶은 리스트
# -2) 가고 싶은 곳은:
#3. 리스트 보기
# -1) 먹고 싶은 리스트:[], 가고 싶은 리스트:[]
#4. 종료

#while True:
    #if a == 1:
     #   print(input(f"먹고 싶은 것은?"))
   # elif b == 2:
     #   print(input(f"가고 싶은 곳은?"))
    #elif c == 3:
      #  print(f"먹고 싶은 리스트: [a], 가고싶은 리스트:[b]")
    #elif d == 4:
       # break
   # else:
        #print("종료")

#while True:
  # code = int(input("""1.먹고 싶은 리스트 추가 2. 가고 싶은 리스트 추가 3. 리스트 보기 4. 종료 """))
   #foodList = []
   #placeList = []

   #if code == 1:
    #  food = input("뭐 드시고 싶으세요:")
    #  foodList.append(food)

   #elif code == 2:
    #   place = input("어디 가고 싶으세요:")
     #  placeList.append(place)

   #elif code == 3:
      # print(f"먹고 싶은 리스트: {foodList}")
      # print(f"가고 싶은 리스트:{placeList}")

   #elif code == 4:
     #  print("프로그램 종료!")
     #  break

#더하기 빼기 프로그램
#1. 더하기
#-1) 첫 번째:
#-2) 두 번째:
#-3) 더한 값은 ~입니다.
#2. 빼기
#3. 종료

#while True:
    #if code == 1:
       # int(input("첫 번째 숫자:"))
       # int(input("두 번째 숫자:"))
   # elif code == 2:

while True:
    code = int(input("1.더하기 2.빼기 3.종료"))
    if code == 1:
        one = int(input("첫 번째:"))
        two = int(input("두 번쨰:"))
        print(one + two)

    elif code == 2:
        one = int(input("첫 번째:"))
        two = int(input("두 번쨰:"))
        print(one - two)
    elif code == 3:
        print("프로그램 종료")
        break
    else:
        print("숫자 오류 재입력")