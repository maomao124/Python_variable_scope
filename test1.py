"""
 * Project name(项目名称)：Python变量作用域
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/26 
 * Time(创建时间)： 12:54
 * Version(版本): 1.0
 * Description(描述)： 局部变量
 在函数内部定义的变量，它的作用域也仅限于函数内部，出了函数就不能使用了，我们将这样的变量称为局部变量
 """


def f1():
    """
    局部变量
    :return:
    """
    a = 123
    print(a)


if __name__ == '__main__':
    f1()
    # print(a)
