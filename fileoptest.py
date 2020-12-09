file = open("input.txt", mode='a+')
if file is None:  # 这个非常重要，因为python普通的打开文件方式，不会插件新文件，而以下这个选项只有当文件不存在的时候才创建，文件存在就报错，所以需要使用if作为判断
    file = open("input.txt", mode='X')
else:
    flag = True
    while flag:
        content = input("请输入内容：\n")
        print(content)
        if content != 'exit':
            file.write(content + "\n")
        if content == 'exit':
            flag = False
file.flush()
file.close()
exit(0)
