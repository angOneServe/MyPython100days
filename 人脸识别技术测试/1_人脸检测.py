import base64
from aip import AipContentCensor
from collections import Iterator

def face_search(imagefile):
    APP_ID = "18000697"
    API_KEY = "bM1vgg3d1illxop8IgXxRrIV"
    SECRET_KEY = "UDvV3krkXwdaIUhoserrlO7UZBZrsMRp "

    aipface = AipFace(APP_ID, API_KEY, SECRET_KEY)  # 百度人脸识别接口

    image = base64.b64encode(open(imagefile, 'rb').read()).decode('utf8')  # 识别的图片
    imageType = "BASE64"  # 上传图片的格式，百度要求的参数
    groupIdList = "test"  # 要搜索的用户组范围，多个用户组用逗号隔开

    #
    dict1={"face_field":"age,beauty,expression",}
    result=aipface.detect(image,imageType,dict1)
    if result["error_code"]==0:  #表示无错误
        r=result["result"]
        print(r)

        print(r["face_num"])
        print(r["face_list"][0]["beauty"])


    re=aipface.faceverify(images=[image,])
    print(re)
if __name__ == '__main__':

    face_search("周冬雨.jpg")
