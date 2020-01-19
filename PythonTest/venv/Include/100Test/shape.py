

# 各个形状

for i in range(-4,5):
    if i<0:       #if..else..条件可以写成三木运算符形式
        j=-i      #  j=-i if i<0 else j=i
    else:
        j=i
    #先是j个空格，然后打印（9-2j）个* ，后面的都是空格，在屏幕上不显示，可以不打印#
    print(' '*j+'*'*(9-2*j))

print("\n")
print("\n")
print("\n")
print("\n")


# 对顶三角形
for i in range(-4,5):
    if i<0:
        j=-i
    else:
        j=i
    print(' '*(9//2 -j)+'*'*(2*j + 1))   #先是(9//2 -j)j个空格，然后打印(2*j + 1)个空格，后面的都是空格，在屏幕上不显示，可以不打印