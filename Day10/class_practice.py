#학생관리시스템 학생 클래스 만들기 (이름, 나이, 학년, 전공,듣고 있는 수업)

#class Student:
#    def __init__(self, a,b,c,d):
#        self.name = a
#        self.grade = b
#        self.major = c
#        self.courses = []

#    def enroll_courses(self,course):
#        if len(self.courses) >= 5:
#        self.courses.append(course)
#        else:
#        print('수업 듣는 과목이 너무 많습니다.')

#    def cancel_course(self):
#        if len(self.courses) == 0:
#            print('과목이 없습니다. 뺄 수가 없어요')
 #       else:
 #           for index, item in enumerate(self.courses):
  #              print(f"{index}.{item}")
   #         removeTarget = int(input("빼고 싶은 과목의 번호를 선택:"))
    #        del self.courses[removeTarget]

#    def infomate(self):
 #       print(f"학생 이름: {self.name} 학년 {self.grade} 전공 {self.mager}")
  #      print("학생의 수업 리스트")
   #     for i in self.courses:
    #        print(f"{i}")

#kim = Student(a:'김주영', b:'3', c:'철학과')
#kim.enroll_courses('철학의 이해')
#kim.enroll_coursee('철학의 쓸모')
#kim.infomate()

#class Circle:
#    def __init__(self, x):
#        self.diameter = x
#    def area(self):
#        print(f"넓이: {x*x}, 둘레 {x*3.14}")

class Circle:
    def __init__(self,x):
        self.radius = x
    def width(self):
        print(f"원의 넓이는 {self.radius **2 * 3.14}")
    def round(self):
        print(f"원의 둘레는 {self.radius *2 * 3.14}")

a = Circle(5)
a.width()
a.round()
b = Circle(7)
b.width()
b.round()
