# LearnPython
学习python编程
# <a href="https://github.com/geekcomputers/Python">Python学习项目</a>
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
  
# python实现只要用户输入的不是exit，就将用户的输入保存到一个叫"input.txt" 的文件中
file = open("input.txt", mode='a+')
if file==None: //这个非常重要，因为python普通的打开文件方式，不会插件新文件，而以下这个选项只有当文件不存在的时候才创建，文件存在就报错，所以需要使用if作为判断
    file=open("input.txt",mode='X')
else:
    flag=True
    while flag:
        content = input("请输入内容：\n")
        print(content)
        if content!='exit':
           file.write(content+"\n")
        if content == 'exit':
          flag=False
file.flush()
file.close()
exit(0)

# python读取xml文件的内容并且解析1
from xml.etree import ElementTree as et ## 这个用来解析xml字符串
xml1=open("person.xml") 
lines=[]
lines2=[]
lines=xml1.readlines()
lines=lines[1:] #这句话的作用是去除xml声明语句,因为后面的xml解析不需要
for x in lines:
    if x[len(x)-1]=='\n':
       lines2.append(x[0:len(x)-1]) #去除换行符
    else:
        lines2.append(x)
strlines = "".join(lines2)
print(strlines)
root = et.fromstring(strlines)
print(root.tag)
child1 =root.__getitem__(0)
child2 =root.__getitem__(1)
child3 =root.__getitem__(2)

print(child1,child2,child3)

# python读取xml文件，并且删除每一个子节点的值：very good
import xml.etree.ElementTree as et

tree = et.ElementTree(file="persons.xml") #### 这个文件必须放在虚拟环境的env文件夹中
# print(tree)
root =  tree.getroot() ####获取跟节点
# print(root)
# print(root[0][0].text)
for child in root: # 遍历root的子节点
    print(child.tag,"\nformat:name value")
    for childnode in child: ####遍历每一个节点的子节点
        print(childnode.tag,childnode.text)
    print("================")
    
# Python 把字典输出到excel文件
import pandas as pds

dict={
       "Jack":{"chinese":80,"english":90,"physics":78,"math":77},
       "Lili":{"chinese":70,"english":80,"physics":70,"math":67},
       "Mike":{"chinese":85,"english":70,"physics":90,"math":87},
       "Christy":{"chinese":60,"english":91,"physics":70,"math":70},
      }
df =pds.DataFrame(dict)
df.to_excel('student.xlsx')
