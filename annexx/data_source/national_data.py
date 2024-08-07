# ./venv/bin/python
# _*_ coding: utf-8 _*_
# @Time     : 2024/8/7 14:22
# @Author   : Perye (Pengyu) LI
# @FileName : national_data.py
# @Software : PyCharm

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from logi_langchain_web.utilities.national_data import NationalData, NationalDataTable


def gdp_index_callback(wd: WebDriver):
    wd.find_element(By.CSS_SELECTOR, '#mySelect_zb > div.dtHtml').click()
    wd.find_element(By.CSS_SELECTOR,
                    '#mySelect_zb > div.dtHtml > div.dtBody > div.dtList > ul > li:nth-child(3)').click()


national_data_ds = NationalData(tables=[
    NationalDataTable(
        name="CPI_monthly_by_province",
        description="全国各省份每月居民消费价格指数(CPI)。",
        url="https://data.stats.gov.cn/easyquery.htm?cn=E0101"
    ),
    NationalDataTable(
        name="GDP_value_quarterly_by_province",
        description="全国各省份每季度地区生产总值(GDP)_累计值(亿元)",
        url="https://data.stats.gov.cn/easyquery.htm?cn=E0102"
    ),
    NationalDataTable(
        name="GDP_index_quarterly_by_province",
        description="全国各省份每季度地区生产总值指数(上年同期=100)_累计值(%)",
        url="https://data.stats.gov.cn/easyquery.htm?cn=E0102",
        wd_preprocess_callback=gdp_index_callback
    ),
])
