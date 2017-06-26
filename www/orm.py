#!/usr/bin/env python3
# -*- coding: utf8 -*-

import asyncio
import aiomysql
import logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(name)s:%(levelnane)s: %(message)s'))

__author__ = 'hg'

def log(sql, args=()):
    logging.info('SQL: %s' % sql)


# 创建一个数据库连接池，么个http请求都从池中获得数据库链接
async def create_pool(loop, **kw):

