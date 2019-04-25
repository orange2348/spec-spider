# -*- coding: utf-8 -*-
import scrapy
from SpecDownloader.items import DownloadItem
from bs4 import BeautifulSoup


class EthSpecSpider(scrapy.Spider):
    name = 'EthSpec'
    allowed_domains = ['www.opensig.org']
    start_urls = ['http://www.opensig.org/Automotive-Ethernet-Specifications/']

    def parse(self, response):
        down_links = response.xpath("//div/div/article/ul/li//@href").extract()
        # print(down_links)
        for link in down_links:
            item = DownloadItem()
            item['file_urls'] = ['https://www.opensig.org/' + link]
            print(item['file_urls'])
            yield item

    def closed(self, reason):
        # from scrapy.mail import MailSender
        
        # mailer = MailSender()
        
        # body = 'ETH spec 文档已经下载完成'
        # subject = 'Eth spec 文件下载完成'
        # mailer.send(to=["xxx@xxx.com"], subject = subject, body = body)
        return
