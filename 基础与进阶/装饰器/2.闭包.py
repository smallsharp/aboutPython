# coding=utf-8

# 闭包函数的实例
# outer是外部函数 a和b都是外函数的临时变量
def outer(a):
    b = 10

    # inner是内函数
    def inner():
        # 在内函数中 用到了外函数的临时变量
        print(a + b)

    # 外函数的返回值是内函数的引用
    return inner


if __name__ == '__main__':
    # 此时外函数两个临时变量 a是5 b是10 ，并创建了内函数，然后把内函数的引用返回存给了demo
    # 外函数结束的时候发现内部函数将会用到自己的临时变量，这两个临时变量就不会释放，会绑定给这个内部函数
    demo = outer(5)
    # 我们调用内部函数，看一看内部函数是不是能使用外部函数的临时变量
    # demo存了外函数的返回值，也就是inner函数的引用，这里相当于执行inner函数
    demo()  # 15

    demo2 = outer(7)
    demo2()  # 17
