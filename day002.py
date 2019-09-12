#计算一个五边形的面积
# import math
# r = float(input("请输入一个半径"))
# s = 2*r*math.sin(math.pi/5)
# area = 5*s*s/(4*math.tan(math.pi/5))
# print("这个五边形的面积为：%0.2f"%area)

#计算大圆距离？？
# import math
# JD_1 WD_1 = input("请输入第一个精度和第一个维度") in degress.split("")
# JD_2 WD_2 = input("请输入第二个精度和第二个维度")
# JD_1_HUD = math.radians()

#计算五角形的面积
# import math
# S = float(input("请输入五角形的边长"))
# area = (5*S*S)/(4*math.tan(math.pi/5))
# print("五角形的面积为：%0.2f"%area)

#求一个正多变形的面积
# import math
# sides = float(input("请输入正多边形的边数："))
# side = float(input("请输入正多边形的边长："))
# area = (sides*side*side)/(4*math.tan(math.pi/sides))
# print("这个多边形的面积为：%0.3f"%area)

#找出ASCII码字符
# number = int(input("请输入一个ASCII码："))
# print (number,"对应的字符为：" ,chr(number))

#工资表
# name = input("请输入名字")
# time = float(input("请输入一周工作的时间"))
# pay = float(input("请输入每小时的报酬"))
# rate = float(input("请输入联邦预扣税率"))
# finall = time*pay*rate
# print("员工姓名为：",name)
# print("一周工作的时间为：%0.1f"%time)
# print("每小时的报酬为：%0.1f"%pay)
# print("联邦预扣税率为：%0.1f"%rate)
# print("员工的一周收入为：%0.1f"%finall)

#反向数字？
# number = float(input("请输入一个4位数"))





#解二元一次方程？
# import math
# a = float(input("请输入a的值"))
# b = float(input("请输入b的值"))
# c = float(input("请输入c的值"))
# R1 = (-b + math.sqrt(b*b - 4*a*c))/(2*a)
# R2 = (-b - math.sqrt(b*b - 4*a*c))/(2*a)
# der = b*b - 4*a*c 
# if der > 0:
# print("此方程两根分别为：%0.2f"%(R1,R2))
# elif der == 0:       
# print("此方程有一个实数根R1与R2相同：%0.2f"%R1)
# else:
# print("此方程没有实数根")

#学习加法
# import random
# number1 = (random.randint(0,100))
# print(number1)
# number2 = (random.randint(0,100))
# print(number2)
# number3 = input("请输入两个随机数之和")
# if number3 == number2 + number1:
#     print("恭喜你答对了")
# else:
#     print("结果错误")

#三个整数排序?
# number1 = int(input("请输入第一个整数"))
# number2 = int(input("请输入第二个整数"))
# number3 = int(input("请输入第三个整数"))
# if number1>number2
#    t=number1
#    number1=number2
#    number2=t
# 
#比较价钱？
# w_k1= float(input("请输入这种包装的重量和价格A"))
# w_k2= float(input("请输入这种包装的重量和价格B"))\

#12
# number1 = float(input("第一条边数"))
# number2 = float(input("第二条边数"))
# number3 = float(input("第三条边数"))
# sum = number1 + number2 + number3
# if number1+number1>number3:
#     print("三角形周长为：%0.2f"%sum)
# else:
#     print("非法输入")

#回文数
# num = input("请输入一个数字")
# if num[:] == num[::-1]:
#     print("这是一个回文数")
# else:
#     print("这不是一个回文数")

#选出一张牌游戏

#剪刀石头布游戏
# import numpy as np 
# computer = np.random.choice(['1','2','3'])
# print(computer)
# user = input('请输入[1,2,3]')
# if computer == user:
#     print('平局')
# elif computer == "1" and user == "2":
#     print("你输了")
# elif computer == "2" and user == "3":
#     print("你输没了")
# elif computer == "3" and user == "1":
#     print("输了，回家吧")
# else:
#     print("赢了")
        