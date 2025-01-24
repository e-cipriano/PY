# CALCULADORA PITAGORICA
# Ferramenta desenvolvida para calcular Nomes completos e Datas de Nascimento para resulta em um valor entre 1 e 9, 11 ou 22.
# Como utilizar: Clique em Run (executar codigo), o terminal solicitará o input do nome (completo) ou data de nascimento. Digite sem acentos, til, 
# ou cedilha, utilize apenas alfanumericos e separadores de datas, como barras(/), traços (-) ou pontos(.). 

def calcular_valor_entrada(entrada):
    entrada=entrada.upper()
    entrada=entrada.replace("/","")
    entrada=entrada.replace("-","")
    entrada=entrada.replace(".","")
    tabela_pitagorica={
        "A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,
        "J":1,"K":2,"L":3,"M":4,"N":5,"O":6,"P":7,"Q":8,"R":9,
        "S":1,"T":2,"U":3,"V":4,"W":5,"X":6,"Y":7,"Z":8,
        "1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9
        }
    total=sum(tabela_pitagorica[letra] for letra in entrada if letra in tabela_pitagorica)

    while total > 9 and total not in (11,22):
        total = sum(int(d) for d in str(total))

    valor_entrada=total
    return(valor_entrada)

entrada=input("Digite um nome completo ou data de nascimento dd/mm/aaaa:")
valor_entrada=calcular_valor_entrada(entrada)
print(f"O resultado de {entrada} é {valor_entrada}")