# ./venv/bin/python
# _*_ coding: utf-8 _*_
# @Time     : 2024/8/27 15:15
# @Author   : Perye (Pengyu) LI
# @FileName : test_ds_selection_chain.py
from unittest import TestCase

from langchain_community.vectorstores import FAISS

from annexx.agent.ds_selection_chain import load_ds_selection_chain
from annexx.core.annexx_core import Annexx
from annexx.data_source.national_data import national_data_ds
from annexx.embedding import embed


# @Software : PyCharm
class Test(TestCase):

    def setUp(self) -> None:
        self.an = Annexx(
            data_sources=[national_data_ds],
            retriever=FAISS.from_texts([''], embedding=embed).as_retriever()
        )

    def test_load_ds_selection_chain(self):
        print(load_ds_selection_chain(self.an).invoke('北京4月份CPI是多少'))
