# Scrapy settings for iowa_salaries project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#


# To export to a CSV: scrapy crawl iowa_salaries --set FEED_URI=items.csv --set FEED_FORMAT=csv
BOT_NAME = 'iowa_salaries'

SPIDER_MODULES = ['iowa_salaries.spiders']
NEWSPIDER_MODULE = 'iowa_salaries.spiders'
#ITEM_PIPELINES = [
#    'iowa_salaries.pipelines.iowa_salaries_pipeline'
#]


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'iowa_salaries (+http://www.yourdomainhere.com)'

# Crawl responsibly by adding some delay
DOWNLOAD_DELAY = 0.25
RANDOMIZE_DOWNLOAD_DELAY = True
