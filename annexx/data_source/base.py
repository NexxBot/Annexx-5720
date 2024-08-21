# ./venv/bin/python
# _*_ coding: utf-8 _*_
# @Time     : 2024/8/21 14:19
# @Author   : Perye (Pengyu) LI
# @FileName : base.py
# @Software : PyCharm

from typing import Optional

from pydantic.v1 import BaseModel


class AnnexxDataSource(BaseModel):
    url: Optional[str] = None


