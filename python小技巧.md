# Python3 安装pygame：
  ## python -m pip install pygame
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

# Python在字符串中动态插值:
在字符串插值的四种方法 | Python
 
1. 通过(%)操作符拼接
>>>print('%s %s!' % ('Hello', 'World'))
Hello World!
2. 通过str.format()方法拼接

 
>>>print('{} {}!'.format('Hello', 'World'))
Hello World!
通过这种方式拼接字符串需要注意的是字符串中{}的数量要和format方法参数数量一致，否则会报错。

3. 通过F-strings拼接

 
>>> s1 = 'Hello'
>>> s2 = 'World'
>>> print(f'{s1} {s2}!')
Hello World!
在python3.6.2版本中，PEP 498 提出一种新型字符串格式化机制，被称为“字符串插值”或者更常见的一种称呼是F-strings，F-strings提供了一种明确且方便的方式将python表达式嵌入到字符串中来进行格式化

4. 通过string模块中的Template对象拼接

>>> from string import Template
>>> s = Template('${s1} ${s2}!')
>>> s.safe_substitute(s1='Hello',s2='World')
Hello World!
Template的实现方式是首先通过Template初始化一个字符串。这些字符串中包含了一个个key。通过调用substitute或safe_subsititute，将key值与方法中传递过来的参数对应上，从而实现在指定的位置导入字符串。这种方式的好处是不需要担心参数不一致引发异常，如：

 
>>> from string import Template
>>> s = Template('${s1} ${s2} ${s3}!')
>>> s.safe_substitute(s1='Hello',s2='World')
Hello World ${s3}!




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
