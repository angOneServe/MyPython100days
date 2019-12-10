import os
def DisableNet():
    os.system('''netsh interface set interface name="无线网络连接" admin=disable''')
def EnableNet():
    os.system('''netsh interface set interface name="无线网络连接" admin=enable''')

while True:
    DisableNet()
