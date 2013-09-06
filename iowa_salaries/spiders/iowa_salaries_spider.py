#!/usr/bin/env python
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from iowa_salaries.items import IowaSalaryItem

def _select_data(r, xpath):
    '''Return the first element if it exists, else return None'''
    data = r.select(xpath).extract()
    return data[0] if data else None

class iowa_salaries_spider(BaseSpider):
    name = "iowa_salaries"
    allowed_domains = ["desmoinesregister.com"]
    start_urls = \
        ["http://data.desmoinesregister.com/dmr/dmr-public-records/state_salaries.php?BRSR=%s" 
            % i for i in range(0, 443700, 100)]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        items = []
        rows = hxs.select("//tr[@class='tr0' or @class='tr1']")
        for r in rows:
            year = _select_data(r, "td[1]/a/text()")
            salary = _select_data(r, "td[2]/text()")
            employee = _select_data(r, "td[3]/a/text()")
            department = _select_data(r, "td[4]/a/text()")
            position = _select_data(r, "td[5]/text()")
            county = _select_data(r, "td[6]/text()")
            sex = _select_data(r, "td[7]/text()")
            base_salary = _select_data(r, "td[8]/text()")
            extra_money = _select_data(r, "td[9]/text()")
            #print "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % (year, salary, employee, department, position, county, sex, base_salary, extra_money)

            if employee:
                item = IowaSalaryItem()
                item['year'] = year
                item['salary'] = salary
                item['employee'] = employee
                item['department'] = department
                item['position'] = position
                item['county'] = county
                item['sex'] = sex
                item['base_salary'] = base_salary
                item['extra_money'] = extra_money
                items.append(item)

        return items
