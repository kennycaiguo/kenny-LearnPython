import json
from types import SimpleNamespace

# dict = {"name": "Mary", "gender": "female", "age": 18} #这是一个字典对象
# p = json.dumps(dict) #这个方法将字典变为字符串
# print(p)
# per=json.loads(p)
# print(per['name'])
class Person:

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age


p = Person("Marycake", "female", 18)
strp = json.dumps(p.__dict__)#注意，如果需要将一个类对象转换为json字符串，需要先调用该对象的__dict__方法
print(strp)
ps = json.loads(strp) #Python中用json反序列化后变成字典对象，需要使用以下方法将其转为类对象
person=SimpleNamespace(**ps)
