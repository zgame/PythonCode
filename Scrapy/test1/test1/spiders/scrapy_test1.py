import scrapy


class ScrapyTest1Spider(scrapy.Spider):
    name = 'scrapy_test1'

    # allowed_domains = ["baidu.com"]
    start_urls = [
        "https://www.leisu.com/data/zuqiu"
    ]


    def parse(self, response):
        print("----------------------------------------")
        print(response.url)
        # print(response)
        print(response.xpath)
        # print(response.url.split("/")[-2])
        print("----------------------------------------")
        area_list = response.xpath('//div[@class="left-list"]/div[contains(@class,"item")]')#包含了热门赛事
        season_item = {}
        for area in area_list[1:]:
            print(area)
            area_name = area.xpath('./div[@class="title"]/span/text()').get()
            print(area_name)
            season_item[area_name] = area_name
        yield season_item
