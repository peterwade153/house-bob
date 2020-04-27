# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from word2number import w2n

class ScraperPipeline(object):
    def process_item(self, item, spider):
        item.save()
        return item


class PropertyStatusPipeline(object):
    def process_item(self, item, spider):
        if item.get('status'):
            item['status'] = item['status'].replace('For ', '')
            return item


class PropertyPricePipeline(object):
    def process_item(self, item, spider):
        if item.get('price'):
            item['price'] = item['price'].replace('/=', '')
            return item


class ConvertNumPipeline(object):
    def process_item(self, item, spider):
        if item.get('bathrooms'):
            item['bathrooms'] = w2n.word_to_num(item['bathrooms'])
        if item.get('bedrooms'):
            item['bedrooms'] = w2n.word_to_num(item['bedrooms'])
        return item
