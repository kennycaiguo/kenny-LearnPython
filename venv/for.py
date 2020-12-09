# colors = ['red', 'green', 'blue', 'yellow', 'white', 'black']
#
# for color in colors:
#     print("color is :", color)

#迭代器对象的简单使用
# list=[1,2,3,4]
# it = iter(list)    # 创建迭代器对象
# for x in it:
#     print (x, end=" ")

#在类中使用迭代器
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)