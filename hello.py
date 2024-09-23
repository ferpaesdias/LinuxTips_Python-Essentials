#!/usr/bin/env python3
"""Hello World Multi Línguas.

Dependendo da língua configurada no ambiente do programa exibe a mensagem 
correspondente.

Como usar:

Tenha a variável LANG devidamente configurada, ex:

    exporte LANG=pt_BR

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.1.2"
__author__ = "Fernando Dias"
__license__ = "Unlicense"

import os

current_language = os.getenv("VAR_TESTE", "pt_BR")[:5]

msg = {
    "en_US":"Hello World",
    "pt_BR":"Olá, Mundo!!",
    "it_IT":"Ciao, Mondo",
    "esp_SP":"Hola, Mundo!!",
    "fr_FR":"Bonjour, Monde!!"
}

print(msg[current_language])  
