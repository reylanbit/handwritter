import os
import requests
import textwrap
import random
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor

# Configurações globais
FONT_FILENAME = 'Caveat-Handwriting.ttf'
PDF_FILENAME = 'redacao_manuscrita.pdf'
# URL de um repositório bower que contém a versão estática TTF (mais garantido que baixar do repo principal que usa VF)
FONT_URL = "https://github.com/google-fonts-bower/caveat-bower/raw/master/Caveat-Regular.ttf"

def download_font():
    """Baixa a fonte Caveat se ela não existir localmente."""
    if not os.path.exists(FONT_FILENAME):
        print(f"Baixando a fonte '{FONT_FILENAME}' do Google Fonts...")
        try:
            response = requests.get(FONT_URL)
            response.raise_for_status()
            with open(FONT_FILENAME, 'wb') as f:
                f.write(response.content)
            print("Download da fonte concluído com sucesso.")
        except Exception as e:
            print(f"Erro ao baixar a fonte: {e}")
            print("Por favor, baixe manualmente 'Caveat-Regular.ttf' e renomeie para 'Caveat-Handwriting.ttf'.")
            return None
    return FONT_FILENAME

def draw_ruled_paper(c, width, height):
    """Desenha linhas horizontais azuis claras para simular papel pautado."""
    line_color = HexColor('#ADD8E6')  # Azul claro
    c.setStrokeColor(line_color)
    c.setLineWidth(0.5)
    
    # Começa as linhas de cima para baixo
    y = 810
    while y > 40:
        c.line(40, y, width - 40, y)
        y -= 24  # Espaçamento entre linhas de caderno comum

def generate_pdf():
    # 1. Preparar fonte
    font_path = download_font()
    if not font_path:
        return

    try:
        pdfmetrics.registerFont(TTFont('Handwriting', font_path))
    except Exception as e:
        print(f"Erro ao registrar a fonte: {e}")
        return

    # 2. Criar Canvas
    c = canvas.Canvas(PDF_FILENAME, pagesize=A4)
    width, height = A4
    
    # 3. Desenhar papel pautado
    draw_ruled_paper(c, width, height)
    
    # 4. Configurar estilo da "caneta"
    # Azul Bic/esferográfica mais realista
    blue_ink = HexColor('#112266') 
    c.setFillColor(blue_ink)
    c.setFillAlpha(0.9) # Leve transparência para simular a pressão da tinta no papel
    font_size = 15
    c.setFont('Handwriting', font_size)

    # 5. Conteúdo da redação
    texto_completo = """O profissional de TI e o fantasma na fibra ótica – um solilóquio sobre a juventude e as redes sociais

Eis a questão, nobres leitores, que atravessa minhas noites de plantão em datacenters: ser ou não ser online? Eis o dilema cruel da juventude atual – e o meu também. Pois sou profissional de TI; meu sangue é café, minha respiração é SSH, meu afeto por um grep bem escrito é mais puro que o amor de Romeu por Julieta. Sem tecnologia, eu não existo. Sou um kernel panic ambulante. E no entanto, vejo os jovens – e a mim mesmo – definharem diante das telas.

Observai a cena contemporânea: um jovem está ali, polegar deslizando sem fim. Ele sorri para a tela, mas seus olhos estão vazios como o vazio entre estrelas. Publica uma foto com filtro e parece um deus; mas quando o telefone se apaga, ele é apenas um espectro de si mesmo. Cada like é um grilhão dourado. Cada story, uma máscara de carne sorridente. E eu, que programo bancos de dados, sei bem o que está por trás: vocês não são os usuários. Vocês são o produto. Seu comportamento, suas lágrimas, suas meia-noites sem sono – tudo vira INSERT INTO tabela_vazio VALUES ('desespero', 1);

A ansiedade cresce como um fork() sem wait(): multiplica, multiplica até explodir. A capacidade de estar só? Morreu: segmentation fault (core dumped). O silêncio? 404 not found. Antigamente, Hamlet gritava "Morrer, dormir, dormir, talvez sonhar". Agora os jovens nem dormem. Sonham acordados, com os olhos grudados em telas. Perderam o gosto da carne, o toque do amigo, o silêncio que cura. Trocam o teatro da vida pelo teatro da vitrine.

Mas quem sou eu para julgar, sendo eu o arquiteto das correntes? Eu construo as pontes para eles se afogarem. Eu otimizo os bancos de dados para que as algemas do like nunca travem. Eu reinicio servidores às 3 da manhã para que ninguém perca um segundo da novela das ilusões. E por quê? Porque eu também sou fraco. Porque quando fecho o laptop, o vazio sibila. Porque eu também já fui jovem e troquei o beijo pelo bit.

Eis então o drama final, cruel e sem vilão fantasmagórico: o fantasma está dentro de nós. O algoritmo é só um espelho. A juventude dança como marionetes de fibra ótica. E eu, que sei tudo isso, não consigo desligar o roteador de casa. Não consigo. Porque do outro lado do ping... há alguém. E mesmo que seja apenas mais um like... é a única coisa que ainda parece real.

Portanto, profissionais de TI, jovens, príncipes da Dinamarca digital: a questão não é largar a tecnologia. Isso seria hipocrisia minha. A questão é saber que estamos ambos – criadores e consumidores – dentro da mesma ratoeira. E o primeiro passo para não ser totalmente devorado é, pelo menos, reconhecer o monstro. Dar um Ctrl+C no silêncio. Olhar para o rosto sem filtro do outro. E talvez, só talvez, descobrir que ser offline por cinco minutos não é um kernel panic. É apenas respirar."""

    # 6. Renderizar texto com simulação manual
    x_margin = 55
    y_pos = 786  # Alinhado com as linhas do papel
    line_height = 24
    chars_per_line = 70

    paragrafos = texto_completo.split('\n\n')
    
    for i, paragrafo in enumerate(paragrafos):
        # Quebra automática respeitando largura
        linhas = textwrap.wrap(paragrafo.strip(), width=chars_per_line)
        
        for j, linha in enumerate(linhas):
            if y_pos < 60:
                c.showPage()
                draw_ruled_paper(c, width, height)
                c.setFillColor(blue_ink)
                c.setFillAlpha(0.9)
                c.setFont('Handwriting', font_size)
                y_pos = 786

            # Indentação no início do parágrafo
            indent = 35 if j == 0 else 0
            
            # Simulação manual: Pequeno deslocamento aleatório
            # jitter_y ajustado para a letra "sentar" na linha azul
            jitter_x = random.uniform(-1, 1)
            jitter_y = random.uniform(1.5, 2.5) 
            
            c.drawString(x_margin + indent + jitter_x, y_pos + jitter_y, linha)
            y_pos -= line_height
        
        # Removemos o meio-espaço que causava o desalinhamento progressivo
        # Se quiser um espaço entre parágrafos, pularia uma linha inteira (24pt)
        # Mas em redações escolares, costuma-se apenas indentar a primeira linha.

    # 7. Adicionar uma "rasura" ou assinatura estilizada no final
    if y_pos > 100:
        y_pos -= 20
        c.setFont('Handwriting', 18)
        c.drawString(x_margin + 200, y_pos, "Assinado: O Fantasma na Fibra")
        
        # Uma pequena rasura (um risco embaixo de uma palavra imaginária)
        c.setLineWidth(1)
        c.line(x_margin + 200, y_pos - 2, x_margin + 350, y_pos + 2)

    c.save()
    print(f"\nPDF '{PDF_FILENAME}' gerado com sucesso!")
    print("O arquivo parece uma redação escolar com fundo pautado e tinta azul.")

if __name__ == "__main__":
    generate_pdf()
