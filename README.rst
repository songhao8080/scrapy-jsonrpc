==================
scrapy-jsonrpc-api-py3
==================

scrapy-jsonrpc is an extension to control a running Scrapy web crawler via
JSON-RPC.

Installation
============

Install scrapy-jsonrpc using ``pip``::

    $ pip install scrapy-jsonrpc-api-py3 -i https://pypi.python.org/simple/


Configuration
=============

First, you need to include the entension to your ``EXTENSIONS`` dict in
``settings.py``, for example::

    EXTENSIONS = {
        'scrapy_jsonrpc.webservice.WebService': 500,
    }

Then, you need to enable the extension with the `JSONRPC_ENABLED`_ setting,
set to ``True``.



The web server will listen on a port specified in `JSONRPC_PORT`_
(by default, it will try to listen on port 6023),
and will log to the file specified in `JSONRPC_LOGFILE`_.
eg ::
    EXTENSIONS = {
        'scrapy_jsonrpc.webservice.WebService': 500,
    }
    JSONRPC_HOST = "0.0.0.0"
    JSONRPC_ENABLED = True
    JSONRPC_PORT = [6023,6025]



The endpoint for accessing the crawler object is::

    http://localhost:6023/crawler

The Api Response::


    [
        {
            "engine.has_capacity()": false,
            "engine.scraper.is_idle()": false,
            "engine.scraper.slot.active_size": 0,
            "engine.scraper.slot.itemproc_size": 0,
            "engine.scraper.slot.needs_backout()": false,
            "engine.slot.closing": false,
            "engine.spider.name": "myspider_redis",
            "engine.spider_is_idle(engine.spider)": true,
            "len(engine.downloader.active)": 0,
            "len(engine.scraper.slot.active)": 0,
            "len(engine.scraper.slot.queue)": 0,
            "len(engine.slot.inprogress)": 0,
            "len(engine.slot.scheduler.dqs or [])": "AttributeError (exception)",
            "len(engine.slot.scheduler.mqs)": "AttributeError (exception)",
            "time()-engine.start_time": 57.646450996398926
        },
        {
            "MySpider1": "1 oldest: 58s ago"
        },
        {
            "downloader/request_bytes": "272",
            "downloader/request_count": "2",
            "downloader/request_method_count/GET": "2",
            "downloader/response_bytes": "41687",
            "downloader/response_count": "1",
            "downloader/response_status_count/200": "1",
            "elapsed_time_seconds": "574.571709",
            "finish_reason": "shutdown",
            "finish_time": "1649382464.844018",
            "httpcompression/response_bytes": "246926",
            "httpcompression/response_count": "1",
            "item_scraped_count": "1",
            "log_count/CRITICAL": "8",
            "log_count/DEBUG": "3",
            "log_count/ERROR": "6",
            "log_count/INFO": "155",
            "memusage/max": "102772736",
            "memusage/startup": "76910592",
            "response_received_count": "1",
            "scheduler/dequeued/redis": "2",
            "scheduler/enqueued/redis": "2",
            "start_time": "1649382467.72047"
        }
    ]




Settings
========

These are the settings that control the web service behaviour:

JSONRPC_ENABLED
---------------

Default: ``False``

A boolean which specifies if the web service will be enabled (provided its
extension is also enabled).

JSONRPC_LOGFILE
---------------

Default: ``None``

A file to use for logging HTTP requests made to the web service. If unset web
the log is sent to standard scrapy log.

JSONRPC_PORT
------------

Default: ``[6080, 7030]``

The port range to use for the web service. If set to ``None`` or ``0``, a
dynamically assigned port is used.

JSONRPC_HOST
------------

Default: ``'127.0.0.1'``

The interface the web service should listen on.

.. _JSON-RPC 2.0: http://www.jsonrpc.org/
