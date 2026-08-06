""" Importado o módulo "array" com o alias "arr". Em seguida, é criado um array do tipo "d" (double/float) com os elementos [1, 3.5]. No entanto, essa linha não possui uma atribuição, então o array é criado, mas não é salvo em nenhuma variável, portanto, não será exibido na saída. """
import array as arr

# Criado um array do tipo "d" (double/float) com os elementos [1, 3.5]. Essa linha não possui uma atribuição, então o array é criado, mas não é salvo em nenhuma variável, portanto, não será exibido na saída.
arr.array('d', [1, 3.5])

# Esse array causará um erro, pois o tipo "d" suporta apenas valores numéricos, e a string 'Guilherme' não é um valor numérico. Se essa linha for executada, um TypeError será gerado.
# arr.array('d', [1, 3.5, 'Guilherme'])

#!pip install numpy # instalar o pacote NumPy 

# NumPy é importado com o alias "np".
import numpy as np

# É criado um array NumPy chamado "numeros" contendo os elementos [1, 3.5], e em seguida, ele é impresso na tela.
numeros = np.array([1, 3.5])
print(numeros)

print(numeros + 3)