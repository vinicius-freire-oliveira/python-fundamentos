# Definição da classe Circulo
class Circulo:

    # Método estático que retorna o valor de PI
    @staticmethod
    def obter_pi():
        return 3.14 

# Chama o método estático obter_pi da classe Circulo e imprime o valor retornado
print(Circulo.obter_pi())

# Definição da classe Circulo com um atributo estático
class Circulo:
    # Atributo estático que representa o valor de PI
    PI = 3.14

# Acessa e imprime o valor do atributo estático PI da classe Circulo
print(Circulo.PI)
