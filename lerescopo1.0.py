from PyPDF2 import PdfReader
import pandas as pd
import re

lista_das_normas = ["ISO", "ABNT", "ASTM", "IEC"]
dados = []

def pesquisa_norma():
    # padrao = r"([A-Z]+ [A-Z]+ [A-Z]+ [A-Z]+ \d+\-\d+ |[A-Z]+ [A-Z]+ [A-Z]+ \d+\-\d+ |[A-Z]+ [A-Z]+ \d+\-\d+ |[A-Z]+ \d+\-\d+ |[A-Z]+ [A-Z]+ [A-Z]+ [A-Z]+ \d+ |[A-Z]+ [A-Z]+ [A-Z]+ \d+ |[A-Z]+ [A-Z]+ \d+ |[A-Z]+ \d+ |\w+ \d+\-\d+ |\w+ \d+)"
    padrao = r"(" + "|".join(lista_das_normas) + r")"
    with open('CRL0495.pdf','rb') as f:
        pdf = PdfReader(f)
        num_pages = len(pdf.pages)
        # for tag in lista_das_normas:
        lines = []
        for page in pdf.pages:
            page_text = page.extract_text()
            lines += page_text.split('\n')
            print("Pegando linhas")

        for i, line in enumerate(lines):
            match = re.search(padrao, line)
            if match:
                palavra = match.group(1)
                print("Printando match.group",match.group)
                if i < len(lines) -1:
                    proxima_linha = lines[i + 1]
                    texto_completo = f"{line} {proxima_linha}"
                else:
                    texto_completo = line

                print('Palavra {} encontrada na linha: {}'.format(palavra, texto_completo))
                dados.append({'Indice': i, 'Texto Completo': texto_completo})

        df = pd.DataFrame(dados)
        df. drop_duplicates(inplace=True)
        df.to_excel('db_normasTeste.xlsx', index=False)
        print("Dados salvos com sucesso!")

pesquisa_norma()
