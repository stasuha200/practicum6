a = input()
if 'a' in a:
    a = a.replace('a', '1')
elif 'b' in a:
    a = a.replace('b', '2')
elif 'c' in a:
    a = a.replace('c', '3')
elif 'd' in a:
    a = a.replace('d', '4')
elif 'e' in a:
    a = a.replace('e', '5')
elif 'f' in a:
    a = a.replace('f', '6')
elif 'g' in a:
    a = a.replace('g', '7')
elif 'h' in a:
    a = a.replace('h', '8')
if int(a[0]) % 2 == int(a[1]) % 2:
    print('Черный')
else:
    print('Белый')
