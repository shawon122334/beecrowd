x,y = map(float,(input().split()))
if x==0:
    print('Origem') if y==0 else print("Eixo Y")

elif y==0:
    print('Origem') if x==0 else print("Eixo X") 
elif x>0:
    print('Q1') if y>0 else print('Q4')
elif x<0:
    print('Q2') if y>0 else print('Q3')
