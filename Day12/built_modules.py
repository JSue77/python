import math
print(math.pi) #파이 3.14

import datetime
print(datetime.datetime.now()) #2024-01-27 00:25:02.963325

import os #운영체제
folder_name = '메가스터디 짱짱맨'

if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print('완료')
