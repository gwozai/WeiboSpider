# -*- coding: utf-8 -*-
# @Author  : CharesFuns
# @Time    : 2021/7/23 15:34
# @Function:

from WeiboSpider.pipelines.base import Pipeline


class ErrorPipeline(Pipeline):
    def __init__(self, db_connector):
        super(ErrorPipeline, self).__init__(db_connector)

    def process_item(self, item, spider):
        pass
