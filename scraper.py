import scrapy


class QuoteSpider(scrapy.Spider):
    name = 'quote-spider'
    start_urls = ['https://quotes.toscrape.com']

    def parse(self, response):
        QUOTE_SELECTOR = '.quote'
        TEXT_SELECTOR = '.text::text'
        AUTHOR_SELECTOR = '.author::text'
        ABOUT_SELECTOR = '.author + a::attr("href")'
        TAGS_SELECTOR = '.tags > .tag::text'
        
        for quote in response.css(QUOTE_SELECTOR):
            yield {
                'text': quote.css(TEXT_SELECTOR).extract_first(),  #큰 quote 박스 내부에 있는 저자 이름 추출
                'author': quote.css(AUTHOR_SELECTOR).extract_first(),
                'about': 'https://quotes.toscrape.com' + 
                        quote.css(ABOUT_SELECTOR).extract_first(),
                'tags': quote.css(TAGS_SELECTOR).extract(),
            }