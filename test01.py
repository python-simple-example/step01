'''
Try hello world 파이썬 p.0 ~ p.187
'''
ko = '가나다'
en = 'ABC'

print('가나다-ABC')
print(ko, '-', en)
print('{}-{}'.format(ko, en))

ens = ['a','b','c']
ens2 = ['c', 'd', 6]

tot_ens = ens + ens2
print(tot_ens)

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

ens.append('d')
print(ens)

print(ens.pop(len(ens)-1))
print(ens)

