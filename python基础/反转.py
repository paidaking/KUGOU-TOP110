reversed()：是python自带的一个方法

1.列表的反转：
bb = [1,3,5,7]
print(list(reversed(bb)))


2.元组的反转：
aa = (1, 2, 3)
print(tuple(reversed(aa)))


3.字符串的反转
ss = "qwer1234"
print(''.join(reversed(ss)))

--------------------------------------------

Python实现字符串反转的几种方法

要求：在Python环境下用尽可能多的方法反转字符串,例如将s = "abcdef"反转成 "fedcba"

第一种：使用字符串切片
result = s[::-1]

第二种：使用列表的reverse方法
l = list(s)
l.reverse()
result = "".join(l)
当然下面也行

l = list(s)
result = "".join(l[::-1])

第三种：使用reduce
result = reduce(lambda x,y:y+x,s)
第四种：使用递归函数
def func(s):
    if len(s) <1:
        return s
    return func(s[1:])+s[0]
result = func(s)

第五种：使用栈
def func(s):
    l = list(s) #模拟全部入栈
    result = ""
    while len(l)>0:
        result += l.pop() #模拟出栈
    return result
result = func(s)

第六种：for循环
def func(s):
    result = ""
    max_index = len(s)-1
    for index,value in enumerate(s):
        result += s[max_index-index]
    return result
result = func(s)

