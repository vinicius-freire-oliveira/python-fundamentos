# Importa o módulo pytz para lidar com fusos horários
import pytz
# Importa a classe datetime do módulo datetime para manipulação de datas e horas
from datetime import datetime

# Função para obter a hora atual em um fuso horário específico
def get_current_time_in_timezone(timezone_str):
    """
    Retorna a hora atual em um fuso horário específico.
    """
    try:
        # Obtém o fuso horário a partir da string fornecida
        timezone = pytz.timezone(timezone_str)
        # Obtém a hora atual no fuso horário especificado
        current_time = datetime.now(timezone)
        # Retorna a hora atual formatada como string
        return current_time.strftime('%Y-%m-%d %H:%M:%S')
    except Exception as e:
        # Retorna a mensagem de erro em caso de exceção
        return str(e)

# Função para converter a hora de um fuso horário para outro
def convert_time_between_timezones(time_str, from_timezone_str, to_timezone_str):
    """
    Converte a hora de um fuso horário para outro.
    """
    try:
        # Obtém os fusos horários de origem e destino a partir das strings fornecidas
        from_timezone = pytz.timezone(from_timezone_str)
        to_timezone = pytz.timezone(to_timezone_str)
        
        # Converte a string de hora fornecida para um objeto datetime
        naive_time = datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
        
        # Localiza a hora no fuso horário de origem
        localized_time = from_timezone.localize(naive_time)
        
        # Converte a hora para o fuso horário de destino
        converted_time = localized_time.astimezone(to_timezone)
        
        # Retorna a hora convertida formatada como string
        return converted_time.strftime('%Y-%m-%d %H:%M:%S')
    except Exception as e:
        # Retorna a mensagem de erro em caso de exceção
        return str(e)

# Função principal que gerencia a entrada do usuário e chama as funções apropriadas
def main():
    print("=== Calcular Fusos Horários ===")
    
    # Obter a hora atual em um fuso horário específico
    timezone_str = input("Digite o fuso horário (exemplo: 'America/Sao_Paulo'): ")
    current_time = get_current_time_in_timezone(timezone_str)
    print(f"A hora atual em {timezone_str} é {current_time}")
    
    # Converter a hora de um fuso horário para outro
    time_str = input("Digite a hora no formato 'YYYY-MM-DD HH:MM:SS' (exemplo: '2023-06-04 15:30:00'): ")
    from_timezone_str = input("Digite o fuso horário de origem (exemplo: 'America/Sao_Paulo'): ")
    to_timezone_str = input("Digite o fuso horário de destino (exemplo: 'Europe/London'): ")
    converted_time = convert_time_between_timezones(time_str, from_timezone_str, to_timezone_str)
    print(f"A hora convertida de {from_timezone_str} para {to_timezone_str} é {converted_time}")

# Executa a função principal se o script for executado diretamente
if __name__ == "__main__":
    main()
