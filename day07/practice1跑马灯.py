import os
import time
def main():
    content="北京欢迎您为您开天辟地..."
    while True:
        i=os.system('cls')
        #print('\033c',end='')
        print(content)
        time.sleep(0.1)
        content=content[1::]+content[0]
if __name__=="__main__":
    main()
