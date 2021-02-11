percents = 100 + float(input())
rub = int(input())
kop = int(input())
years = int(input())
sum_kop = rub * 100 + kop
i = 0
while i < years:
    sum_kop = sum_kop * percents // 100
    i = i + 1
rub_res = int(sum_kop // 100)
kop_res = int(sum_kop % 100)
print(rub_res, kop_res)
