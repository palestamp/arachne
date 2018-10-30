from html import escape
from typing import Any

import jmespath
import ujson

class JmespathResolver:
    def resolve(self, definition: Any, data: dict) -> Any:
        return jmespath.search(definition, data)


class Response:
    def __init__(self, json, failed=False, resolver=None):
        self.json = json
        self.failed = failed
        self._resolver = resolver or JmespathResolver()

    def resolve(self, definition: Any) -> Any:
        return self._resolver.resolve(definition, self.json)


def ujson_loads(data):
    return ujson.loads(data)


def success(data):
    return Response(data, failed=False)


def failure(data):
    return Response(data, failed=True)


async def from_aiohttp(response, json_only=True):
    obj = None
    failed = False

    if response.status > 400:
        failed = True
        obj = {
            "error": escape(await response.text()),
            "code": response.status
        }

    try:
        obj = await response.json(loads=ujson_loads)
    except Exception as e:
        if json_only:
            failed = True
        obj = {"text": str(e)}

    return Response(json=obj, failed=failed)
