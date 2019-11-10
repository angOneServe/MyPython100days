#
from threading import Lock
from threading import Thread
import time
lock=Lock()
counter=0
class Task(Thread):
    def __init__(self,id):
        super().__init__()
        self.id=id
        self.lock=Lock()
    def run(self):
        global counter
        locked=False
        if locked:
            self.lock.acquire()
            try:
                time.sleep(0.1)
                counter+=1
            except:
                pass
            finally:
                self.lock.release()
        else:
            time.sleep(0.1)
            counter+=1
pool=[]
def main():
    for i in range(1000):
        t=Task(i)
        t.start()
        pool.append(t)
    for v in pool:
        v.join()
if __name__=="__main__":
    main()
    print(counter)
