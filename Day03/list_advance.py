#list 함수
#맛보기
#menu = ['🍔', '🍟', '🍗', '🥗']
#menu.append('🍿')
#print(menu)

#리스트 연산자
#1. 덧셈 연산자(+)
#listone = [1,2,3] + ['a','b','c']
#print(listone)

#2. 곱셈 연산자(*)
#list_two = ['넷플','티빙','유튜브'] * 2
#print(list_two)

#3. 인덱싱
#ist_three = ['신서유기','강식당','지구오락실']
#print(list_three[2]) #지구오락실

#4. 슬라이싱
#list_four = ['메가커피','벤티','투썸','스벅']
#print(list_four[1:3]) #벤티& 투썸

#5. in, not in
#burger = ['버거킹', '롯데리아', '노브랜드','맥도날드']
#result = '롯데리아' in burger
#result1 = '롯데리아' not in burger
#print(result)
#print(result1)

#리스트 함수
#1. append() 항목 추가 [맨뒤에]
#coffee = ['아아', '라떼', '바닐라']
#coffee.append('믹스커피')
#print(coffee)

#2. extend() + 리스트 추가  연산자와 같음
#ice_coffee = ['아이스 아메리카노', '아이스라떼']
#coffee.extend(ice_coffee)
#print(coffee)

#3. insert(어디에, 무엇을) 도중에 삽입
#coffee.insert(1,'디카페인')
#print(coffee)

#4. remove(무엇을) 삭제
#coffee.remove('바닐라')
#print(coffee)

#5. pop(몇번째) 안쓰면 맨뒤에 삭제
#coffee.pop(2)
#print(coffee)

#6. clear 올삭제
#7. index(무엇을) 몇번째 위치?
#result = coffee.index('라떼')
#print(result)

#8. count(무엇을) 몇 개 있는지
#9. sort() 오름차순 정렬
#coffee.sort()
#print(coffee)

#coffee.sort(reverse=True) #내림차순
#print(coffee)


#mini quiz : 뉴스 기자를 가져오시고, 뉴스 기사를 리스트화 해주시고, 오름차순으로 단어 리스트를 만들어주세요.
#news = """‘목디스크’는 흔히 ‘퇴행성 목디스크’와 혼용되기도 하는데 이를 구분해야 한다.
#먼저, ‘퇴행성 목디스크’는 ‘목디스크’의 전단계인 경우가 많다. 퇴행성 목디스크는 경추 관절 사이에 있는 추간판의 퇴행성변화로 인해
#수분함량과 탄력성이 감소하면서 외상에 취약한 상태가 되는 질환을 말한다.
#이때 특별한 증상이 없을 수도 있으나 대부분 경추 후방 근육의 긴장과 관련돼 뒷목의 뻣뻣함 및 통증, 후두부의 두통 등과 동반된다."""

#newsList = news.split()
#newsList.sort()
#print(newsList)

#마무리 퀴즈
#1. 운동순서 저장 리스트
#운동 루틴을 총 5개를 입력을 받고
#오름차순으로 표현하는 프로그램
#2. 뉴스를 가져와서 유저가 찾는 단어를 몇 개인지 출력하는 프로그램

#1. 운동순서
ex1 = input("첫번째 운동:")
ex2 = input("두번째 운동:")
ex3 = input("세번째 운동:")
ex4 = input("네번째 운동:")
ex5 = input("다섯번째 운동:")

routine = list['ex1','ex2','ex3','ex4','ex5']
routine.sort()
print(routine)














