import re

lista = ["ABC", "ABNT", "TESTE"]

# Crie o padrão de regex usando a lista com opções
padrao = r"(" + "|".join(lista) + r")"

# Exemplo de uso:
texto = "ABC ABNT TESTE XYZ"
correspondencias = re.findall(padrao, texto)

print(correspondencias)