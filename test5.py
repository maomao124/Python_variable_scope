"""
 * Project name(项目名称)：Python变量作用域
 * Package(包名): 
 * File(文件名): test5
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/26 
 * Time(创建时间)： 13:19
 * Version(版本): 1.0
 * Description(描述)：
  3) vars(object)
vars() 函数也是 Python 内置函数，其功能是返回一个指定 object 对象范围内所有变量组成的字典。
如果不传入object 参数，vars() 和 locals() 的作用完全相同。
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
    print(locals())


class C1:
    a2 = 1
    b2 = 2
    c2 = 3


if __name__ == '__main__':
    print(vars(C1))
    print()
    print(vars())
