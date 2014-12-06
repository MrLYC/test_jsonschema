#!/usr/bin/env python
# encoding: utf-8


class Draft4(object):
    PersonQuery = {
        "properties": {
            "from": {"type": "string"},
            "till": {"type": "string"},
            "start": {
                "type": "integer",
                "minimum": 0
            },
            "limit": {
                "type": "integer",
                "minimum": 0
            },
            "filter": {
                "anyOf": ["type", "name", "age"]
            },
            "output": {
                "oneOf": [
                    {"anyOf": ["type", "name", "age"]},
                    "all"
                ]
            },
        },
        "required": ["from", "till"]
    }
