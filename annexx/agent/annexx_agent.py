# ./venv/bin/python
# _*_ coding: utf-8 _*_
# @Time     : 2024/8/23 12:58
# @Author   : Perye (Pengyu) LI
# @FileName : annexx_agent.py
# @Software : PyCharm

from langchain_community.vectorstores import FAISS

from annexx.agent import create_agent_from_data_source
from annexx.agent.ds_selection_chain import load_ds_selection_chain
from annexx.core.annexx_core import Annexx
from annexx.data_source.national_data import national_data_ds
from annexx.embedding import embed

data_sources = [national_data_ds]

an = Annexx(
    data_sources=data_sources,
    retriever=FAISS.from_texts([''], embedding=embed).as_retriever()
)

agents = {ds.name: create_agent_from_data_source(ds) for ds in data_sources}

user_question = '北京4月份CPI是多少'
agents[load_ds_selection_chain(an).invoke(user_question)].invoke(user_question)

