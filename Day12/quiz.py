#숫자 뒤집기
#num = 12345 #데이터 타입 바꾸기

#numStr = str(num) #"12345"
#numList = list(numStr) #['1','2','3','4','5']
#numList.reverse()
#numIntList = list(map(lambda x: int(x), numList))
#print(numIntList)


phoneNumber = "01033334444"
passwordNumber = ""
for index, item in enumerate(phoneNumber):
    if len(phoneNumber) - index > 4:
        passwordNumber += "*"
    else:
        passwordNumber += item
print(passwordNumber)
