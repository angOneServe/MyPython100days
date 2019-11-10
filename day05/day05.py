jiweng=5
jimu=3
jichu=1/3.0

#百鸡百钱
for i in range(0,101):
    for j in range(0,101-i):
        for o in range(0,101-i-j):
            if i+j+o==100:
                if jiweng*i+jimu*j+jichu*o==100:
                    print(i,j,o)


print("\n\ncraps赌博游戏")
'''
0-12
    玩家胜利      庄家胜利
1：  7 11          2 3 12
    第一次点数      7
'''
import random
money=1000
first=True
firstDian=-1
while money>0:
    debt=int(input("请下注："))
    if money<debt:
        continue

    dianshu=random.randint(1,12)
    #记录第一次
    if first==True:
        first=False
        firstDian=dianshu
        if dianshu in [7,11]:
            money+=debt
            print("玩家胜利","  第一次点数：",firstDian,"  抽的点数：",dianshu,"  剩余钱数：",money)

        if dianshu in [2,3,12]:
            money-=debt
            print("玩家失败","  第一次点数：",firstDian,"  抽的点数：",dianshu,"  剩余钱数：",money)

        continue
    #非第一次
    if dianshu ==firstDian:
        money+=debt
        print("玩家胜利","  第一次点数：",firstDian,"  抽的点数：",dianshu,"  剩余钱数：",money)

        continue
    elif dianshu==7:
        money-=debt
        print("玩家失败","  第一次点数：",firstDian,"  抽的点数：",dianshu,"  剩余钱数：",money)
        continue

    print("再来一次!","  第一次点数：",firstDian,"  抽的点数：",dianshu,"  剩余钱数：",money)
print("赌资耗尽")

for i in range(0,4):
    if 1==1:
        print(1)
        if 2==2:
            print(2)
            if True:
                print(2,1)
                continue
            if True:
                print(2,2)
                continue
            print(2,3)
            continue

