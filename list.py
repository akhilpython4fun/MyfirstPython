fruits=["apple","banana","cherry","grapes"]
for x in fruits:
    print(x)
    if x=="cherry":
        print(x+" is a cherry")
        break
    a=0
    for x in range(20):
        print("x="+str(x))
        a=a+x
        print("a="+str(a))
        if x>10:
            print("I'm tired so i'm breaking at 10")
            break
