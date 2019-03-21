import scrapy
from ..items import CorporateBuybacksItem


class BuyBacksSpider(scrapy.Spider):

    name = 'buys'
    start_urls = [
        # 'https://www.marketbeat.com/stock-buybacks/2019/',
        'https://www.marketbeat.com/stock-buybacks/2018/',
        'https://www.marketbeat.com/stock-buybacks/2017/',
        'https://www.marketbeat.com/stock-buybacks/2016/',
        'https://www.marketbeat.com/stock-buybacks/2015/',
        'https://www.marketbeat.com/stock-buybacks/2014/',
        'https://www.marketbeat.com/stock-buybacks/2013/',
        'https://www.marketbeat.com/stock-buybacks/2012/',
        'https://www.marketbeat.com/stock-buybacks/2011/',
        'https://www.marketbeat.com/stock-buybacks/2010/',
        'https://www.marketbeat.com/stock-buybacks/2009/',
    ]
    # change the file name of you plan to use flat storage
    # TMP_FILE = os.path.join(os.path.dirname(sys.modules['src'].__file__), 'tmp/buybacks.csv')
    # enter the field names below to format the output in your csv file
    FIELDS = [
        'date',
        'company',
        'percent_of_shares',
        'buyback_amount',
        'offer_type',
        'current_price',
        'week_range'
    ]
    # custom setting per spider if not needed then remove and adjust crawl in settings
    custom_settings = {
        # 'FEED_FORMAT': 'csv',
        # 'FEED_URI': TMP_FILE,
        # 'FEED_EXPORT_FIELDS': FIELDS,
        'DOWNLOAD_DELAY': 4,
        'CONCURRENT_REQUESTS': 3,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 3,
        'AUTOTHROTTLE_ENABLED': True,
        'AUTOTHROTTLE_START_DELAY': 4,
    }

    def parse(self, response):
        date_list = response.css('#ratingstable > tbody > tr > td:nth-child(1)::text').extract()
        company_list = response.css('#ratingstable > tbody > tr > td:nth-child(2)::text').re(r'[A-z].+[^\(]')
        shares_list = response.css('#ratingstable > tbody > tr > td:nth-child(3)::text').extract()
        amount_list = response.css('#ratingstable > tbody > tr > td:nth-child(4)::text').extract()
        offer_list = response.css('#ratingstable > tbody > tr > td:nth-child(5)::text').extract()
        price_list = response.css('#ratingstable > tbody > tr > td:nth-child(7)::text').extract()
        week_list = response.css('#ratingstable > tbody > tr > td:nth-child(8)::text').extract()

        for date_item, company_item, percent_of_shares_item, buyback_amount_item, offer_type_item, \
            current_price_item, week_range_item in zip(date_list, company_list, shares_list, amount_list,
                                                       offer_list, price_list, week_list):

            buybackItem = CorporateBuybacksItem(
                date=date_item.strip(),
                company=company_item.strip(),
                percent_of_shares=percent_of_shares_item.strip(),
                buyback_amount=buyback_amount_item.strip(),
                offer_type=offer_type_item.strip(),
                current_price=current_price_item.strip(),
                week_range=week_range_item.strip()
            )
            yield buybackItem
