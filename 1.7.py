min = int(input("Сколько минут вы израсходовали за месяц: "))
sms = int(input("Сколько sms вы израсходовали за месяц: "))
mb = int(input("Сколько mb интернета вы израсходовали за месяц: "))

extra_min = max(0, min - 60) * 0.89
extra_sms = max(0, sms - 30) * 0.59
extra_mb = max(0, mb - 1000) * 0.79

if extra_min > 0: print(min - 60, "доп минуты, сумма за доп минуты =", extra_min)
if extra_sms > 0: print(sms - 30, "доп смс, сумма за доп смс =", extra_sms)
if extra_mb > 0: print(mb - 1000, "доп мб, сумма за доп мб =", extra_mb)

summa = 24.99 + extra_min + extra_sms + extra_mb
nalog = summa * 0.02
itog = summa + nalog
print("Базовая сумма тарификации:", 24.99)
print("Налог (2%):", nalog)
print("Итоговая сумма к оплате:", itog)