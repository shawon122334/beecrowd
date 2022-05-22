n1,n2,n3,n4 =map(float,(input().split()))
avg = (n1*2 + n2*3 + n3*4 + n4*1)/(2+3+4+1)
print(f"Media: {avg:.1f}")
if avg >= 7.0: 
    print("Aluno aprovado.")
elif avg < 5.0:
    print("Aluno reprovado.")
elif avg >= 5.0 and avg <= 6.9:
    print("Aluno em exame.")
    examScore = float(input())
    print(f"Nota do exame: {examScore:.1f}")
    avg2 = (examScore+avg)/2
    if avg2 >= 5.0:
        print("Aluno aprovado.")
        print(f"Media final: {avg2:.1f}")
    elif avg2<= 4.9:
        print("Aluno reprovado.")
        print(f"Media final: {avg2:.1f}")
