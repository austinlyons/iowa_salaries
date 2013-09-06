#!/usr/bin/env python
# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class IowaSalaryItem(Item):
    year = Field()
    salary = Field()
    employee = Field()
    department = Field()
    position = Field()
    county = Field()
    sex = Field()
    base_salary = Field()
    extra_money = Field()
