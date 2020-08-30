# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import pymysql
result_path = './result.csv'

# CREATE TABLE `douban_movie` (
#   `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
#   `title` varchar(40) NOT NULL,
#   `category` varchar(40) NOT NULL,
#   `show_date` varchar(40) NOT NULL,
#   PRIMARY KEY (`id`)
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 |
#

#已新建好了表
class ScrapySpiderPipeline:


    def open_spider(self, spider):
        # self.csv_file = open(result_path, 'w')
        # self.csv_write = csv.writer(self.csv_file)
        # self.csv_write.writerow(['title', 'show_date', 'category'])
        try:
            self.con = pymysql.connect('localhost', 'root', '123', 'scrapy_spider', charset='utf8')
        except Exception as e:
            print("con db error")

    def close_spider(self, spider):
        self.con.close()

    def process_item(self, item, spider):
        # 写入csv 文件
        # 如果中途宕机 如何恢复
        insert_sql_format = 'insert into douban_movie (title, category, show_date) values ("{}" ,"{}", "{}")'
        insert_sql = insert_sql_format.format(item['name'], item['categroy'], item['show_date'])
        cur = self.con.cursor()
        try:
            cur.execute(insert_sql)
            cur.close()
        except Exception as e:
            print(e)
        return item
