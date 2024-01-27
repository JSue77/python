#library
#import random #랜덤을 쓸게 (내부 라이브러리)
#외부 library #도구 모음 (외부 라이브러리)
import qrcode

url = 'https://medicine.yonsei.ac.kr/medicine/index.do'
qrcode_img = qrcode.make(url)
qrcode_img.save('yonsei.png')

