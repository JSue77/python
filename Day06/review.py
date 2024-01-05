#영화 티켓 가격 계산기
#movie = {
   # 1: {'name': '일반영화',
    #    'price': 10000,
   # },
    #2: {'name': '3D영화',
     #   'price': 12000,
     #   },
    #3: {'name': '4DX영화',
     #   'price': 15000,
     #   },
#}

#seat = {
   # 1: {'label': '일반석',
        #'price': 0,
       # },
    #2: {'label': '프리미엄석',
      #  'price': 3000,
       # },
    #3: {'label': 'VIP석',
       # 'price': 5000,
       # },
#}

#snack = {
    #1: {'type': '기본콤보',
      #  'prcie': 3000,
    #},
   # 2: {'type': '프리미엄 콤보',
      #  'prcie': 5000,
    #},
   # 3: {'type': 'VIP 콤보',
        #'prcie': 8000,
       # },
#}

#user = int(input(f"영화 종류(1~3번): 좌석등급(1~3번): 간식 종류(1~3번):를 골라주세요."))
#total = {movie['price'] + seat['price'] + snack['price']}
#age = int(input("나이를 입력하세요"))

#if age <= 12:
    #print(f"금액은 total * 0.5 입니다.")
#elif 13 < age and age >= 18:
    #print(f"금액은 total * 0.8 입니다.")
#elif age >= 65:
   # print(f"금액은 total * 0.7 입니다.")
#else:
    #print(f"금액은 total 입니다.")

#print(f"귀하의 영화는 {movie['name']}, 좌석은 {seat['label']}, 간식은 {snack['type']}입니다.")

#쌤풀이
#dict를 잘 활용하면 if문을 많이 안써도 됨
movie  = {
    1: 10000,
    2: 12000,
    3: 15000,
}
seats  = {
    1: 0,
    2: 3000,
    3: 5000,
}

snack  = {
    1: 3000,
    2: 5000,
    3: 8000,
}

movie_choice = int(input("영화 종류 [1.일반 2. 3D 3. 4D]:"))
seat_choice = int(input("좌석 종류 [1.일반 2. 프리미엄 3.VIP]:"))
snack_choice = int(input("간식 종류 [1.일반 2. 프리미엄 3.VIP]:"))
age = int(input("나이를 입력하세요:"))

if age <= 12: #50%
    print(f"총 금액은 {(movie[movie_choice] + seats[seat_choice] + snack[snack_choice]) * 0.5}")
elif 13 <= age and age <= 18: #20%
    print(f"총 금액은 {(movie[movie_choice] + seats[seat_choice] + snack[snack_choice]) * 0.8}")
elif 65 <= ang:#30%
    print(f"총 금액은 {(movie[movie_choice] + seats[seat_choice] + snack[snack_choice]) * 0.7}")
else:
    print(f"총 금액은 {(movie[movie_choice] + seats[seat_choice] + snack[snack_choice]) * 1}")
          
