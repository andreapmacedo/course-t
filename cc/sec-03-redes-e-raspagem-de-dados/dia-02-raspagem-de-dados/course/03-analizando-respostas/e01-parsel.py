from parsel import Selector
import requests


response = requests.get("http://books.toscrape.com/")
selector = Selector(text=response.text)
# print(selector)


# print(selector.css("img.thumbnail").getall()[0])

# for thumbnail in selector.css("img.thumbnail").getall():
#     print(thumbnail)

# for thumbnail in selector.css("img.thumbnail"):
#     print(thumbnail.css("::attr(src)").get())

# print(selector.css("div.image_container a").get())
# print(selector.css("div.image_container a::attr(href)").get())
# print(selector.css("div.image_container a::attr(href)").getall())

# thumb_url = selector.css("div.image_container a::attr(href)").get()
# thumbnail_requests = requests.get("http://books.toscrape.com/" + thumb_url)
# thumbnail_selector = Selector(text=thumbnail_requests.text)
# book_title = thumbnail_selector.css("div.product_main h1")
# print(book_title)


thumb_url_selector = selector.css("div.image_container a::attr(href)")
for url in (thumb_url_selector).getall():
    thumbnail_requests = requests.get("http://books.toscrape.com/" + url)
    thumbnail_selector = Selector(text=thumbnail_requests.text)
    book_title = thumbnail_selector.css("div.product_main h1")
    print(book_title.get())
  


# O título está no atributo title em um elemento âncora (<a>)
# Dentro de um h3 em elementos que possuem classe product_pod
titles = selector.css(".product_pod h3 a::attr(title)").getall()
# print(titles)
# Estamos utilizando a::attr(title) para capturar somente o valor contido no texto do seletor
