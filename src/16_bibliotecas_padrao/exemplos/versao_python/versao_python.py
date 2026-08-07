# Importa o módulo sys, que fornece acesso a algumas variáveis usadas ou mantidas pelo interpretador Python,
# bem como funções que interagem com o sistema.
import sys

print("Versão do Python")

# Imprime a versão do Python utilizando a variável version do módulo sys, que contém a string da versão do Python.
print(sys.version)

print("Informação da versão instalada")

# Imprime informações detalhadas sobre a versão do Python utilizando a variável version_info do módulo sys.
# A variável version_info é uma tupla contendo informações como major, minor, micro, releaselevel e serial.
print(sys.version_info)
