# ./venv/bin/python
# _*_ coding: utf-8 _*_
# @Time     : 2024/8/27 08:57
# @Author   : Perye (Pengyu) LI
# @FileName : ds_selection_chain.py
# @Software : PyCharm
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers.openai_functions import JsonOutputFunctionsParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI

from annexx.core.annexx_core import Annexx
from annexx.data_source.national_data import national_data_ds
from annexx.embedding import embed
from language_model import load_gpt_default


prompt_template = """
You are a data source manager tasked with selecting the appropriate data source.
You will be given a user question and a list of data tables from different data sources, 
and you should output the data source name that contains user required data.
User question: {user_question}
List of data tables:  {data_tables}. 
Given the following user request, respond with the data source name (not data table name) to use. 
Given the following user request, respond with the data source name (not data table name) to use. 
If no data table is related to the user question,
respond with FINISH.

You only need to output the data source name or FINISH, no need to say anything else.
"""


prompt = PromptTemplate(
    template=prompt_template,
    input_variables=['user_question', "data_tables"],
)

an = Annexx(
    data_sources=[national_data_ds],
    retriever=FAISS.from_texts([''], embedding=embed).as_retriever()
)


def load_ds_selection_chain(annexx_instance: Annexx):
    return (
        {'user_question': RunnablePassthrough(), 'data_tables': annexx_instance.retriever} |
        prompt
        | load_gpt_default()
    )
