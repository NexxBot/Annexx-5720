# ./venv/bin/python
# _*_ coding: utf-8 _*_
# @Time     : 2024/8/7 14:21
# @Author   : Perye (Pengyu) LI
# @FileName : __init__.py.py
# @Software : PyCharm

from logi_langchain.utilities.data_source import BaseDataSource
from logi_langchain_web.utilities.national_data import NationalStatisticsDataSource

from annexx.core.agent import national_data
from annexx.data_source.national_data import national_data_ds

_DS_AGENT_MAPPING = {
    NationalStatisticsDataSource: national_data.create_from_data_source,
    BaseDataSource: national_data.create_from_data_source,
}


def create_agent_from_data_source(data_source: BaseDataSource):
    return _DS_AGENT_MAPPING[data_source.__class__](data_source)

