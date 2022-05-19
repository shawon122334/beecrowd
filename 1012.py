a,b,c = list(map(float,input().split()))
pi = 3.14159

triangle = (1/2)*a*c 
print(f"TRIANGULO: {triangle:.3f}")

radius_circle = pi*c**2 
print(f"CIRCULO: {radius_circle:.3f}")

area_of_trapezium = ((a+b)/2)*c
print(f"TRAPEZIO: {area_of_trapezium:.3f}")

area_of_square = b*b
print(f"QUADRADO: {area_of_square:.3f}")

area_of_rectangle = a*b
print(f"RETANGULO: {area_of_rectangle:.3f}")
