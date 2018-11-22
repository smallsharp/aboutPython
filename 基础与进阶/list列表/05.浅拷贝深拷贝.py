'''
在 python 中，标识一个对象唯一身份的是：对象的id(内存地址)，对象类型，对象值，
而浅拷贝就是创建一个具有相同类型，相同值但不同id的新对象。
'''
import copy

a = [1, 2, 3, 4, ['a', 'b']]  # 原始对象

# 赋值，传对象的引用
b = a

# 对象拷贝，浅拷贝(只拷贝第一层数据)
c = copy.copy(a)

# 对象拷贝，深拷贝（深层次拷贝）
d = copy.deepcopy(a)

'''
重点：均操作完毕后，查看各个操作之间的差异
'''

# a中追加一个元素
a.append(5)  # a =  [1, 2, 3, 4, ['a', 'b', 'c'], 5]

# 修改对象a中的['a', 'b']数组对象
a[4].append('c')

print('a = ', a)  # a =  [1, 2, 3, 4, ['a', 'b', 'c'], 5]
print('b = ', b)  # b =  [1, 2, 3, 4, ['a', 'b', 'c'], 5]
print('c = ', c)  # c =  [1, 2, 3, 4, ['a', 'b', 'c']]
print('d = ', d)

'''
总结：
1. 赋值运算：其实就是对象的引用（起别名），修改其中一方，另一个也会跟着发生改变
2. 浅拷贝(copy)：拷贝父对象，不会拷贝对象的内部的子对象。
3. 深拷贝(deepcopy)： copy 模块的 deepcopy 方法，完全拷贝了父对象及其子对象。

附：浅拷贝的三种形式
浅拷贝有三种形式:
    切片操作:  b = a[:] 或者 b = [x for x in a];
    工厂函数： b = list(a);
    copy函数： b = copy.copy(a)
'''
