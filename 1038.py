a,b = map(int,(input().split()))
if a ==1:
    result = 4.00 * b
    print(f"Total: R$ {result:.2f}")
elif a ==2 :
    result = 4.50 * b 
    print(f"Total: R$ {result:.2f}")
elif a==3:
    result = 5.00 * b 
    print(f"Total: R$ {result:.2f}")
elif a==4:
    result = 2.00 * b 
    print(f"Total: R$ {result:.2f}")
elif a==5:
    result = 1.50 * b 
    print(f"Total: R$ {result:.2f}")
