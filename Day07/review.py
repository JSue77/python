# 리스트 요소의 제곱
#문제: 정수 리스트 [1,3,5,7,9]의 각 요소를 제곱하여 새로운 리스트를 만드세요.
#예상 답안: [1,9,25,49,81]

#a = [1,3,5,7,9]
#b = []
#for i in a:
  #  b.append(i**2)
#print(b)

#문자열 길이 변환
#word = ["hello", "world", "python", "programming"]
#words = []
#for i in word:
    #b.append(len(i))
   # b = len(word[0]),len(word[1]),len(word[2]),len(word[3])
#print(words)

#문자열 처리를 위한 리스트1
#첫 글자만 추출하여 새로운 리스트를 만드세요.
#word_list = ["apple", "banana", "cherry", "date"]
#b = []
#for i in word_list:
   # b.append(word_list[0])
#print(b)

#a = ["apple", "banana", "cherry", "date"]
#b = []
#for i in a:
    #b.append(i[0])
#print(b)



#문자열 처리를 위한 리스트2
#["apple", "banana", "cherry", "date"] "a"가 담겨져 있는 단어들만 리스트를 만드세요.
#답안 ['apple', 'banana']

#word_list = ["apple", "banana", "cherry", "date"]
#b = []
#for word in word_list: #apple
   # for spell in word:
       # if spell == 'a':
         #   b.append(word)

#for word in word_list:
        #if 'a' in word:
          #  b.append(word)
#print(a)

#정답풀이
#a = ["icecream", "americano", "latte"]
#b = []
#for i in a:
   # b.append(len(i))

#문자열 처리를 위한 리스트 3
#word_list = ["apple", "banana", "cherry", "date"]
#consonant_word_list = []
#for word in word_list: #apple
#   newWord = ""
#    for spell in word:
#        if not spell in 'aeiou':
#                newWord += spell
#        consonant_word_list.append(newWord)
#print(consonant_word_list)


#일본 여행 투두리스트 프로그램 만들기
#1.사용자가 선택할 수 있는 메뉴를 만드세요.
#2.1)음식 리스트 추가 2)갈 곳 리스트 추가 3)쇼핑 리스트 추가 4)리스트 모두보기 5)종료
#3.각 메뉴 선택에 따라 사용자로부터 관련 정보를 입력 받으세요.

foodList = []
placeList = []
shopList = []

while True:
    code = int(input("1.음식 리스트 추가 2.갈 곳 리스트 추가 3.쇼핑 리스트 추가 4.리스트 모두보기 5.종료"))

    if code == 1:
        food = input("1.음식 리스트 추가:")
        foodList.append(food)

    elif code == 2:
        place = input("2.갈 곳 리스트 추가:")
        placeList.append(place)

    elif code ==3:
        shop = input("3.쇼핑 리스트 추가:")
        shopList.append(shop)

    elif code ==4:
        print(f"1. 음식 리스트: {foodList}")
        print(f"2. 갈곳 리스트: {placeList}")
        print(f"3. 쇼핑 리스트: {shopList}")

    elif code ==5:
        break
        print("5.프로그램 종료")

    else:
        print("잘못 입력하셨습니다.")