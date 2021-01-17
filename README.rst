==================
scrapy-jsonrpc-api
==================

scrapy-jsonrpc is an extension to control a running Scrapy web crawler via
JSON-RPC.

Installation
============

Install scrapy-jsonrpc using ``pip``::

    $ pip install scrapy-jsonrpc-api -i https://pypi.python.org/simple/


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
(by default, it will try to listen on port 6080),
and will log to the file specified in `JSONRPC_LOGFILE`_.

The endpoint for accessing the crawler object is::

    http://localhost:6080/crawler

The Api Response:
```text
[
    {
        "time()-engine.start_time": 4.3701982498168945,
        "engine.has_capacity()": false,
        "len(engine.downloader.active)": 10,
        "engine.scraper.is_idle()": false,
        "engine.spider.name": "zhihu",
        "engine.spider_is_idle(engine.spider)": false,
        "engine.slot.closing": false,
        "len(engine.slot.inprogress)": 29,
        "len(engine.slot.scheduler.dqs or [])": 0,
        "len(engine.slot.scheduler.mqs)": 1,
        "len(engine.scraper.slot.queue)": 0,
        "len(engine.scraper.slot.active)": 19,
        "engine.scraper.slot.active_size": 258036,
        "engine.scraper.slot.itemproc_size": 0,
        "engine.scraper.slot.needs_backout()": false
    },
    {
        "Request": "30 oldest: 3s ago",
        "TextResponse": "19 oldest: 3s ago",
        "TestSpider": "1 oldest: 4s ago"
    },
    {
        "log_count/INFO": 27,
        "start_time": "2021-01-17 10:39:02",
        "log_count/ERROR": 3,
        "scheduler/enqueued/memory": 35,
        "scheduler/enqueued": 35,
        "scheduler/dequeued/memory": 34,
        "scheduler/dequeued": 34,
        "downloader/request_count": 34,
        "downloader/request_method_count/GET": 34,
        "downloader/request_bytes": 28923,
        "downloader/response_count": 24,
        "downloader/response_status_count/200": 24,
        "downloader/response_bytes": 100766,
        "response_received_count": 24,
        "request_depth_max": 3,
        "item_scraped_count": 2
    }
]
```


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
