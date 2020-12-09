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
    


 