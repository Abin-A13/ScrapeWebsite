from scrapy.utils.project import get_project_settings

from extensions import db
from model import Flat

from scrapy import signals
from scrapy.signalmanager import dispatcher
from scrapy.crawler import CrawlerRunner, CrawlerProcess

from spiders import FlatsSpider

results = []


def crawler_results(signal, sender, item, response, spider):
    results.append(item)


def crawl_flats():
    dispatcher.connect(crawler_results, signal=signals.item_scraped)

    process = CrawlerProcess(get_project_settings())
    process.crawl(FlatsSpider)
    process.start()

    for item in results:
        db.session.add(
            Flat(item.get('title'), item.get('image_url'))
        )
    db.session.commit()