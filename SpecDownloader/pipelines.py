# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.files import FilesPipeline
from urllib.parse import urlparse
from os.path import basename, dirname, join


class DownloadPipeline(FilesPipeline):
    # def process_item(self, item, spider):
    #     with open("my_meiju.txt",'a', encoding='utf8') as fp:
    #         print(item['name'])
    #         fp.writelines(item['name'] + '\n')

    def file_path(self, request, response=None, info=None):
        print("*****************" + request.url)
        path = urlparse(request.url).path
        return join(basename(dirname(path)), basename(path))
