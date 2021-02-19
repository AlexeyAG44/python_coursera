# Процентная ставка по вкладу составляет P процентов годовых,
# которые прибавляются к сумме вклада.
# Вклад составляет X рублей Y копеек.
# Определите размер вклада через год.
# При решении этой задачи нельзя пользоваться условными инструкциями и циклами.

percents = float(input())
rub = int(input())
kop = int(input())
rub_in_kop = rub * 100
sum_kop = rub_in_kop + kop
per_year = (sum_kop / 100) * percents
per_year_kop = per_year + sum_kop
rub_res = int(per_year_kop // 100)
kop_res = int(per_year_kop % 100)
if per_year_kop % 100 == 0:
    print(rub_res, kop_res)
else:
    print(rub_res, round(kop_res))