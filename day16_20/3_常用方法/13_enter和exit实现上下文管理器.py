class FileCloser:
    def __init__(self):
        pass
    def __enter__(self):
        print("enter")
        return "enter返回的对象是这个"
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")

with FileCloser() as a:
    print(a)
    pass