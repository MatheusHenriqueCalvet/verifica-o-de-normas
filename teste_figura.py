from reportlab.pdfgen import canvas as reportlab_canvas
from reportlab.lib import utils
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Preformatted
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import datetime
import os

pastaApp = os.path.dirname(__file__)
cnv = reportlab_canvas.Canvas(pastaApp+"\\teste.pdf", pagesize=A4)
data_atual = datetime.date.today()
data_formatada = data_atual.strftime('%d/%m/%Y')

def mp(mm):
    return mm/0.352777
try:
    cnv.setFont("Helvetica", 12)
    texto = "TESteçp"
    texto1 = "teste"
    cnv.setFillColor(colors.black)
    
    x_cord = 100
    y_cord = 100

    recX_width = 100
    recY_height = 50
  
    largura = cnv.stringWidth(texto, "Helvetica", 12)

    x_centro = recX_width / 2
    y_centro = recY_height / 2
    metade_largura = largura / 2

    print("Tamanho do x_centro: {} ".format(x_centro))
    print("Tamanho do y_centro: {} ".format(y_centro))
    print("Tamanho do metade_largura: {} ".format(metade_largura))
    print("Tamanho do largura: {} ".format(largura))

    aux = largura - x_centro

    metade_retangulo = recX_width / 2

    cnv.rect(x_cord, y_cord, recX_width, recY_height)
    cnv.drawString(x_cord + (x_centro - metade_largura),  y_cord + (y_centro - ((12/72) *25)), texto)
    cnv.save()
except:
    print("Erro ao criar pdf")
print("Pdf criado com sucesso!")



    