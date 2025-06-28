count=0
for n in range(0,int(input())):
    f=input().split()
    
    if f.count('1')>=2:
        count+=1
print(count)