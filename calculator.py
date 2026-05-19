n=int(input())
a,b=map(int,input().split())
if (n==1):
    print(a+b)
elif(n==2):
    print(a-b)
elif(n==3):
    print(a*b)
elif(n==4):
    print(a/b)
elif(n==5):
    print(a%b)
else:
    print("default operator")
    
    