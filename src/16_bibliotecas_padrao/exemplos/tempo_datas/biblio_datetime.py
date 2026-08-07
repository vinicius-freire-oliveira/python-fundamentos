import datetime  # Importa o módulo 'datetime' que fornece classes para manipulação de datas e horas

# Cria um objeto de data específico (ano, mês, dia)
data = datetime.date(2023, 3, 28)  
print(data)  # Imprime a data no formato padrão AAAA-MM-DD

# Converte a data para uma string com a representação legível por humanos
print(data.ctime())  

# Substitui o dia da data original por 2, criando um novo objeto de data
nova_data = data.replace(day=2)  
print(nova_data)  # Imprime a nova data com o dia alterado

# Obtém a data atual
hoje = datetime.date.today()  
print(hoje)  # Imprime a data atual

# Calcula a diferença entre a data atual e a data especificada
delta = hoje - data  
print(delta)  # Imprime a diferença em dias
print(type(data))  # Imprime o tipo do objeto 'data' (datetime.date)

# Adiciona a diferença (delta) à data original, criando uma nova data
nova_data = data + delta  
print(nova_data)  # Imprime a nova data resultante

# Cria um objeto de hora específico (hora, minuto, segundo)
hora = datetime.time(11, 55, 15)  
print(hora.hour)  # Imprime a hora (11)
print(hora.minute)  # Imprime os minutos (55)
print(hora.second)  # Imprime os segundos (15)
# Imprime a hora completa no formato HH:MM:SS
print(hora.hour, ":", hora.minute, ":", hora.second)  

# Cria um objeto de data e hora específico (ano, mês, dia, hora, minuto)
data = datetime.datetime(2023, 3, 28, 11, 55)  
print(data)  # Imprime a data e hora no formato padrão AAAA-MM-DD HH:MM:SS

# Obtém a data e hora atuais
agora = datetime.datetime.now()  
print(agora)  # Imprime a data e hora atuais

# Formata a data e hora atuais em uma string personalizada
agora_string = agora.strftime("%A %d %B %y %I:%M")  
print(agora_string)  # Imprime a data e hora formatadas

# Converte a string formatada de volta para um objeto datetime
agora_datetime = datetime.datetime.strptime(agora_string, "%A %d %B %y %I:%M")  
print(agora_datetime)  # Imprime o objeto datetime criado a partir da string
