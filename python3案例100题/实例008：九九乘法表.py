# -*- coding: UTF-8 -*-
# 题目 输出 9*9 乘法口诀表
# 分行与列考虑，共9行9列，i控制行，j控制列

for i in range(1,10):
    for j in range(1,i+1): # %.2f，表示保留小数点后2位
        print('%d*%d=%d'%(i,j,i*j),end=' ') #%.2d，表示长度为2，不满足则在前面补0，长度大于等于2则保持原样输出
    print()


# end=' ',空格来分割各列