# 자료 구조(data_structure) - dict

#coffee = {
    # 'key': 'value'  #키 [정수, 문자] - value [any]
   # 1: '아메리카노',
  #  2: '라떼',
  #  3: '바닐라',
#}

#nation = {
   # '한국': '서울',
   # '일본': '도쿄',
   # '중국': '베이징',
   # '프랑스': '파리',
#}

#japan_travel = {
   # 'city': ['후쿠오카', '오사카', '벳푸', '나가사키', '히로시마'],
   # 'food': ['라멘', '초밥', '텐동'],
  #  'hotel': [
   #     {'이름': '퍼스트스테이', '가격': 100000, '조식': False},
  #      {'이름': '지니어스호텔', '가격': 120000, '조식': False},
  #  ]
#}

#print(coffee[3])  # 바닐라
#print(nation['일본'])  # 도쿄
#print(japan_travel['city'][0])  # 후쿠오카
#print(japan_travel['hotel'][0]['이름'])  # 퍼스트스테이

# mbti 성향 프로그램
# 유저한테 mbti를 입력 받기
# e - 외향, i - 내향
# s - 현실, n - 직관
# t - 이성, f- 감정
# p - 즉흥, j - 기획
# 당신은 외향적 직관적 이성적 기회적이시군요!

# m = {
# 'energy': ['e:외향', 'i:내향']
# }
# b = {
# 'in1': ['s:현실', 'n:직관']
# }

# m3 = {
# 'in2': ['t:이성', 'f:감정']
# }

# m4 = {
# 'in3': ['p:즉흥', 'j:기획']
# }

# 쌤풀이

# mbti = {
# 'e': '외향적',
# 'i': '내향적',
# 's': '현실적',
# 'n': '직관적',
# 't': '이성적',
# 'f': '감성적',
# 'j': '계획적',
# 'p': '즉흥적',
# }

# a = input("mbti가 어떻게 되시나요?")
# a.lower()
# ENTJ a[0] e a[1] n
# print(f"{mbti[a[0]]} {mbti[a[1]]} {mbti[a[2]]}  {mbti[a[3]]})")
# print(mbti['j']) #계획적

# 6. 영화 티켓 예매 시스템
#ticket = {
    #'movie': ['1.액션영화', '가격:10000'],
    #'movie': ['2.로맨틱코미디', '가격:8000'],
   # 'movie': ['3.공포영화', '가격:9000'],
#}

#age = {
   # '13세 미만': '50% 할인',
    #'60세 이상': '30% 할인',
#}

#a = input(("영화를 선택하세요. 1~3번"))
#b = int(input("나이를 입력하세요."))

#print(f"영화는 {ticket[a[0]]} ")

#쌤풀이
#어떻게 하면 dic화 시킬까

#movie = {
    #1:{
    # 'name: '액션 영화',
    # 'price': 10000,
#},
    #2:{
    # 'name: '로맨틱 코미디',
    # 'price': 8000,
#},
   # 3:{
    # #'name: '공포영화',
     #'price': 9000,
#},
#}
#movie_number = int(input("영화를 고르세요.(1.액션 2.로코 3.공포):"))
#age = int(input("나이를 입력하세요:"))

#if age < 13:
   # print(f"고르신 영화는 {movie[movie_number]['name'] 가격은 {movie[movie_number]['price'] * 0.5}")
#elif age >= 60:
   # print(f"고르신 영화는 {movie[movie_number]['name'] 가격은 {movie[movie_numver]['price'] * 0.3}")
#else:
   # print(f"고르신 영화는 {movie[movie_number]['name'] 가격은 {movie[movie_number]['price']}입니다.")


#7. 버스 요금 계산기
#사용자로부터 버스 노선의 종류를 나타내는 정수와 승객의 나이를 입력받습니다.

#bus = {
   # 1: {
   # 'name': '시내버스',
   # 'price': '1200원',
   # },
   # 2: {
   # 'name': '광역버스',
   # 'price': '2000원',
    #},

   # 3: {
   # 'name': '마을버스',
   # 'price': '1000원',
   # },
#},

#pick = int(input("버스를 골라주세요(1. 시내버스 2. 광역버스 3. 마을버스"))
#age = int(input("나이를 입력해주세요."))

#if age <= 7:
  #  print("무료입니다.")
#elif 8 < age and age >=19:
    #print(f"버스는 {bus[pick]['name']}이고, 가격은 {bus['price'] * 0.3}입니다.")
#elif age >= 60:
   # print(f"무료입니다.")
#else:
   # "잘못 입력했습니다."

#쌤풀이
bus_info = {
    1: {
        'tpye': '시내버스',
        'price': 1200,    },
    2: {
        'type': '광역버스',
        'price': 2000,
    },
    3: {
        'type': '마을버스',
        'price': 1000,
    },
}

bus = int(input("버스 종료 입력: 1.시내 2. 광역 3. 마을)"))
age = int(input("나이를 입력하세요"))

if age <=7 or 65 <= age:
    print("무료입니다.")
elif 8 <= age and age <=19:
    print(f"버스: {bus_info[bus]['type']} 가격: {bus_info[bus]['price'] * 0.7}")
else:
    print(f"버스: {bus_info[bus]['type']} 가격: {bus_info[bus]['price']}")






