from myRandom import randomNC

while True:
    # یک عدد ده رقمی تولید می کنیم
    nationalCode = randomNC()

    # متغییر برای محاسبه کل مجموع
    total = 0

    # محاسبه مجموع اعداد کد ملی
    for i in range(9):
        total = total + (nationalCode[i] * (10 - i))
        # print(nationalCode[i], ' : ', 10 - i, ' : ', tmp)

    # باقی‌مانده مجموع را به عدد ۱۱ محاسبه میکنیم
    mod = total % 11

    # اگر باقی‌مانده بزرگتر از ۲ باشد باید از عدد ۱۱ کم شود
    if mod >= 2:
        mod = 11 - mod

    # بیت کنترلی باید با باقی‌مانده برابر باشد در این صورت کد ملی صحیح است
    if nationalCode[9] == mod:
        print(*nationalCode, sep='')
        break
