def fact(x):
    if x==0:
     return 1
    facto=1
    i=1
    while i<=x: 
        facto=facto*i 
        i=i+1
    return facto

x=int(input('Enter a number:')) 
y=fact(x)
print(y)

