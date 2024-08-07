# ./venv/bin/python
# _*_ coding: utf-8 _*_
# @Time     : 2024/8/7 14:35
# @Author   : Perye (Pengyu) LI
# @FileName : national_data.py
# @Software : PyCharm

from logi_langchain_web.agents.agent_toolkits.national_data.base import create_national_data_agent
from logi_langchain_web.agents.agent_toolkits.national_data.toolkit import NationalDataToolkit

from annexx.data_source.national_data import national_data_ds
from language_model import load_gpt_4_turbo

agent = create_national_data_agent(
    llm=load_gpt_4_turbo(),
    toolkit=NationalDataToolkit(national_data=national_data_ds),
    verbose=True,
    max_iterations=30,
)

# agent.invoke({'input': '北京2024年第一季度GDP是多少，北京6月的CPI是多少'})
