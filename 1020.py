#age in days
days = int(input()) 

year = days // 365
days = days % 365

months = days // 30
days = days % 30

print(f"{year} ano(s)")
print(f"{months} mes(es)")
print(f"{days} dia(s)")
