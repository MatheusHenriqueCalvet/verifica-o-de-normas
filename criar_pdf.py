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

def cria_figura():
    cnv.setFillColor(colors.black)

def mp(mm):
    return mm/0.352777

def calcula_tamanho_string(texto, fonte, tamanho_fonte):
    cnv.setFont(fonte, tamanho_fonte)
    largura = cnv.stringWidth(texto, fonte, tamanho_fonte)
    cnv.save()
    return largura

def calcula_ponto_inicial(x_form, y_form, tamanho_string, fonte):
    x_centro = x_form / 2
    y_centro = y_form / 2
    return (x_centro - tamanho_string / 2), (y_centro - proporcao_fonte(fonte))

def proporcao_fonte(tamanho_fonte):
    #Para alinhar o texto com a figura, |-> cnv.drawString(x,  y + (y_centro - proporcao_fonte(tamanho_fonte) <-|
    return ((tamanho_fonte/72)* 25)

def cria_string(x, y, texto):
    pass

def cabecalho():
    num_total_pages = 1
    cnv.setFillColor(colors.white)
    cnv.rect(mp(10), mp(257), mp(50), mp(30), fill=True)
    cnv.rect(mp(60), mp(257), mp(140), mp(10), fill=True)
    cnv.rect(mp(60), mp(267), mp(140), mp(20), fill=True)
    img = utils.ImageReader("C:\\Users\\matheus.calvet\\Desktop\\testecriarpdfff\\testecriarpdf\\logo.png")
    x = mp(15)
    y = mp(260)
    cnv.drawImage(img, x, y, width=120, height=70, mask='auto')
    cnv.setFillColor(colors.black)
    cnv.setFont("Helvetica", 11)
    cnv.drawString(mp(62), mp(279), "SCiTec Soluções em Ensaios de Materiais e Produtos")
    texto = "SCiTec Soluções em Ensaios de Materiais e Produtos", "Helvetica"

    cnv.drawString(calcula_ponto_inicial(140, 20, 12), texto)

    cnv.setFont("Helvetica-Bold", 10)
    cnv.drawString(mp(80), mp(271), "LABORATÓRIO DE ENSAIOS SCITEC")
    cnv.setFont("Helvetica-Bold", 12)
    cnv.drawString(mp(65), mp(260), "Relatório de normas")

def criar_PDF():
    try:
        cabecalho()
        cria_figura()
        cnv.save()
    except:
        print("Erro ao criar pdf")
        return
    print("Pdf criado com sucesso!")


criar_PDF()