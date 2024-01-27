#영어가 싫어요
#num = 12345 #데이터 타입 바꾸기

target = "onetwothreefourfivesixseveneightnine"
#target.replace("zero","0")
#target.replace("one","1")
#...
#target.replace("nine","9")

#어떻게 한 줄로 바꿀까

numList = ['zero','one', 'two','three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
#for i in numList:
#   if i in target:
#        target.replace(i, "1")

for index, item in enumerate(numList):
    if item in target:
        target = target.replace(item, str(index))
print(target)











