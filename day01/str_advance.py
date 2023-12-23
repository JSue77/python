
#문자열 연산
#1) 연결

#a = '123'
#b = '123'
#c = a + b #123123

#2) 반복
#d = "mega"
#print(d*3)

#3) 인덱싱(색인)
#coffee = "americano"
#print(coffee[0]) #a가 나옴
#print(coffee[-1])

#4) 슬라이싱
#test = "python"
#print(test[1:3]) #012


#문자열 함수
#1. 대문화자, 소문자화
#a = 'mega'
#b = a.upper()
#print(a)
#print(b)

#upper_mega = mega.upper() #대문자화
#lower_mega = mega.lower() #소문자화

#2. all 대문자 입니까 all 소문자입니까
#mega = 'megastudy'
#isMegaAllLower = mega.islower()
#isMegaALLUpper = mega.isupper()


#3. 공백제거
#merriage = " 오늘 결혼식 추카 "
#newMarriage = merriage.strip()
#print(newMarriage)

#4. split 찢다 -> 리스트
#con = "오늘 결혼 축하해!"
#test = con.split()
#print(test) #공백 기준으로 찍어줌

#con = "오늘! 결혼! 축하해!"
#test = con.split("!")
#print(test)


#news = """올해 정부의 고물가와 고금리 장기화에 따른 부담을 줄이기 위해
#마련한 통신비 부담 완화 정책에 따라 이동통신사들을 향한 압박이 점점 커지고 있다."""

#newNews = news.split()
#print(newNews)


#5. replace 대신 넣기
#article = """The UN Security Council (UNSC) has adopted a resolution urging more aid for the Gaza Strip,
#but falling short of a call for an immediate ceasefire between Israel and Hamas.
#The vote followed days of negotiations to avoid a veto by the US, a permanent UNSC member and a key ally of Israel.
#UN chief António Guterres said the "real problem" to delivering aid was Israel's ongoing offensive."""

#newAricle = article.replace("UN", "KR")
#print(newAricle)


#6. find(찾기) rfind(뒤에서 찾기)
#location = article.find("call")
#print(location)

#7. startswith(시작), endwsith() 끝

#8. join(연결) *주의 필요
#menu = ['아아', '라테', '디카페인']
#result= ' 존맛 '.join(menu)
#print(result)

# quiz
# 뉴스기사에서 유저가 입력한 단어를 빈 공백에 넣어서 재구성하는 뉴스를 만드세요.
# 원래 뉴스 -> {꿀잼}-> 꿀잼 꿀잼 꿀잼 ~~

article = """테슬라는 지난해 ‘AI 데이’ 행사에서 첫 휴머노이드 옵티머스(Optimus)를 공개했다. 
기대가 너무 컸던 걸까. 옵티머스는 큰 실망을 안겨줬다. 옵티머스 시제품은 내부 부품을 그대로 드러낸 채 등장했다. 
스스로 걸을 수는 있었지만, 어딘가 엉성했다. 차세대 옵티머스라고 선보인 로봇은 서 있지도 못했다. 
움직이려면 직원의 도움이 필요했다."""

#result_1 = '꿀잼 '.join(article.split())
#print(result_1)

#word = input("넣고 싶은 단어:")
#news = article.replace(' ', ' '+word+' ')
#print(news)


#9. is 시리즈
# isdigit(), isalpha(), isalum()


#10. count 단어 세주기
#a = article.count("AI")
#print(a)




































