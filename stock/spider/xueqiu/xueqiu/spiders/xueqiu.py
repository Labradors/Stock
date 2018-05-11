import scrapy

from spider.models import Quote


class DianPing(scrapy.Spider):
    name = 'xueqiu'
    count = 0
    start_urls = [
        "http://quotes.toscrape.com/tag/humor/",
    ]

    custom_settings = {
        'LOG_FILE': 'xueqiu.log',
    }
    save_dir = './xueqiu/'

    def parse(self, response):
        for quote in response.css('div.quote'):
            quote_data = Quote()
            quote_data.author = quote.xpath('span/small/text()').extract_first()
            quote_data.text = quote.css('span.text::text').extract_first()
            quote_data.save()
            return quote_data

        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
