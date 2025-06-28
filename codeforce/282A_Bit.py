n=int(input())
x=0
for i in range(0,n):
    bit=list(input())
    
    if '+' in bit:
        x=x+1
        
    elif '-' in bit:
        x=x-1
print(x)    