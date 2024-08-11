a= input("First Fibonacci number")
b= input("2nd fibonacci number")
a=int(a)
b=int(b)
fibn=a+b
print("Fibonacci number")
print(a)
print(b)
while fibn<=1000:
    print(fibn)
    a=b
    b=fibn
    fibn=a+b
    print(fibn)







