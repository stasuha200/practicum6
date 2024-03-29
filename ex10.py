x_1 = int(input())
y_1 = int(input())
x_2 = int(input())
y_2 = int(input())
x_3 = int(input())
y_3 = int(input())
x_4 = int(input())
y_4 = int(input())
xc1 = (x_1 + x_2) / 2
xc2 = (x_3 + x_4) / 2
yc1 = (y_1 + y_2) / 2
yc2 = (y_3 + y_4) / 2
length1 = x_1 - x_2
length2 = x_3 - x_4
width1 = y_1 - y_2
width2 = y_3 - y_4
if (length1 + length2) / 2 < abs(xc1 - xc2):
    print('Прямоугольники лежат вне друг друга, не касаясь')
elif ((length1 + length2) / 2 == abs(xc1 - xc2) and (width1 + width2) / 2 <= abs(yc1 - yc2)) or ((length1 + length2) / 2 <= abs(xc1 - xc2) and (width1 + width2) / 2 == abs(yc1 - yc2)):
    print('Прямоугольники имеют касание')
elif