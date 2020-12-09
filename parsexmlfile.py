import xml.dom.minidom as xmldom #这个比较怪，是pycharm的问题，可以别管，只要程序能正常运行


def parse_xml(file,tagname):
    elements = []
    xml_file = xmldom.parse(file)
    root = xml_file.documentElement
    elements=root.getElementsByTagName(tagname)
    for x in elements:
       print(x.nodeName)
       # print(x.lastChild)




if __name__ == '__main__':
    parse_xml("persons.xml","person")
