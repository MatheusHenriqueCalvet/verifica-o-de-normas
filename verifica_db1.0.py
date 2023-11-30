import re

# Lista de strings do banco de dados
normas = [
    "ABNT NBR 12642 - Água - Determinação de cianeto total - Métodos colorimétrico e titulométrico",
    "ABNT NBR 13934 - Água - Determinação de ferro - Método colorimétrico da ortofenantrolina",
    "ABNT NBR 13736 - Água - Determinação de alcalinidade - Métodos potenciométrico e titulométrico",
    "ISO 1443 - Meat and meat products - Determination of total fat content",
    "ISO 7932:2004 - Microbiology of food and animal feeding stuffs — Horizontal method for the enumeration of presumptive Bacillus cereus — Colony-count technique at 30 degrees C",
    "ISO 4833-1 - Microbiology of the food chain — Horizontal method for the enumeration of microorganisms — Part 1: Colony count at 30 °C by the pour plate technique",
    "ABNT NBR 15747 - Sistemas solares térmicos e seus componentes - Coletores solares Parte 1: Requisitos gerais",
    "ABNT NBR IEC 60529 - Graus de proteção para invólucros de equipamentos elétricos (código IP)",
    "ABNT NBR IEC 15747 - Sistemas solares térmicos e seus componentes - Coletores solares Parte 1: Requisitos gerais",
    "ABNT NBR ISO 7206-6 - Implantes para cirurgia - Próteses parcial e total de articulação de quadril. Parte 6: Determinação de propriedades de fadiga da região de colo de hastes femorais"
]

# Expressão regular para extrair o tipo de norma e o número dela
# padrao = r"([A-Z]+ [A-Z]+ \d+\-\d+|[A-Z]+ [A-Z]+ [A-Z]+ \d+\-\d+|[A-Z]+ [A-Z]+ [A-Z]+ [A-Z]+ \d+\-\d+|[A-Z]+ [A-Z]+ [A-Z]+ [A-Z]+ \d+\-\d+|\w+ \d+\-\d+|\w+ \d+)"
padrao = r"([A-Z]+ [A-Z]+ [A-Z]+ [A-Z]+ \d+\-\d+ |[A-Z]+ [A-Z]+ [A-Z]+ \d+\-\d+ |[A-Z]+ [A-Z]+ \d+\-\d+ |[A-Z]+ \d+\-\d+ |[A-Z]+ [A-Z]+ [A-Z]+ [A-Z]+ \d+ |[A-Z]+ [A-Z]+ [A-Z]+ \d+ |[A-Z]+ [A-Z]+ \d+ |[A-Z]+ \d+ |\w+ \d+\-\d+ |\w+ \d+)"

for norma in normas:
    # Procurar padrão na string
    resultado = re.search(padrao, norma)
    
    # Se encontrar o padrão, imprimir tipo de norma e número
    if resultado:
        tipo_norma = resultado.group(1)
        # descricao = resultado.group(2)
        # , Descrição: {descricao}
        print(f"Norma resumida: {tipo_norma}")
    else:
        print("Padrão não encontrado para:", norma)