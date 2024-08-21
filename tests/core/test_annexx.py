# ./venv/bin/python
# _*_ coding: utf-8 _*_
# @Time     : 2024/8/21 15:11
# @Author   : Perye (Pengyu) LI
# @FileName : test_annexx.py
from unittest import TestCase

from langchain_community.vectorstores import FAISS
from logi_langchain_web.utilities.national_data import NationalStatisticsDataSource, NationalDataTable

from annexx.core.annexx_core import Annexx
from annexx.data_source.national_data import national_data_ds
from annexx.embedding import embed


# @Software : PyCharm
class TestAnnexx(TestCase):
    def setUp(self):
        self.an = Annexx(
            data_sources=[national_data_ds],
            retriever=FAISS.from_texts([''], embedding=embed).as_retriever()
        )

    def test_retrieve_table(self):
        print(self.an.retrieve_data_table('CPI'))
