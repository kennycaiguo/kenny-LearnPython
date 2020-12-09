from xml.etree import ElementTree as et
# xml = """<books>
#   <book id='37476'>aaaa</book>
#   <book id='83727'>bbbb</book>
#  </books>"""
xml1=open("person.xml")
lines=[]
lines2=[]
lines=xml1.readlines()
lines=lines[1:]#这句话的作用是去除xml声明语句,因为后面的xml解析不需要
for x in lines:
    if x[len(x)-1]=='\n':
       lines2.append(x[0:len(x)-1])#去除换行符
    else:
        lines2.append(x)
# print(lines2)
strlines = "".join(lines2)
print(strlines)
root = et.fromstring(strlines)
print(root.tag)
child1 =root.__getitem__(0)
child2 =root.__getitem__(1)
child3 =root.__getitem__(2)

print(child1,child2,child3)