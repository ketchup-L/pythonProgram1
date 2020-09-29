"""
print("哈喽!我是李孟沙")
#注释快捷键：ctrl+/
print(23)   #整数
print(2.44) #浮点数
print(True) #布尔值
print(False)
print(())   #元组
print([])   #数组
print({})   #字典

print("嘿嘿",1234)
print("哈哈"+"嘿嘿")    #字符串的拼接
print("嘿嘿"*10)    #字符串成倍打印
print(2+5)  #数值运算
print(2<3)  #判断
"""

#变量
#赋值
#变量名必须为小写字母,不要特殊符号
"""
name = "李四"
print(name)
"""

"""
a = input()
print("input获取的内容：",a)    #获取输入的值
b = input("请输入：")
print("第二次输入的内容：",b)
"""

"""
a = input("请输入：")
b = input("请输入：")
print("input获取的内容：",a+b)  #字符串拼接（input获取的都是字符串）
"""

#数据格式的转换 type
# print(type(233))
# print(type(3.5))
# print(type(()))
# print(type(False))
# print(type("嘿嘿"))
# print(type([]))
# print(type({}))

# a = float(input("请输入："))
# b = float(input("请输入："))
# print("input获取的内容：",a+b)    #数值运算

"""
len的使用
# a = "哈哈"
# print(len(a))
"""

"""
练习：通过代码获取两段内容，并且计算它们的长度和
"""
str1 = input("请输入第一段内容：")
str2 = input("请输入第二段内容：")
print("两段内容的长度和：",len(str1)+len(str2))
