# 题目:输入两个字符串str1和str2
# 判断str1中的所有字符是否都存在于str2中
str1 = "abc"
str2 = "abfbewrhc"


def fun():
    for i in (str1):
        f = True
        for j in (str2):
            if j == i:
                f = False
        if f:
            print("False")
            return
    print("True")
fun()
