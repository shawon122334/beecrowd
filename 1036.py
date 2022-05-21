a,b,c = map(float,(input().split()))

root = (b**2 - 4*a*c)

if a==0 or root<0:
    print("Impossivel calcular")
else:    
    x1 = (-b+ root**0.50)/(2*a)
    x2 = (-b-root**0.50)/(2*a)
    print(f"R1 = {x1:.5f}")
    print(f"R2 = {x2:.5f}")
