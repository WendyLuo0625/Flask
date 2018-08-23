# -*- coding=utf-8 -*-

import scrapy

class ShiyanlouGithubSpider(scrapy.Spider):
    name = "shiyanlou-github"

    @property
    def start_urls(self):
        url_tmpl="https://github.com/shiyanlou?page={}&tab=repositories"
        return (url_tmpl.format(i) for i in range(1, 5))

    def parse(self, response):
        for course in response.xpath('//div[@id="user-repositories-list"]/ul/li'):
            yield{
                "name":course.xpath('.//div[contains(@class,"d-inline-block")]/h3/a/text()').extract_first().strip(),
                "update_time": course.xpath('.//div[contains(@class,"text-gray")]/relative-time/@datetime').extract_first()
                 }


