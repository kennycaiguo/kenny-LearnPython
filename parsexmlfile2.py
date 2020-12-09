import xml.etree.ElementTree as et

tree = et.ElementTree(file="persons.xml")
# print(tree)
root =  tree.getroot()
# print(root)
# print(root[0][0].text)
for child in root: # 遍历root的子节点
    print(child.tag,"\nformat:name value")
    for childnode in child:
        print(childnode.tag,childnode.text)
    print("================")