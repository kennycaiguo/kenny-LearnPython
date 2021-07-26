#输入三个数，输出最大值
num1=input("please enter num1:")
num2=input("please enter num2:")
num3=input("please enter num3:")

medMax=''
maxNum=''

#Python中并没有三目运算符，以下是最接近的写法
medMax=num1 if num1>num2 else num2
maxNum=medMax if medMax>num3 else num3

print("最大值：",maxNum)

