'''
Try hello world 파이썬 197
'''
ko = '가나다'
en = 'ABC'

print('가나다-ABC')
print(ko, '-', en)
print('{}-{}'.format(ko, en))

ens = ['a','b','c']

for en in ens :
    print(en)

for cnt in range(len(ens)):
    print('{}:{}'.format(cnt+1, ens[cnt]))

for cnt, value in enumerate(ens):
    print('{}:{}'.format(cnt,value))

import test01_fun01

choice = test01_fun01.get_random(ens)
print(choice)

import datetime
print(datetime.date.today())

import random
random.shuffle(ens)
print(ens)