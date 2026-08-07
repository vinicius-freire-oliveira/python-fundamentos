import re

# 1. Encontrar Palavras Específicas
padrao = r'\bcat\b'
texto = "O gato está no tapete com um cat."
matches = re.findall(padrao, texto)
print(f"1. Palavras específicas: {matches}")  # Deve imprimir: ['cat']

# 2. Correspondência de Dígitos
padrao = r'\d'
texto = "Há 123 gatos."
matches = re.findall(padrao, texto)
print(f"2. Dígitos: {matches}")  # Deve imprimir: ['1', '2', '3']

# 3. Correspondência de Um ou Mais Dígitos
padrao = r'\d+'
texto = "Há 123 gatos."
matches = re.findall(padrao, texto)
print(f"3. Um ou mais dígitos: {matches}")  # Deve imprimir: ['123']

# 4. Correspondência de Caracteres Alfabéticos
padrao = r'[a-zA-Z]'
texto = "Gato123"
matches = re.findall(padrao, texto)
print(f"4. Caracteres alfabéticos: {matches}")  # Deve imprimir: ['G', 'a', 't', 'o']

# 5. Correspondência de Endereço de E-mail
padrao = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
texto = "Meu e-mail é exemplo@exemplo.com."
matches = re.findall(padrao, texto)
print(f"5. Endereço de e-mail: {matches}")  # Deve imprimir: ['exemplo@exemplo.com']

# 6. Correspondência de Data (Formato DD/MM/AAAA)
padrao = r'\b\d{2}/\d{2}/\d{4}\b'
texto = "Hoje é 05/06/2024."
matches = re.findall(padrao, texto)
print(f"6. Data (DD/MM/AAAA): {matches}")  # Deve imprimir: ['05/06/2024']

# 7. Correspondência de CEP (Formato Brasileiro)
padrao = r'\d{5}-\d{3}'
texto = "Meu CEP é 12345-678."
matches = re.findall(padrao, texto)
print(f"7. CEP (Formato Brasileiro): {matches}")  # Deve imprimir: ['12345-678']

# 8. Correspondência de Número de Telefone (Formato Internacional)
padrao = r'\+\d{1,3}\s\d{1,4}[\s-]\d{4,10}'
texto = "Ligue para +55 21 1234-5678."
matches = re.findall(padrao, texto)
print(f"8. Número de telefone (Internacional): {matches}")  # Deve imprimir: ['+55 21 1234-5678']

# 9. Correspondência de URLs
padrao = r'https?://(?:www\.)?[a-zA-Z0-9./?=&_-]+'
texto = "Visite https://www.exemplo.com para mais informações."
matches = re.findall(padrao, texto)
print(f"9. URLs: {matches}")  # Deve imprimir: ['https://www.exemplo.com']

# 10. Correspondência de Tags HTML
padrao = r'<[^>]+>'
texto = "<div>Olá, mundo!</div>"
matches = re.findall(padrao, texto)
print(f"10. Tags HTML: {matches}")  # Deve imprimir: ['<div>', '</div>']

# 11. Correspondência de Espaços em Branco
padrao = r'\s'
texto = "O gato está na casa."
matches = re.findall(padrao, texto)
print(f"11. Espaços em branco: {matches}")  # Deve imprimir os espaços encontrados

# 12. Correspondência de Início e Fim de Linha
padrao_inicio = r'^Olá'
padrao_fim = r'mundo!$'
texto = "Olá, mundo!"
matches_inicio = re.findall(padrao_inicio, texto)
matches_fim = re.findall(padrao_fim, texto)
print(f"12. Início de linha: {matches_inicio}")  # Deve imprimir: ['Olá']
print(f"12. Fim de linha: {matches_fim}")  # Deve imprimir: ['mundo!']

# 13. Correspondência de Qualquer Caractere
padrao = r'.'
texto = "Gato"
matches = re.findall(padrao, texto)
print(f"13. Qualquer caractere: {matches}")  # Deve imprimir: ['G', 'a', 't', 'o']

# 14. Correspondência de Repetições Específicas
padrao = r'a{2,4}'
texto = "aaa aaaa aaaaa"
matches = re.findall(padrao, texto)
print(f"14. Repetições específicas: {matches}")  # Deve imprimir: ['aaa', 'aaaa', 'aaaa']

# 15. Correspondência de Alternativas
padrao = r'gato|cachorro'
texto = "Eu tenho um gato e um cachorro."
matches = re.findall(padrao, texto)
print(f"15. Alternativas: {matches}")  # Deve imprimir: ['gato', 'cachorro']
