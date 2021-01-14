# -*- coding: utf-8 -*-
import scrapy
from SpecDownloader.items import DownloadItem
from scrapy.utils.project import get_project_settings

class AutosarSpider(scrapy.Spider):
    name = 'Autosar'
    allowed_domains = ['www.autosar.org']
    settings = get_project_settings()

    if settings['AUTOSAR_VER'] == "4.4.0":
        start_urls = ['https://www.autosar.org/standards/classic-platform/classic-platform-440/']
    elif settings['AUTOSAR_VER'] == "R19-11":
        start_urls = ['https://www.autosar.org/nc/document-search/?tx_sysgsearch_pi1%5Bquery%5D=&tx_sysgsearch_pi1%5Bcategory%5D%5B126%5D=126&tx_sysgsearch_pi1%5Bwidget%5D=1&tx_sysgsearch_pi1%5Bpage%5D=2&tx_sysgsearch_pi1%5BshowAll%5D=1']
    else:
        start_urls = ['https://www.autosar.org/nc/document-search/?tx_sysgsearch_pi1%5Bquery%5D=&tx_sysgsearch_pi1%5Bcategory%5D%5B145%5D=145&tx_sysgsearch_pi1%5Bwidget%5D=1&tx_sysgsearch_pi1%5Bpage%5D=2&tx_sysgsearch_pi1%5BshowAll%5D=1']

    def parse(self, response):
        down_links = response.xpath("//@href").extract()
        # print(down_links)
        for link in down_links:
            item = DownloadItem()
            if link.endswith(".zip") or link.endswith(".pdf"):
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