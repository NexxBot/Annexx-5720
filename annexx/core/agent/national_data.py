# ./venv/bin/python
# _*_ coding: utf-8 _*_
# @Time     : 2024/8/7 14:35
# @Author   : Perye (Pengyu) LI
# @FileName : national_data.py
# @Software : PyCharm
from logi_langchain_web.agents.agent_toolkits.national_data.base import create_national_data_agent
from logi_langchain_web.agents.agent_toolkits.national_data.toolkit import NationalDataToolkit
from logi_langchain_web.utilities.national_data import NationalStatisticsDataSource

from language_model import load_gpt_default


def create_from_data_source(data_source: NationalStatisticsDataSource):
    return create_national_data_agent(
        llm=load_gpt_default(),
        toolkit=NationalDataToolkit(national_data=data_source),
        verbose=True,
        max_iterations=30,
    )
