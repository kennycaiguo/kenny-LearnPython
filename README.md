# LearnPython
学习python编程
# <a href="https://blog.csdn.net/tz_zs/article/details/78228542">python 占位符（百分号方式、Format 方式）</a>
# python 递归
## febonacci.py
def febonacci(i):
    if(i==0):
        return 0
    if(i==1):
        return 1
    return febonacci(i-1)+febonacci(i-2)   
feb = []
for i in range(0,10):
    feb.append(febonacci(i)) 
print(feb)
    
## factorial.py //计算一个数的阶乘如：5*4*3*2*1.。。
def factorial(i):
    if(i==0):
        return 0
    if(i==1):
        return 1
    return i*factorial(i-1)
i = 15
print("{}的阶乘={}".format(i,factorial(i)))

# Python遍历文件夹，使用os.walk(文件夹路径)
import os

def WalkThruDir(dir):
    g = os.walk(dir)
    for path,dirlist,filelist in g:
        for file in filelist:
            print(os.path.join(path,file))
WalkThruDir("e:/pythonstudy")        
# python 分离奇数和偶数
nums = [1,2,3,4,5,11,12,13,14,15]
odds = []
events = []
while(len(nums) > 0):
    num = nums.pop()
    if(num%2==0):
        events.append(num)
    else:
         odds.append(num)   
print(odds,events)        

# python 变量列表
colors = ['red', 'green', 'blue', 'yellow', 'white', 'black']
 
for color in colors:
    print("color is :",color)
    
# python格式化输出
### 实例1
for x in range(1, 11):
     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
     
### 实例2
 print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com'))
菜鸟教程网址： "www.runoob.com!"
     
## Python发送电子邮件：
import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host ="smtp.gmail.com"
mail_user="caivenus2019@gmail.com"
mail_pass="你的账户密码" #这里要改成你的账户密码
port=465

sender = "caivenus2019@gmail.com"
receiver="guimaihong@gmail.com"

message=MIMEText("Python mail test",'plain','utf-8')
subject="mail test"
message['subject']=Header(subject,'utf-8')

try:
  smtpobj = smtplib.SMTP_SSL(mail_host,port) 
  smtpobj.login(mail_user,mail_pass)
  smtpobj.sendmail(sender,receiver,message.as_string())
except smtplib.SMTPException:
  print("fail to send mail")
