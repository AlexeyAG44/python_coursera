#решение с сайта
price = float(input())
rub = int(price)
kop = (float(price) - rub) * 100
print(rub, round(kop))

#мое решение (работает правильно, но блядский бот не принял его)
x = float(input())
x1 = str('{0:.2f}'.format(x).lstrip('0').rstrip('.'))
sub_x = "."
res = x1.replace(sub_x, " ")
print(res)
