s={}
n=int(input("Enter Number of Inputs: "))
for i in range(1,n+1):
    name=input("Enter Your name: ")
    lang= input("Enter Your fav Coding lang: ")
    s.update({name:lang})
print(s)