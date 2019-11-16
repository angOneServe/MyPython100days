from openpyxl import Workbook,load_workbook

wb=load_workbook("橙子代课表.xlsx")
binjiang=wb["滨江"]
gaoxin=wb["高新"]
print("滨江".center(120,"*"))
for row in binjiang.rows:
    for v in row:
        text=""
        if v.value==None:
            text=" "
        else:
            text=v.value
        print(f"{text: <16}",end="")
    print()
print("高新".center(120,"*"))
for row in gaoxin.rows:
    for v in row:
        text=""
        if v.value==None:
            text=" "
        else:
            text=v.value
        print("{0: <16}".format(text,),end="")
    print()
print("高新".center(120,"*"))
for row in gaoxin.rows:
    for v in row:
        text=""
        if v.value==None:
            text=" "
        else:
            text=v.value
        print(str(text).ljust(16," "),end="")
    print()
print("高新".center(120,"*"))
for row in gaoxin.rows:
    for v in row:
        text=""
        if v.value==None:
            text=" "
        else:
            text=v.value
        print(f"{text: <16}",end="")
    print()
