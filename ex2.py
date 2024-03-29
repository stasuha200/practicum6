s = list(map(float, input().split('x')))
v = list(map(float, input().split('x')))
a = s[0]
b = s[1]
c = v[0]
d = v[1]
e = v[2]
if (a * b >= c * d) or (a * b >= c * e) or (a * b >= e * d):
    print('Да')
else:
    print('Нет')
