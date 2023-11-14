#print("Hello World!")

#Begin1. Дана сторона квадрата a. Найти его периметр P = 4*a.
##a = 8
##p = 4 * a
##print('P = ', p)

#Begin2. Дана сторона квадрата a. Найти его площадь S = a * a
##print('Введите целое число - сторону квадрата ', end = '')
##a = int(input())
##S = a * a
##print('S = ', S)

#Begin3. Даны стороны прямоугольника a и b. Найти его площадь S = a*b и периметр P = 2*(a + b)
##print('Введите целое число - сторону прямоугольника ', end = '')
##a = int(input())
##b = int(input())
##S = a * b
##P = 2*(a + b)
##print('S = ', S)
##print('P = ', P)

#Begin4. Дан диаметр окружности d. Найти ее длину L = π*d. В качестве значения π использовать 3.14.
##print('Введите целое число - диаметр окружности ', end = '')
##d = int(input())
##L = 3.14 * d
##print('L = ', L)

#Begin5.Дана длина ребра куба a. Найти объем куба V = a*a*a и площадь его поверхности S = 6*(a*a)
##print('Введите целое число')
##a = int(input())
##V = a*a*a
##S = 6*(a*a)
##print('V = ', V)
##print('S = ', S)

#Begin6. Даны длины ребер a, b, c прямоугольного параллелепипеда. Найти его объем V = a*b*c и площадь поверхности S = 2*(a*b + b*c + a*c).
##print('Введите целое число')
##a = int(input())
##b = int(input())
##c = int(input())
##V = a*b*c
##S = 2*(a*b + b*c + a*c)
##print('V = ', V)
##print('S = ', S)

#Begin7.Найти длину окружности L и площадь круга S заданного радиуса R:Найти длину окружности L и площадь круга S заданного радиуса R:L = 2*3.14*R, S = 3.14*R*R
##print('Введите целое число')
##R = int(input())
##L = 2*3.14*R
##S = 3.14*R**2
##print('L = ', L)
##print('S = ', S)

#Begin8. Даны два числа a и b. Найти их среднее арифметическое: (a + b)/2
##print('Введите целое число')
##a = int(input())
##b = int(input())
##N = (a + b)/2
##print('N = ', N)

#Begin9. Даны два неотрицательных числа a и b. Найти их среднее геометрическое, то есть квадратный корень из их произведения: √a·b
##print('Введите целое число')
##import math
##a = int(input())
##b = int(input())
##x = math.sqrt(a*b)
##print('x = ', x)

#Begin10.Даны два ненулевых числа. Найти сумму, разность, произведение и частное их квадратов
##print('Введите целое число')
##a = int(input())
##b = int(input())
##d = (a*a)+(b*b)
##c = (a*a)-(b*b)
##m = (a*a)*(b*b)
##n = (a*a)/(b*b)
##print('d = ', d)
##print('c = ', c)
##print('m = ', m)
##print('n = ', n)

#Begin11. Даны два ненулевых числа. Найти сумму, разность, произведение и частное их модулей
##print('Введите целое число')
import math
##a = int(input())
##b = int(input())
##math.fabs(a) 
##d = math.fabs(a)+math.fabs(b)
##c = math.fabs(a)-math.fabs(b)
##m = math.fabs(a)*math.fabs(b)
##n = math.fabs(a)/math.fabs(b)
##print('d = ', d)
##print('c = ', c)
##print('m = ', m)
##print('n = ', n)

#Begin18. Даны три точки A, B, C на числовой оси. Точка C расположена между точками A и B. Найти произведение длин отрезков AC и BC.
##print('Введите целое число')
##import math
##A = int(input())
##B = int(input())
##C = int(input())
##D = math.fabs(A-C)*math.fabs(B-C)
##print('D = ', D)

##Begin19. Даны координаты двух противоположных вершин прямоугольника:(x1, y1), (x2, y2). Стороны прямоугольника параллельны осям координат.
##Найти периметр и площадь данного прямоугольника.
##print('Введите целое число')
##x1 = int(input())
##y1 = int(input())
##x2 = int(input())
##y2 = int(input())
##S = math.fabs(y2-y1)*math.fabs(x2-x1)
##P = 2*(math.fabs(y2-y1)+math.fabs(x2-x1))
##print('P = ', P)
##print('S = ', S)

##Begin20.Найти расстояние между двумя точками с заданными координатами (x1, y1) и (x2, y2) на плоскости. Расстояние вычисляется по формуле √(x2 − x1)*(x2 − x1)+(y2 − y1)*(y2 − y1).
##print('Введите целое число')
##x1 = int(input())
##y1 = int(input())
##x2 = int(input())
##y2 = int(input())
##x = math.sqrt(math.fabs(x1-x2)**2 + math.fabs(y1-y2)**2)
##print('x = ', x)

##Begin21. Даны координаты трех вершин треугольника: (x1, y1), (x2, y2), (x3, y3).Найти его периметр и площадь, используя формулу для расстояния между двумя точками на плоскости (см. задание Begin20). Для нахождения площади треугольника со сторонами a, b, c использовать формулу Герона: S = √p*(p − a)*(p − b)*(p − c),где p = (a + b + c)/2 — полупериметр.
##print('Введите целое число')
##x1 = int(input())
##y1 = int(input())
##x2 = int(input())
##y2 = int(input())
##x3 = int(input())
##y3 = int(input())
##a = math.sqrt(math.fabs(x1-x2)**2 + math.fabs(y1-y2)**2)
##b = math.sqrt(math.fabs(x2-x3)**2 + math.fabs(y2-y3)**2)
##c = math.sqrt(math.fabs(x3-x1)**2 + math.fabs(y3-y1)**2)
##S = math.sqrt(p*(p − a)*(p − b)*(p − c))
##p = (a + b + c)/2
##print('a = ', a)
##print('b = ', b)
##print('c = ', c)
##print('S = ', S)
















