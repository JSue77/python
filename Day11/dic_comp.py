#iphoneList = ['iphone13', 'iphone13max', 'iphone14', 'iphone14plus', 'iphone15']
#iphonePriceList = [1000000, 1200000, 1300000, 1350000, 1500000]

#zip zipper
#zip(iphoneList, iphonePriceList)
#print(list(zip(iphoneList, iphonePriceList)))


#for i in zip(iphoneList, iphonePriceList)
#print([{'아이폰': phone, '가격': price} for phone,price in zip(iphoneList, iphonePriceList)])

#alpha = ['a','b','c','d','e']
#numbers = [1,2,3,4,5]
#zip(alpha,numbers)
#print(list(zip(alpha,numbers)))

#쌤
#print([{'알파벳': a, '숫자':n} for a,n in zip(alpha, numbers)])


text = "apple banana apple strawberry banana"
# [{"단어": "apple", "글자수":5},{"단어": "banana", "글자수":6]

#text_list = [text]
#lenth = len(list(text))
#zip(text_list, lenth)

#[{"단어":'apple',"글자수":lenth(0)}]

#쌤
wordList = text.split()
wordLenList = list(map(lambda x: len(x), wordList))

print([{'단어': word, '글자수':length} for word, length in zip(wordList,wordLenList)])


