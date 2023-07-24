from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class CrawlingSpider(CrawlSpider):
        name = "mycrawler" #identifier of this class:  scrapy crawl mycrawler
        allowed_domains = ["toscrape.com"] 
        start_urls = ["http://books.toscrape.com/"] #a base point to start from

        rules = (  #tuple of rules need a comma at the end 
                Rule(LinkExtractor(allow="catalogue/catagory")),
                Rule(LinkExtractor(allow="catalogue", deny="category"), callback="parse_item")
        )

        def parse_item(self, response):
            yield {
                  "title": response.css(".product_main h1::text").get(),
                  "price": response.css(".price_color::text").get(),
                  "availability": response.css(".availability::text")[1].get().replace("\n", "").strip()
                }