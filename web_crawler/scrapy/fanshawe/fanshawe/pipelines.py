# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

from urllib.parse import quote_plus
from scrapy.utils.project import get_project_settings
from scrapy.exceptions import DropItem


class MongoPipeline(object):

    def __init__(self):
        setting = get_project_settings()
        url = "mongodb://%s:%s@%s:%s" % (quote_plus(setting['MONGODB_USER']), quote_plus(setting['MONGODB_PASS']), setting['MONGODB_SERVER'], setting['MONGODB_PORT'])
        connection = pymongo.MongoClient(url)
        db=connection[setting['MONGODB_DB']]
        self.collection=db[setting['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        valid=True
        for data in item:
            if not data:
                valid=False
                raise DropItem("Missing {0}".format(data))
        if valid:
            self.collection.insert(dict(item))
        return item
