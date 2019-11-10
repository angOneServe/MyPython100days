persons=[True for x in range(30)]
abandon=0
count=0
while abandon<15:
    for index in range(30):
        if persons[index]==False:
            continue
        count+=1        #未淘汰开始数数字
        if count==9:    #报到数字9的淘汰
            count=0
            persons[index]=False
            abandon+=1  #淘汰者加1
    if abandon>=15:     #淘汰者人数超过15，结束
        break
def Display(persons):
    for k,v in enumerate(persons):
        if v:
            print(k,"基督徒")
        else:
            print(k,"非基督徒")
print(persons)
Display(persons)
