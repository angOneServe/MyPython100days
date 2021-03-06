'''

循环引用

所有的引用计数系统，都存在循环应用的问题。例如下面的引用关系：

对象a创建并引用到了对象b.
对象b创建并引用到了对象c.
对象c创建并引用到了对象b.
这时候b和c的引用计数分别是2和1。当a不再使用b，调用release释放对b的所有权，因为c还引用了b，所以b的引用计数为1，b不会被释放。b不释放，c的引用计数就是1，c也不会被释放。从此，b和c永远留在内存中，引起了内存泄漏。



结论:不要让对象的子对象保留自己。
'''
