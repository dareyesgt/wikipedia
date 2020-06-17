# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup
from wikipedia.items import WikipediaItem
import re
import nltk


class PagesSpider(CrawlSpider):
    """
    the Page Spider for wikipedia
    """

    name = "wiki"
    allowed_domains = ["wikipedia.org"]

    start_urls = [
        "https://en.wikipedia.org/wiki/Wikipedia:Featured_articles"
    ]

    rules = (
        Rule(LinkExtractor(allow="https://en\.wikipedia\.org/wiki/.+_.+",
                           deny=[
                               "https://en\.wikipedia\.org/wiki/Wikipedia.*",
                               "https://en\.wikipedia\.org/wiki/Main_Page",
                               "https://en\.wikipedia\.org/wiki/Free_Content",
                               "https://en\.wikipedia\.org/wiki/Talk.*",
                               "https://en\.wikipedia\.org/wiki/Portal.*",
                               "https://en\.wikipedia\.org/wiki/Special.*"
                               "https://en\.wikipedia\.org/wiki/Template.*"
                           ]),
             callback='parse_wikipedia_page