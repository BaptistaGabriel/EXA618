import urllib.request
from urllib.parse import urljoin
from bs4 import BeautifulSoup

def processar_estudantes():
    dados_extraidos = []
    seeds_path = 'seeds.txt'

    with open(seeds_path, 'r', encoding='utf-8') as f:
        urls = [linha.strip() for linha in f if linha.strip()]

    for url in urls:
        page = urllib.request.urlopen(url)
        html_content = page.read().decode('utf-8')
        soup = BeautifulSoup(html_content, 'lxml')

        titulo = soup.title.string.strip() if soup.title else "Estudante sem título"

        img_tag = soup.find('img')
        src_relativo = img_tag.attrs.get("src") if img_tag else None
        
        src_absoluto = None
        if src_relativo:
            src_absoluto = urljoin(url, src_relativo)

        dados_extraidos.append({
            'titulo': titulo,
            'imagem': src_absoluto,
            'url_origem': url
        })
        print(f"Ok: {titulo}")

    gerar_html_saida(dados_extraidos)

def gerar_html_saida(dados):
    html_template = """
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <title>Relatório de Estudantes</title>
    </head>
    <body>
        <h1>Lista de Estudantes</h1>
        {conteudo}
    </body>
    </html>
    """
    
    itens_html = ""
    for item in dados:
        if item["imagem"]:
            img_tag = f'<img src="{item["imagem"]}" width="150">'
        else:
            img_tag = '<p>(Sem imagem disponível)</p>'
            
        itens_html += f"""
        <hr>
        <h2>{item['titulo']}</h2>
        {img_tag}
        <p>Fonte: {item['url_origem']}</p>
        """

    final_html = html_template.format(conteudo=itens_html)

    nome_arquivo = 'resultado_estudantes.html'
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        f.write(final_html)
    
    print("\n FINALIZADO")

if __name__ == "__main__":
    processar_estudantes()