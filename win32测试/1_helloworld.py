import win32gui
import win32con
win = win32gui.FindWindow('OpusApp','test.doc - WPS 2019')
tid = win32gui.FindWindowEx(win,None,'_WwG',"DocView")
win32gui.SendMessage(tid, win32con.WM_SETTEXT, None, '你好hello word!')
win32gui.PostMessage(tid,win32con.WM_KEYDOWN,win32con.VK_RETURN,0)
print("%x" % tid)
print("%x" % win)
