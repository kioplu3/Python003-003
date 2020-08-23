# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv

result_path = './result.csv'


class ScrapySpiderPipeline:
    def open_spider(self, spider):
        self.csv_file = open(result_path, 'w')
        self.csv_write = csv.writer(self.csv_file)
        self.csv_write.writerow(['title', 'show_date', 'category'])

    def close_spider(self, spider):
        self.csv_file.close()

    def process_item(self, item, spider):
        # 写入csv 文件
        # 如果中途宕机 如何恢复
        self.csv_write.writerow([item['name'], item['categroy'], item['show_date']])
        return item
