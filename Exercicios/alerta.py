"""
Alarme de temperatura

Pergunte ao usuário qual a temperatura atual e o índice de umidade do ar e será 
exibida uma mensagem de alerta dependendo das condições:

temp > 45: ALERTA!!! Perigo!! Calor extremo
temp vezes 3 for >= a umidade: ALERTA!! Perigo de calor úmido
temp entre 10 e 30: Normal
temp entre 0 e 10: Frio
temp < 0 Frio Extremo

"""
import sys
import logging
log = logging.Logger("alerta")

info = {
    "temperatura": None,
    "umidade": None
}
keys = info.keys()

for key in keys:
    try:
        info[key] = float(input(f"Qual a {key}? ").strip())
    except ValueError:
        log.error(f"{key.capitalize()} inválida")
        sys.exit(1)
temp = info["temperatura"]
umidade = info["umidade"]


if temp > 45:
    print("ALERTA!!! Perigo!! Calor extremo")
elif (temp * 3) >= umidade:
    print("ALERTA!! Perigo de calor úmido")
elif temp >= 10 and temp <= 30:
    print("Normal")
elif temp >= 0 and temp < 10:
    print("Frio")
elif temp < 0:
    print("Frio extremo")

print(temp)
print(umidade)