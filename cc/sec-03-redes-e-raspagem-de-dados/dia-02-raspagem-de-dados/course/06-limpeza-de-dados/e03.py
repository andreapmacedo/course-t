from parsel import Selector
import requests


URL_BASE = "http://books.toscrape.com/catalogue/"
# Define a primeira página como próxima a ter seu conteúdo recuperado
next_page_url = 'page-1.html'
while next_page_url:
    # Busca o conteúdo da próxima página
    response = requests.get(URL_BASE + next_page_url)
    selector = Selector(text=response.text)
    # Imprime os produtos de uma determinada página
    for product in selector.css(".product_pod"):
        # Busca e extrai o título e  o preço
        title = product.css("h3 a::attr(title)").get()
        price = product.css(".product_price .price_color::text").re(r"£\d+\.\d{2}")
        print(title, price)

        # Busca o detalhe de um produto
        detail_href = product.css("h3 a::attr(href)").get()
        detail_page_url = URL_BASE + detail_href

        # Baixa o conteúdo da página de detalhes
        detail_response = requests.get(detail_page_url)
        detail_selector = Selector(text=detail_response.text)

        # Extrai a descrição do produto
        description = detail_selector.css("#product_description ~ p::text").get()
        suffix = "...more"
        if description.endswith(suffix):
            description = description[:-len(suffix)]
        print(description)

    # Descobre qual é a próxima página
    next_page_url = selector.css(".next a::attr(href)").get()


# # Recupera o primeiro elemento
# [1, 2, 3][0]  # Saída: 1

# # Quando não incluso o valor inicial, iniciaremos do índice 0
# # e do índice 2 em diante, os elementos não são incluídos
# (1, 2, 3, 4)[:2]  # Saída: (1, 2)

# # Quando omitimos o valor final
# # o fatiamento ocorre até o fim da sequência
# (1, 2, 3, 4)[1:]  # Saída: (2, 3, 4)

# # Vá do índice 3 até o 7.
# # O item no índice 7 não é incluído
# "palavra"[3:7]  # Saída: "avra"

# # Começando do elemento de índice 1, vá até o último,
# # saltando de 2 em 2
# [1, 2, 3, 4][1::2]  # Saída: [2, 4]

# À partir da versão 3.9 do Python, teremos uma função chamada removesuffix, que é equivalente à palavra[:-len(suffix)].