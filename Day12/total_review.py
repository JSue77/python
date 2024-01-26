# 2 + 3 = 5
#인간: 연산(뇌) + 기억(뇌)
#컴퓨터: 연산(CPU) + 기억(RAM)

#변수: 메모리에 값을 저장하는 공간
#변수 네이밍
#문법: 숫자로 시작이 안되고, 특수문자_만 가능하고, 대소문자 구분하고, if, elif, class 예약어 안됨

#연산자
#사칙연산(+-*/%//**), 대입연산(=,+=, -+, *=,...),
#비교연산(<, >, >=, <=, !=, ==), 논리연산(and, or, not), in 연산자(in)

#제어문
#조건문: if, elif, else
#if 조건문, elif 조건문
#반복문 for, while
#for - range, 문자열, 리스트
#while - 무한루프
#break, continue 문 - 반복문을 제어 했음

#컴프리헨션(리스트, 딕셔너리 단축화)
#[i for i in range/ str/ list] - 기본형
#[i for i in range/ str/ list if i % 2 == 0 ] - filter형
#[i if i % 2 == 0 for i in range/str/list] - map형
#['🍕' if i % 2 == 0 else '🍔' for i in range/str/list] - map형 짝수이면 '🍕' 아니면 '🍔'로

#zip화
#coffeeList = ['a','b','c'], priceList = [1000,2000,3000]
#zip(coffeeList, priceList) #('a',1000), ('b',2000), ('c',3000)
#[{'이름': c, '가격': p} for c,p in zip(coffeeList, priceList)]


#함수, 람다함수, 콜백함수, 3대장 내장함수

#일반 함수
#def name(arg):
#...
#return...

#람다 함수
#lamda x: x

#콜백 함수
#함수의 매개변수에 함수를 넣어줌
#funtion some(x[콜백함수])

#map(변형), filter(필터), reduce(누적)

#내장함수
#print, input, str, int, float, list, dict, set
#len, max, nin, zip, range, sum


#문자열의 함수 - alg 퀴즈 많이 풀기
#리스트의 함수 - alg 퀴즈 많이 풀기
#"asd".

#클래스와 상속
#클래스: 멤버 변수 + 멤버 함수
#class BankAccount:
#    def __init__(): 멤버 변수 초기화 및 보관함
#    def withdraw, deposit, check: 멤버 함수[멤버 변수 조작]

#상속: 부모 클래스에서 상속 받고 추가로 멤버 변수 or 변수함수를 추가
#코드가 짧아지고, 유지보수에 유리























