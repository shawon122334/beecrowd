#time conversion 
seconds = int(input()) 

minutes = seconds//60 
seconds = seconds % 60

hour = minutes // 60
minutes = minutes%60

print(f"{hour}:{minutes}:{seconds}")
