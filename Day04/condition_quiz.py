#조건문 챌린지!
#1. 알파벳 탐지기

#str = input("문자 한개를 입력해주세요.")
#is = isalpha(str)
#if str == is
   # print("알파벳입니다!.")
#else:
    #print("알파벳이 아니에요.")

#text = input("문자 입력:")
#if text.isalpha():
    #print("알파벳입니다.")
#else:
    #print("알파벳이 아니올시다.")

#**쌤 풀이

#text = input("문자 입력:")
#if text.isupper():
   #print(f"{text.lower}")
#else:
   # print(f"{text.upper()}")

#비밀번호 체크
#비밀번호를 입력하세요:
#1. 특수문자가 포함이 되어야 합니다.
#2. 첫번째 글자가 대문자여야 합니다.
#3. 비밀번호의 길이가 8글자 이상이어야 합니다.
#4. 비밀번호가 설정이 되었습니다.

#password = input("비밀번호를 입력하세요.:")
#if password == password.isalnum():
    #elif password.isupper():
    #elif password.len() >= 8 :
        #print("비밀번호가 설정되었습니다.")

#isalum 숫자 and 알파벳이 있으면 True
#if not password.isalnum():
    #print("특수문자를 넣으셔야 합니다!")
#elif not password[0].isupper():
    #print("첫 글자는 대문자여야 합니다.")
#elif len(password) < 8:
    #print("비밀번호가 8글자 이상이어야 합니다.")
#else:
    #print("비밀번호가 올바르게 설정되었습니다.🎆")

#2. 홀수? 짝수? 확인해보세요.
#num = int(input("숫자 입력:"))

#if num % 2 == 0
   #print("짝수입니다.")
#else:
   #print("홀수입니다.")


#6. 각도의 비밀을 밝혀라
#예각이면 1, 직각이면 2, 둔각이면 3, 평각이면 4로 분류
#angle = int(input("각도를 입력하세요.:"))
#if 0 < angle >90:
    #print("예각")
#elif angle == 90:
    #print("직각")
#elif 90 < angle >180:
    #print("둔각")
#else:
    #print("평각")

#쌤
if 0 < angle > 90:
    print("예각")
elif angle ==90:
    print("직각")
elif 90 < angle < 180:
    print("둔각")
elif angle == 180:
    print("평각")
else:
    print("잘못 입력하였습니다.")
