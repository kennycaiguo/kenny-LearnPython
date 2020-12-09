import pandas as pds #需要安装xlrd： pip install xlrd

xcl =pds.read_excel("score.xlsx") #xcl相当于excel的worksheet
# print(xcl) #打印所有内容
head1 = xcl.head(1) #获取第一行内容
print(head1) #打印第一行,每一行都是一个字典
for r in xcl.iterrows(): #可以迭代
    print(r)
# rowsum =head1.sum() #
# rowcount = head1.count() #
# print(rowsum)
# colen=head1.__getitem__("English") #获取本行指定名称的列单元
# print(colen)
# print(xcl.head(1)["chinese"]) #打印第一行
# print(xcl.columns[1]) #获取第一列

column1 = xcl.__getitem__("chinese") #根据列名获取一列的数据，__getitem__("chinese")
print(column1.sum()) #计算本列总和
print(column1.count()) #获取本列有多少项
print(column1.sum()/column1.count()) #计算本列平均值
print(xcl)
# df = pds.DataFrame(xcl,index=[0,1,2,3,4],columns=["name","chinese","English","math","computer"])
df = pds.DataFrame(xcl) #需要安装 openpyxl：pip install openpyxl
df.to_excel("bal.xlsx")