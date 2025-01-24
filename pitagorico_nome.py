

def calcular_valor_nome(nome):
    nome=nome.upper()
    nome=nome.replace("/","")
    tabela_pitagorica={
        "A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,
        "J":1,"K":2,"L":3,"M":4,"N":5,"O":6,"P":7,"Q":8,"R":9,
        "S":1,"T":2,"U":3,"V":4,"W":5,"X":6,"Y":7,"Z":8,
        "1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9
        }
    total=sum(tabela_pitagorica[letra] for letra in nome if letra in tabela_pitagorica)

    while total > 9 and total not in (11,22):
        total = sum(int(d) for d in str(total))

    valor_nome=total
    return(valor_nome)

nome=input("Digite um nome completo ou data de nascimento dd/mm/aaaa:")
valor_nome=calcular_valor_nome(nome)
print(f"O resultado de {nome} é {valor_nome}")