NotaUm, NotaDois, NotaTres, NotaQuatro = [float(x) for x in input().split(' ')]

N1 = NotaUm * 2
N2 = NotaDois * 3
N3 = NotaTres * 4
N4 = NotaQuatro * 1

ValorFinal = N1 + N2 + N3 + N4
MediaFinal = ValorFinal / 10

if MediaFinal < 5:
    print(f"Media: {MediaFinal:1f}")
    print("Aluno reprovado")

if MediaFinal >= 7:
    print(f"Media: {MediaFinal:.1f}")
    print("Aluno aprovado")

if  5  <= MediaFinal <= 6.9:
    NotaExame = float(input())
    ExameFinal = NotaExame + MediaFinal
    ExameFinal2 = ExameFinal / 2
    if ExameFinal2 >= 5:
        print(f"Media: {MediaFinal:.1f}")
        print("Aluno em exame.")
        print(f"Nota do exame: {NotaExame:.1f}")
        print("Aluno aprovado.")
        print(f"Media final: {ExameFinal2:.1f}")
        
    else:
        print(f"Media: {MediaFinal:.1f}")
        print("Aluno em exame.")
        print(f"Nota do exame: {NotaExame:.1f}")
        print("Aluno reprovado.")
        print(f"Media final: {ExameFinal2:.1f}")
