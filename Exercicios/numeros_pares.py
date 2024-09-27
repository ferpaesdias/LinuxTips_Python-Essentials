"""
Programa que imprime os números pares de 1 a 200 

"""
# # Solução 01
# for num in range(1,101):
#     print(num * 2)

# Solução 02
for num in range(1,201):
    if num % 2 != 0:
        continue
    print(num)