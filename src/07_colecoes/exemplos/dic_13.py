usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}

# Interseção dos conjuntos usuarios_data_science e usuarios_machine_learning.
# Resultado: conjunto com os elementos comuns aos dois conjuntos (23 e 56).
print(usuarios_data_science & usuarios_machine_learning)

# Diferença dos conjuntos usuarios_data_science e usuarios_machine_learning.
# Resultado: conjunto com os elementos que estão em usuarios_data_science,
# mas não estão em usuarios_machine_learning (15 e 43).
print(usuarios_data_science - usuarios_machine_learning)

# Cria um novo conjunto chamado fez_ds_mas_nao_fez_ml contendo os elementos presentes em usuarios_data_science,
# mas não presentes em usuarios_machine_learning (15 e 43).
fez_ds_mas_nao_fez_ml = usuarios_data_science - usuarios_machine_learning
print(fez_ds_mas_nao_fez_ml)

# Verifica se o valor 15 está presente no conjunto fez_ds_mas_nao_fez_ml.
# Resultado: True, pois 15 está presente no conjunto fez_ds_mas_nao_fez_ml.
print(15 in fez_ds_mas_nao_fez_ml)

# Verifica se o valor 23 está presente no conjunto fez_ds_mas_nao_fez_ml.
# Resultado: False, pois 23 não está presente no conjunto fez_ds_mas_nao_fez_ml.
print(23 in fez_ds_mas_nao_fez_ml)

# Diferença simétrica dos conjuntos usuarios_data_science e usuarios_machine_learning.
# Resultado: conjunto com os elementos que estão em apenas um dos conjuntos, mas não em ambos (13, 15, 42, 43).
print(usuarios_data_science ^ usuarios_machine_learning)