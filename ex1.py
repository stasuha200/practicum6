s = list(map(int, input().split('x')))
n = s[0]
m = s[1]
if n ** 2 + m ** 2 <= (6.5 * 2) ** 2:
    print('да')
else:
    print('нет')