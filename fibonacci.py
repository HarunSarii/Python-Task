fibonacci=[]

x,y=0,1

while y<56:
    fibonacci.append(y)
    x,y = y,x+y
print(fibonacci)
