# ./venv/bin/python
# _*_ coding: utf-8 _*_
# @Time     : 2024/8/21 14:38
# @Author   : Perye (Pengyu) LI
# @FileName : annexx_core.py
# @Software : PyCharm

from typing import Sequence, Dict, Optional

from langchain.agents import AgentExecutor
from langchain_core.retrievers import BaseRetriever
from logi_langchain.utilities.data_source import BaseDataSource, BaseDataTable
from pydantic.v1 import BaseModel, root_validator


class Annexx(BaseModel):
    data_sources: Sequence[BaseDataSource]
    _ds_dict: Dict[str, BaseDataSource]
    retriever: BaseRetriever

    class Config:
        arbitrary_types_allowed = True

    @root_validator(pre=False)
    def init_ds(cls, values):
        values['_ds_dict'] = {}
        for ds in values['data_sources']:
            values['_ds_dict'][ds.name] = ds
            values['retriever'].add_documents([
                table.document for table in ds.tables
            ])
        return values

    def retrieve_data_table(self, name: str) -> Sequence[BaseDataTable]:
        """retrieve table by name"""
        return [
            self._ds_dict[doc.metadata['data_source_name']].get_table(doc.metadata.get('name'))
            for doc in self.retriever.invoke(name) if 'data_source_name' in doc.metadata
        ]

    def get_data_source(self, name: str) -> Optional[BaseDataSource]:
        return self._ds_dict.get(name)

