from PIL import Image,ImageDraw,ImageFont
import random
def GetChar():
    return chr(random.randint(48,90))
def GetColor(Bg=False):
    if Bg==True:
        return (random.randint(30,255),random.randint(30,255),random.randint(30,255))
    else:
        return (random.randint(0,250),random.randint(0,250),random.randint(0,250))

width=60*4
height=60
#创建一个图片
image=Image.new("RGB",(width,height),(255,255,255))
#常见字体对象
font=ImageFont.truetype(r"C:\Windows\Fonts\Arial.ttf",36)
#创建draw对象
imageDraw=ImageDraw.Draw(image)



for x in range(0,width):
    for y in range(height):
        imageDraw.point((x,y),fill=GetColor(True))
str1=""
for t in range(4):
    ch=GetChar()
    str1+=ch
    imageDraw.text((60*t+10,10),ch,font=font,fill=GetColor())
image.show()
print(str1)
enterStr=input("请输入验证码：")
if enterStr==str1:
    print("正确")
else:
    print("错误")
image.save('code.jpg', 'jpeg')
while True:
    pass
