"""
 * Project name(项目名称)：Python变量作用域
 * Package(包名): 
 * File(文件名): test4
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/26 
 * Time(创建时间)： 13:16
 * Version(版本): 1.0
 * Description(描述)： 2) locals()函数
locals() 函数也是 Python 内置函数之一，通过调用该函数，我们可以得到一个包含当前作用域内所有变量的字典。
这里所谓的“当前作用域”指的是，在函数内部调用 locals() 函数，会获得包含所有局部变量的字典；
而在全局范文内调用 locals() 函数，其功能和 globals() 函数相同。
 """

a = 1
b = 2
c = 3


def f1():
    """
    返回包含当前作用域的局部变量的字典。
    注意：此字典的更新是否会影响本地范围内的名称查找，反之亦然，这取决于实现，并且不受任何向后兼容性保证的覆盖。
    :return:
    """
    a1 = 4
    b1 = 5
    c1 = 6
    print(locals())


if __name__ == '__main__':
    f1()
    print()
    print(locals())
