from reportlab.pdfgen import canvas as reportlab_canvas

class drawtexto:

    def __init__(self, texto, fonte, tamanho_fonte):
        self.cnv = reportlab_canvas.Canvas()
        self.texto = texto
        self.fonte = fonte
        self.tamanho_fonte = tamanho_fonte

    def calcula_largura(self, texto, fonte, tamanho_fonte):
        return self.cnv.stringWidth(texto, fonte, tamanho_fonte)
    
    def calcula_altura(self, tamanho_fonte):
        return (tamanho_fonte/72) * 25

    def calcula_ponto_inicial(self, width_figura, height_figura, x_cord, y_cord):
        return ((width_figura / 2) - (self.calcula_largura(self.texto, self.fonte, self.tamanho_fonte) / 2)) + x_cord, (height_figura / 2) - (self.calcula_altura(self.fonte)) + y_cord

    def cria_string_livre(self, x, y):
        return self.cnv.drawString(x, y, self.texto)
    
    def cria_string_infigura(self, width_figura, height_figura, x_cord, y_cord):
        valor1, valor2 = self.calcula_ponto_inicial(width_figura, height_figura, x_cord, y_cord)
        return self.cnv.drawString(valor1, valor2, self.texto)
        
    
