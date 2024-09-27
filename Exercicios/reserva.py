"""
Faça um programa de terminal que exibe ao usuário uma lista dos quartos 
disponíveis para alugar e o preço  de cada quarto, esta informação está 
disponível em um arquivo de texto separado por vírgulas.

`quartos.txt`
```
# codigo, nome, preco
1,Suite Master,500
2,Quarto Famillia,200
3,Quarto Single,100
4,Quarto Simples,50  
```

O programa pergunta ao usuário o nome, qual o número do quarto a ser resevado e 
a quantidade de dias e no final exibe o valor estimado a ser pago.

O programa deve salvar esta escolha em outro arquivo contendo as reservas

`reservas.txt`

```
# cliente, quarto, dias
Bruno,3,12
```

Se outro usuário tentar reservar o mesmo quarto o programa deve exibir uma 
mensagem informando que já está reservado.
"""
import sys
import logging

quartos = {}
try:
    for line in open("quartos.txt"):
        codigo, nome, preco = line.strip().split(",")
        quartos[int(codigo)] = {
            "nome": nome,
            "preco": float(preco), # TODO: Decimal
            "disponivel": True
        }
except FileNotFoundError:
    logging.error("Arquivo não existe")
    sys.exit(1)

for codigo, dados in quartos.items():
    nome = dados["nome"]
    preco = dados["preco"]
    disponivel = "⛔️" if not dados["disponivel"] else "👍️"
    # TODO: Substituir casa decimal por virgula
    print(f"{codigo} - {nome} - R$ {preco:.2f} - {disponivel}")

nome = input("Nome do cliente: ").strip()
try:
    num_quarto = int(input("Número do quarto"))
    if not quartos[num_quarto]["disponivel"]:
        print(f"O quarto {num_quarto} esta ocupado")
except ValueError:
    logging.error("Número inválido, digite apenas dígitos")
    sys.exit(1)

if quarto not in quartos:
    print("Quartos escolhido inválido")

try:
    dias = int(input("Número do dias"))
except ValueError:
    logging.error("Número inválido, digite apenas dígitos")
    sys.exit(1)

