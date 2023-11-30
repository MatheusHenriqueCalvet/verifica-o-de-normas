from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def create_pdf(file_path, text):
    # Cria um arquivo PDF na página tamanho "letter"
    c = canvas.Canvas(file_path, pagesize=letter)

    # Obtém as dimensões da página
    width, height = letter

    # Define a fonte e o tamanho do texto
    font_name = "Helvetica"
    font_size = 12
    c.setFont(font_name, font_size)

    # Mede a largura e altura do texto
    text_width = c.stringWidth(text, font_name, font_size)
    text_height = c.getFont().getAscent()

    # Calcula as coordenadas para centralizar o texto na página
    x = (width - text_width) / 2
    y = (height - text_height) / 2

    # Desenha o texto no centro da página
    c.drawText(x, y, text)

    # Salva o arquivo PDF
    c.save()

if __name__ == "__main__":
    file_path = "output.pdf"
    text = "Centralizado"

    create_pdf(file_path, text)
    print(f"PDF criado com sucesso em: {file_path}")