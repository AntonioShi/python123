import scrapy

class baisibudejie(scrapy.Spider):
    name = "baisibudejie"

    def start_requests(self):
        urls = [
            'http://www.budejie.com/text/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        lies = response.css('div.j-r-list >ul >li')
        for li in lies:
            username = li.css('a.u-user-name::text').extract()
            content = li.css('div.j-r-list-c-desc a::text').extract()
            yield {'username': username, 'content': content}

        page = response.url.split("/")[-1]
        filename = 'user.json'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(filename)