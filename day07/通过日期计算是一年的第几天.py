
def GetDays(year,mounth,day):
    runDay=(31,29,31,30,31,30,31,31,30,31,20,31)
    notrunDay=(31,28,31,30,31,30,31,31,30,31,20,31)
    runNian=False
    if year%4==0 and year%100!=0 or year%400==0:
        runNian=True
    sum=0
    if runNian:
        for index in range(0,mounth-1):
            sum+=runDay[index]
        sum+=day
    else:
        for index in range(0,mounth-1):
            sum+=notrunDay[index]
        sum+=day
    return sum

print(GetDays(2019,10,28))

