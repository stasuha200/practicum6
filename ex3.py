s = list(map(int, input().split('x')))
k = int(input())
n = s[0]
m = s[1]
if k < n * m and (k % n == 0 or k % m == 0):
    print('Успешно')
else:
    print('Неосуществимо')
