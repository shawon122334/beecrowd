n = float(input())
print('NOTAS:')
for i in [100,50,20,10,5,2]:
    x = n//i
    print(f"{int(x)} nota(s) de R$ {i},00")
    n = n%i
print('MOEDAS:')
for j in [1,0.50,0.25,0.10,0.05,0.01]:
    y = n//j
    print(f"{int(y)} moeda(s) de R$ {j:.2f}")
    n = n%j
