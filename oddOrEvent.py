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