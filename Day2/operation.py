#비교 연산자
#비교 연산자의 결과는 Bool tpye이다.

# 초과, 미만 >, <
print(5 > 1)
print(3 >=3)
# 이상, 이하 >=, <=

#같다(same) ==
#a=1
print(3 == 1)
print(3 == 3)

#다르다 !=
print(3 != 100)
print(3 != 3)

#논리 연산자
# and [모든 조건이 True 이어야만 True]
print(3 > 1 and 5 < 10) #True
print(3 != 5 and 3 == 3)

#or [하나라도 조건이 True이면 True]
print(1 > 2 or 2 < 3)

#not  boolean type의 반대로
a = (3 > 1) and (5 > 1)
print(a)
print(not a)



#우선순위 연산자
#일차 함수 퀴즈
# y = x*a + b

a = int(input("a:"))
b = int(input("b:"))
x = int(input("x:"))
print(f"y = {x*a+b}")

