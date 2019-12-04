#利用反射做一个类似命令行dir类的操作 本命令行有dir cd rename delete help exit等命令

import os
import shutil
class HelpTools:
    def dir(self):
        for v in os.listdir():
            print(v)
        return os.listdir()
    def exit(self):
        quit()
    def help(self):
        print("本命令行有dir cd rename delete help exit等命令")
    def cd(self,directoryName):
        os.chdir(f"./{directoryName}")
    def delete(self,directoryName):
        #shutil.rmtree(directoryName)
        self._delete(directoryName)
    def rename(self,old,new):
        old=os.path.join(os.getcwd(),old)
        new=os.path.join(os.getcwd(),new)
        os.rename(old,new)
    def _delete(self,directoryName):
        #
        os.chdir(f"./{directoryName}")
        """
        os.walk 
        
        返回值：三元组
        root 父目录【string】
        files 所有文件名
        dirs  所有目录名字
        
        参数：
        top:主目录
        topdown 为true的话，先遍历完上层目录，再遍历子目录，相当于广度搜索
                为False的话，先遍历完内层目录，再遍历父目录，相当于深度搜索
        onerror 不知道干啥的，貌似报错时能用到
        
        followlinks 是否遍历快捷方式？
        
        """
        for root,dirs,files in os.walk(os.getcwd(),topdown=False,onerror=lambda:print("你应该是出错了^_^"),followlinks=True):
            for file in files:
                os.remove(os.path.join(root,file))      #删除文件
            for dir in dirs:
                os.rmdir(os.path.join(root,dir))        #删除空文件夹
        os.chdir("..")
        os.rmdir(os.path.join(os.getcwd(),directoryName))

h=HelpTools()
h.dir()

while True:
    cmdstr=input("请输入命令：")
    array=cmdstr.split(" ")
    cmd=array[0]
    count=len(array)

    if hasattr(h,cmd):
        if count==1:
            getattr(h,cmd)()
        elif count==2:
            getattr(h,cmd)(array[1])
        elif count==3:
            getattr(h,cmd)(array[1],array[2])
    else:
        print("没有此命令，重新输入！")
