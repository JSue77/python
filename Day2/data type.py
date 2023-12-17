#print() 출력
#inpur() 입력
#int() 정수화
#str() 문자화
#tpye() 무슨 타입인지 알려줌

#print(type(123))
#print(type("123"))
#print(type(1.23))

#print(5/2) #실수까지 표현
#print(5//2) #정수(몫)
#print(5%2) #나머지


age = int(input("당신의 나이는 몇 살입니까"))
print(f"만나이는 {2023-age +1}")

a = int(4)
b = int(7)
c = int(3)
print(f"세 숫자의의 평균은 {(a+b+c)//3}")

won = int(input("금액이 얼마입니까"))
print(f"엔화로는 {won * 1300}원입니다.")

km = int(input("거리는 얼마입니까"))
print(f"거리는 {km*0.621372}mile입니다.")

C = int(input("섭씨 온도는 몇 입니까"))
print(f"{C*59+32}")

height = int(input("키"))
weight = int(input("몸무게"))
print(f"{weight/(height**2)}")

