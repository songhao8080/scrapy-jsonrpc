import json
from time import time

from scrapy.utils.engine import get_engine_status
from twisted.web import resource
from scrapy.utils.trackref import format_live_refs, NoneType, live_refs


class JsonResource(resource.Resource):
    json_encoder = json.JSONEncoder()

    def render(self, txrequest):
        r = resource.Resource.render(self, txrequest)
        return self.render_object(r, txrequest)

    def render_object(self, obj, txrequest):
        # 获取引擎状态
        ext = format_engine_status_test(obj.engine)
        # 获取各个排列状态
        refs = format_live_refs_test()
        # 获取所有统计信息：
        stats = obj.stats.get_stats()
        # fix encode error
        stats_str = {}
        for k, v in stats.items():
            stats_str[k.decode()] = v.decode()
        list_data = [ext, refs, stats_str]
        r = self.json_encoder.encode(list_data)
        sb = bytes(r, encoding="utf8")
        txrequest.setHeader('Content-Type', 'application/json')
        txrequest.setHeader('Access-Control-Allow-Origin', '*')
        txrequest.setHeader('Access-Control-Allow-Methods', 'GET, POST, PATCH, PUT, DELETE')
        txrequest.setHeader('Access-Control-Allow-Headers', 'X-Requested-With')
        txrequest.setHeader('Content-Length', str(len(sb)))
        return sb

def format_live_refs_test(ignore=NoneType):
    now = time()
    map = {}
    for cls, wdict in sorted(live_refs.items(),
                             key=lambda x: x[0].__name__):
        if not wdict:
            continue
        if issubclass(cls, ignore):
            continue
        oldest = min(wdict.values())
        s = f"{len(wdict)} oldest: {int(now - oldest)}s ago"
        map[cls.__name__] = s
    return map


def format_engine_status_test(engine=None):
    checks = get_engine_status(engine)
    map = {}
    for test, result in checks:
        map[test] = result

    return map
