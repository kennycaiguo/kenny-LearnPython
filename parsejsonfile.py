import json
from types import SimpleNamespace

with open("example.json","r",encoding="utf-8") as jsonfile:#打开json文件，最好指定编码为utf-8，因为不支持gbk
    jsondict= json.load(jsonfile) #这个是字典
    jsonobj=SimpleNamespace(**jsondict) #这个将字典转换为对象
    print(jsonobj.data)