"""
 * Project name(项目名称)：Python变量作用域
 * Package(包名): 
 * File(文件名): test3
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/26 
 * Time(创建时间)： 13:09
 * Version(版本): 1.0
 * Description(描述)： 获取指定作用域范围中的变量
在一些特定场景中，我们可能需要获取某个作用域内（全局范围内或者局部范围内）所有的变量
1) globals()函数
globals() 函数为 Python 的内置函数，它可以返回一个包含全局范围内所有变量的字典，该字典中的每个键值对，键为变量名，值为该变量的值。
 """

a = 1
b = 2
c = 3


def f1():
    """

    :return:
    """
    a1 = 4
    b1 = 5
    c1 = 6


if __name__ == '__main__':
    # 返回包含当前作用域的全局变量的字典。
    # 注意：对此字典的更新将影响当前全局范围内的名称查找，反之亦然。
    # print(globals())
    dict1 = dict(globals())
    for k, v in dict1.items():
        print(k, "--->", v)

    print()
    print(globals()['a'])
    print(globals()['__file__'])
