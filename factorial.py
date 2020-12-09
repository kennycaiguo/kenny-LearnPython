def factorial(i):
    if(i==0):
        return 0
    if(i==1):
        return 1
    return i*factorial(i-1)
i = 15
print("{}的阶乘={}".format(i,factorial(i)))
