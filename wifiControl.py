import os
import tkinter
def DisableNet():
    os.system('''netsh interface set interface name="无线网络连接" admin=disable''')
def EnableNet():
    os.system('''netsh interface set interface name="无线网络连接" admin=enable''')
cmd="Disable"


import win32serviceutil
import win32service
import win32event

class wifiControl(win32serviceutil.ServiceFramework):
    _svc_name_ = "wifiControl"#服务名
    _svc_display_name_ = "Python wifiControl Service"
    _svc_description_ = "控制无线的连接"

    #__init__完成后，系统服务算是启动成功了，
    # 然后会去调用SvcDoRun函数，该函数不能结束，结束表示服务终止
    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)

        print("aaaaaaaaaaaaaaaaaaaaaaaaa")

    #实际的逻辑代码不论是放在init以线程方式启动还是SvcDoRun中调用，
    # 都需要确保SvcDoRun不退出
    def SvcDoRun(self):
        print("bbbbbbbbbbbbbbbbbbbbbbbb")

        while True:
            if cmd=="help":
                print("Enable Disable")
            if cmd=="Enable":
                EnableNet()
            if cmd=="Disable":
                DisableNet()

            cmd=input("(help)>")
        win32event.WaitForSingleObject(self.hWaitStop, win32event.INFINITE)

    #服务停止时调用
    def SvcStop(self):
        print("cccccccccccccc")
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

if __name__=='__main__':
    win32serviceutil.HandleCommandLine(wifiControl)
