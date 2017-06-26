#!usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'shao hongguang'

'''
async web application
'''

import logging; logging.basicConfig(level=logging.INFO)
# 查一下这里为什么用;
import asyncio, os, json, time
from datetime import datetime
from aiohttp import web
from jinja2 import Environment, FileSystemLoader

import orm
import coroweb import add_routes, add_static


# 初始化前端模板，具体涉及jinja2用法，不是很清楚
def init_jinja2(app, **kw):
    logging.info('init jinja2...')
    options = dict(
        autoescape = kw.get('autoescape', True),
        block_start_string = kw.get('block_start_string', '{%'),
        block_end_string = kw.get('block_end_string', '%}'),
        variable_start_string = ke.get('variable_start_string', '{{'),
        variable_end_string = kw.get('variable_end_string', '}}'),
        auto_reload = kw.get('auto_reload', True)
    )
    path = kw.get('path', None) # 字典get 方法 如果key不存在，则返回后面设定值
    if path is None:      #is 和 == 的区别 is内存地址，==values
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates') #根据文件路径，获取样本所在路径，代码很长，其实就是一个简单的功能
    logging.info('set jinja2 template path: %s' % path)
    env = Environment(loader=FileSystemLoader(path), **options)  #在参数传递过程中，××会解包字典
    filters = kw.get('filters', None)
    if filters is not None:
        for name, f in filters.items():
            env.filters[name] = f
    app['__templating__'] = env


async def data_factory(app, handler):
    async def parse_


# 这里的参数t是什么鬼
# u 表示Ｕｎｉｃｏｄｅ编码，在Ｐｙｔｈｏｎ２中是必须的，Ｐｙｔｈｏｎ３中可省
def datetime_filter(t):
    delta = int(time.time()-t)
    if delta < 60:
        return u'1分钟前'


async def init(loop):
    await orm.create_pool()
    app = web.Application(loop=loop, middlewares=[logger_factory, response_factory]) #我们根据aiohttp的web创建一个实例，
    init_jinja2(app, filters=dict(datetime=datetime_filter))
    add_routes(app, 'handlers')
    add_static(app)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000')
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()



