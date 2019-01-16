# -*- coding: utf-8 -*-
import scrapy
from SpecDownloader.items import DownloadItem
from bs4 import BeautifulSoup


class AutosarSpider(scrapy.Spider):
    name = 'Autosar'
    allowed_domains = ['www.autosar.org']
    start_urls = ['https://www.autosar.org/standards/classic-platform/classic-platform-440/']

    def parse(self, response):
        down_links = response.xpath("//*[@id='c677']/div//*[@class='ce-bodytext']/p//@href").extract()
        # print(down_links)
        for link in down_links:
            item = DownloadItem()
            item['file_urls'] = ['https://www.autosar.org/' + link]
            print(item['file_urls'])
            yield item

    def closed(self, reason):
        # from scrapy.mail import MailSender
        
        # mailer = MailSender()
        
        # body = 'AUTOSAR 文档已经下载完成'
        # subject = 'AUTOSAR文件下载完成'
        # mailer.send(to=["xxx@xxx.com"], subject = subject, body = body)
        return