n = int(input())
cout = n // 60 #макс кол-во абонементов по 60 поездок
cout1 = (n % 60) // 10 #макс кол-во абонементов по 10 поездок
cout2 = n % 10 #макс кол-во поездок по одному разу
if cout2 * 15 > 125: #если стоимость поездок по одному разу больше чем стоимость одной
    cout2 = 0
    cout1 += 1 #прибавляем один абонемент и обнуляем количество поездок по 1
elif (cout2 * 15) + (cout1 * 125) > 440: #если сумма стоимости абонементов по 10 и единичных поездок больше стоимости одного абонемента на 60
    cout2 = 0
    cout1 = 0 #обнуляем счетчики на 10 и 1 поездок и прибавляем один к абонементам по 60
    cout += 1
print(cout2, end = ' ')
print(cout1, end = ' ')
print(cout, end = ' ')
