nota1 = int (input ("informe sua nota: "))
nota2 = int (input("informe sua nota: "))
nota3 = int (input("informe sua nota: "))
media = (nota1 + nota2 + nota3) / 3
if media <=4.9:
    print("Reprovado❌")
elif media <= 6.9:
    print("Recuperação⚠️")
elif media >= 7:
    print("Aprovado✅")
print (f"a sua nota foi {media}")