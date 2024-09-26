#!/usr/bin/env python3
"""Hello World Multi Línguas.

Dependendo da língua configurada no ambiente do programa exibe a mensagem 
correspondente.

Como usar:

Tenha a variável LANG devidamente configurada, ex:

    exporte LANG=pt_BR

Ou informe através do CLI argument `--VAR_TEST`

Ou o usuário terá que digitar.

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.1.3"
__author__ = "Fernando Dias"
__license__ = "Unlicense"

import os
import sys
import logging

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
# nossa instância
log = logging.Logger("logs.py", log_level)
# level
ch = logging.StreamHandler()
ch.setLevel(log_level)
# formatação
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s '
    'l:%(lineno)d f:%(filename)s %(message)s'
)
ch.setFormatter(fmt)
#  destino
log.addHandler(ch)


arguments = {"VAR_TESTE": None, "count": 1}

for arg in sys.argv[1:]:
    try:
        key, value = arg.split("=")
    except ValueError as e:
        log.error(
            "You need to use `=`, You passed %s, try with --key=value: %s", 
            arg,
            str(e)
        )
        sys.exit(1)

    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print("Invalid Option '{key}'")
        sys.exit()

    arguments[key] = value

current_language = arguments["VAR_TESTE"]
if current_language is None:
    # TODO: User repetição
    if "VAR_TESTE" in os.environ:
        current_language = os.getenv("VAR_TESTE")
    else:
        current_language = input('Choose a language:')

current_language = current_language[:5]

msg = {
    "en_US":"Hello World",
    "pt_BR":"Olá, Mundo!!",
    "it_IT":"Ciao, Mondo",
    "es_ES":"Hola, Mundo!!",
    "fr_FR":"Bonjour, Monde!!"
}
"""
# Try com valor default
message = msg.get(current_language, msg["pt_BR"])
""" 

# EAFP
try:
    message = msg[current_language]
except KeyError as e:
    print(f"[ERROR] {str(e)}")
    print(f"Language is invalid, choose from: {list(msg.keys())}")  
    sys.exit(1)

print(
    message * int(arguments["count"])
)
