from datetime import datetime  # Importa a classe 'datetime' do módulo 'datetime'
import math  # Importa o módulo 'math' para operações matemáticas

def calculate_time_since_start_of_year():
    # Obtém a data e hora atuais
    today = datetime.today()
    
    # Define o início do ano atual
    start_of_year = datetime(today.year, 1, 1)
    
    # Calcula a diferença em dias entre a data atual e o início do ano
    delta_days = (today - start_of_year).days
    
    # Calcula a diferença em semanas
    delta_weeks = delta_days / 7
    
    # Calcula a diferença em meses (aproximado como 30.44 dias por mês)
    delta_months = delta_days / 30.44
    
    # Retorna as diferenças em dias, semanas e meses
    return delta_days, delta_weeks, delta_months

def main():
    # Chama a função para calcular o tempo desde o início do ano e obtém os resultados
    delta_days, delta_weeks, delta_months = calculate_time_since_start_of_year()
    
    # Imprime os resultados
    print(f"Desde o início do ano até hoje, passaram-se:")
    print(f"{delta_days} dias")
    # Imprime o número de semanas completas e os dias restantes
    print(f"{math.floor(delta_weeks)} semanas e {delta_days % 7} dias")
    # Imprime o número de meses completos e os dias restantes
    print(f"{math.floor(delta_months)} meses e {math.floor((delta_months - math.floor(delta_months)) * 30.44)} dias")

if __name__ == "__main__":
    # Verifica se o script está sendo executado diretamente (não importado como módulo)
    main()  # Chama a função principal
