#Код, шде если первая переменная больше второй, то в третью перемнную присваиваем разницу первой и второй; если вторая переменная больше первой - их сумму; если не выполняется ни одно условие - значение первой переменной

var1 = int(input("Введите первое число отличное от нуля: "))
var2 = int(input("Введите второе число отличное от нуля: "))

if var1>var2:
   var3 = var1 - var2
elif var1<var2:
   var3 = var1 + var2
else:
   var3 = var1
   
print ("Значение третьей переменной: ", var3)