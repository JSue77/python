#1.
#ex1 = input("첫 번째 운동:")
#ex2 = input("두 번째 운동:")
#ex3 = input("세 번째 운동:")
#ex4 = input("네 번째 운동:")
#ex5 = input("다섯 번째 운동:")

#list = [ex1, ex2, ex3, ex4, ex5]
#list.sort()
#print(list)

#-> 쌤풀이
#1) 유저에게 input을 다섯번 받기
#2) 띄워쓰기 기준으로 리스트화 시키기

# = input("운동을 입력하세요(띄워쓰기):")
#list_exe = exe.split()
#list_exe.sort()
#print(f"운동순서: {list_exe}")



#2. 뉴스를 가져와서 유저가 찾는 단어가 몇 개인지 출력하는 프로그램
#news = """24일 새벽 세종시의 한 목욕탕에서 여성 입욕객 3명이 감전돼 심정지 상태로 병원으로 옮겨졌으나 2명은 숨졌다.
#세종시와 세종경찰청 등에 따르면 이날 오전 5시 37분께 조치원읍의 한 목욕탕 여탕에서 3명이 비명을 지르며 쓰러지는 것을 탈의실에 있던 다른 여성이 보고 119에 신고했다.
#쓰러진 여성들은 모두 70대인 것으로 전해졌다.
#현장에 출동한 소방 당국은 모두 심정지 상태인 이들을 병원으로 긴급 이송했다.
#하지만 3명 가운데 2명은 숨진 것으로 경찰은 파악했다.
#경찰과 소방 당국, 전기안전공사 등은 욕탕에 들어갔던 이들이 감전된 것으로 보고 정확한 사고 원인을 조사하고 있다."""

#test = news.count('여성')
#print(test)

#word = input("찾고 싶은 단어:")
#found_words_number = news.count(word)
#print(f"찾고 싶은 단어 {word}는 {found_words_number}개 있습니다.")

#3. 이메일 주소 분리하기
#이메일을 입력 받으면 megastudy@naver.com
#mega, naver.com 으로 분리기하기

email = input("이메일 주소:")
email_list = email.split("@")
print(f"이메일 아이디: {email_list[0]}, 이메일 도메인: {email_list[1]}")


#4. 문자열 변신 마법사!
#"마법의 주문을 외워보세요! 문자열을 입력하면 순서가 바뀌고, 알파벳 순서로도 변신할 거예요. 예를 들어 'mega'를 입력하면 'agem'과 'aemg'로 변해요.

#magic = input("무엇이든 써봐:")
#reversed_magic = "".join(reversed(magic))
#print(reversed_magic)

#문자열 > 거꾸로, 오름차순
#word = input("단어 입력:") #mega
#word_list = list(word) #[m,e,g,a]
#word_reverse_list.reverse() #[a,e,g,m]
#reverse_word = ''.join(word_reverse_list) #aegm

#word_sort_list = list(word) #[m,e,ga]
#word_sort_list.sort()  #[a,e,g,m]
#sort_word = ''.join(word_sort_list) #aegm
#print(sort_word) #aemg

