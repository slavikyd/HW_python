n = int(input())
cout = int(input()) #вводим кол-во букв а для сравнения с последующими вводами
out = 0
for i in range(n - 1): 
    a = int(input()) #вводим кол-во букв
    out += min(a, cout) #выбираем меньшее между введенным только что числом и первым введенным
    cout = a #приравниваем для обнуления работы логики цикла
print(out)