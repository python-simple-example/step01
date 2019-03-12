'''
Try hello world 파이썬 p.188 ~ p.210
'''

dic = {'A':1, 'B':2, 'C':3}

print(dic)
print(dic['A'])

dic['A'] = '일'

print(dic)
print(dic['A'])

del(dic['A'])
print(dic)

print(dic.pop('B'))
print(dic)

dic = {'A':1, 'B':2, 'C':3}

for d in dic.keys():
    print('d:{} dic:{}'.format(d, dic[d]))

for key, value in dic.items():
    print('key:{} value:{}'.format(key, value))

print('A' in dic.keys())
print('3' in dic.values())
print(3 in dic.values())

dic2 = {'C':3, 'D':4}

dic.update(dic2)
print(dic)