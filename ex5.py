s = input().split('-')
move_1 = s[0]
move_2 = s[1]
if ((abs(ord(move_1[0]) - ord(move_2[0])) == 2 and abs(int(move_1[1]) - int(move_2[1])) == 1)
    or (abs(ord(move_1[0]) - ord(move_2[0])) == 1 and abs(int(move_1[1]) - int(move_2[1])) == 2)):
    print('верно')
else:
    print('ошибка')
