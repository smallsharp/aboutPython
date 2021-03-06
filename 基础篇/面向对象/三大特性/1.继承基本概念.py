class Animal:
    pass


class Person(Animal):
    pass


tester = Person()

'''查看 对象和类 的类型'''
print(tester.__class__)  # p1 是由 <class '__main__.Person'> 实例化而来
print(Person.__class__)  # Person 是由 <class 'type'> 实例化而来
print(type.__class__)  # type 是由 <class 'type'> 实例化而来

"""查看父类"""
print(Person.__bases__)  # Person 继承自 (<class '__main__.Animal'>,)
print(Animal.__bases__)  # Animal 继承自 (<class 'object'>,)
print(int.__bases__)  # Animal 继承自 (<class 'object'>,)
print(bool.__bases__)  # bool 继承自 (<class 'int'>,)
print(type.__bases__)  # type继承自 (<class 'object'>,)
