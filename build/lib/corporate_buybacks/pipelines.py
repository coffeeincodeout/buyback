# -*- coding: utf-8 -*-
import psycopg2


# class CorporateBuybacksPipeline(object):

#     def open_spider(self, spider):
#         hostname = 'localhost'
#         username = 'dcarlo81'
#         password = '3251motifes6'  # your password
#         database = 'stock_buybacks'
#         self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
#         self.cur = self.connection.cursor()

#     def close_spider(self, spider):
#         self.cur.close()
#         self.connection.close()

#     def process_item(self, item, spider):
#         self.cur.execute(
#             "INSERT INTO buybacks_history(post_date, company, percent_of_shares, buyback_amount, offer_type, current_price, fifty_two_week_range) VALUES(%s,%s,%s,%s,%s,%s,%s)",
#             (item['date'],item['company'],item['percent_of_shares'],item['buyback_amount'],item['offer_type'],item['current_price'],item['week_range'])
#         )
#         self.connection.commit()
#         return item