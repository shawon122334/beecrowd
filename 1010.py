# code_prod1 = int(input())
# no_of_units_of_prod1 = int(input())
# price_of_prod1 = "{:2f}".format(float(input()))

# code_prod2 = int(input()) 
# no_of_units_of_prod2 = int(input())
# price_of_prod2 = "{:2f}".format(float(input()))

input1 = input().split()[1:]
unit_prod1 = int(input1[0]) 
price_prod1 = float(input1[1])

input2 = input().split()[1:] 
unit_prod2 = int(input2[0]) 
price_prod2 = float(input2[1])

payable = (unit_prod1*price_prod1) + (unit_prod2*price_prod2)

print(f"VALOR A PAGAR: R$ {payable:.2f}")
 