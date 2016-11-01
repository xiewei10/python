# coding = utf-8
#!/usr/bin/python3
__author__ = "谢威"

import  sys


# Fibonacci series: 斐波纳契数列
# # 两个元素的总和确定了下一个数
# a,b = 0,1;
# while(b < 10):
#    print(b,end = "---"); #关键字end可以用于将结果输出到同一行，或者在输出的末尾添加不同的字符
#    a,b = b,a+b;
#
#
# n=100;
# sum = 0;
# i = 1;
# while (i <= n):
#     sum +=i;
#     i +=1;
#
# print(sum);
#
# while (1>0):
#     num = int(input("输入的数为 "));
#     print("输入是 ",num);
#




# 迭代器
# 迭代是Python最强大的功能之一，是访问集合元素的一种方式。。
# 迭代器是一个可以记住遍历的位置的对象。
# 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。
# 迭代器只能往前不会后退。
# 迭代器有两个基本的方法：iter() 和 next()。
# 字符串，列表或元组对象都可用于创建迭代器：

# list = [1,2,3,4];
# it = iter(list);
# print(next(it));
# print(next(it));
# print(next(it));
# print(next(it));
#
# list2 = ["9","10","11"];
# it = iter(list2); # 迭代器对象创建
#
# for x in it:
#     print(x);
#

#也可以使用 next() 函数：创建迭代器

'''
try:
    <...............>   #可能得到异常的语句
except <.......>:       #锁定是哪种异常
    <...............>   #出现异常的处理方法

'''
# list = [1,2,3,4];
# it = iter(list);
# while True:
#     try:
#         print(next(it));
#     except StopIteration:
#         sys.exit();
#


#### 生成器
# 在 Python 中，使用了 yield 的函数被称为生成器（generator）。
# 跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
# 在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，
# 返回yield的值。并在下一次执行 next()方法时从当前位置继续运行。
#
#






