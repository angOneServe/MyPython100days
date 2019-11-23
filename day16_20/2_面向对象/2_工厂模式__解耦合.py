from day16_20.sdk import *

class PersonFactory:
    @staticmethod
    def creat(type):
        if type=="b":
            return bilibiler()
        elif type=="d":
            return douyiner()
        else:
            print("提供了PersonFactory不生产的Person类")

PersonFactory.creat("b").say()
PersonFactory.creat("d").say()
PersonFactory.creat("")
