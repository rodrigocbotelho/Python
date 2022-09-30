resposta = str(input('BEM-VINDO AO SISTEMA DE BOLETIM ON-LINE DA SEDUC PRESSIONE A TECLA "S" PARA CONTINUAR:').strip().lower())
while resposta == 's':
    print('                    BOLETIM ON-LINE SEDUC\033[m')
    print('NOTA MÉDIA 5.0')
    print('MÉDIA ANUAL MIN 50.0')
    materia = str(input('INFORME A DISCIPLINA: ').strip().upper())
    n1 = float(input('1° Av: ').strip())
    n2 = float(input('2° Av: ').strip())
    n3 = float(input('3° Av: ').strip())
    n4 = float(input('4° Av: ').strip())
    media = (n1 * 2) + (n2 * 3)  + (n3 * 2) + (n4 * 3)
    print('DISCIPLINA: {}'.format(materia))
    print('MÉDIA: {}'.format(media))
    if (media >= 50 ):
        print('STATUS: APROVADO')
    else:
        print('STATUS: REPROVADO')
    resposta = str(input('BOLETIM ON-LINE DA SEDUC PRESSIONE A TECLA "S" PARA REPETIR: ').strip().lower())
