from PyPDF2 import PdfReader

def extrair_texto_pagina_1(nome_arquivo):
    with open(nome_arquivo, 'rb') as f:
        pdf = PdfReader(f)
        if len(pdf.pages) >= 1:
            primeira_pagina = pdf.pages[0]
            texto = primeira_pagina.extract_text()
            return texto
        else:
            return "O arquivo PDF está vazio ou não contém páginas."

# Usando a função
nome_arquivo = 'CRL0495.pdf'
texto_pagina_1 = extrair_texto_pagina_1(nome_arquivo)
print(texto_pagina_1)