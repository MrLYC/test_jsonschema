#!/usr/bin/env python
# encoding: utf-8

from jsonschema import Draft4Validator as Validator

from unittest import TestCase

from JsonSchema.schemas import Draft4 as Schemas


class TestPersonQuery(TestCase):
    def setUp(self):
        self.validator = Validator(Schemas.PersonQuery)

    def test_required(self):
        self.assertFalse(self.validator.is_valid({}))
        self.assertFalse(self.validator.is_valid({
            "from": "2014-11-10T09:00:00.0"}))
        self.assertTrue(self.validator.is_valid({
            "from": "2014-11-10T09:00:00.0",
            "till": "2014-11-10T11:00:00.0",
        }))
        self.assertFalse(self.validator.is_valid({
            "from": 1,
            "till": 2,
        }))

    def test_optional(self):
        basic_json = {
            "from": "2014-11-10T09:00:00.0",
            "till": "2014-11-10T11:00:00.0",
        }

        json_ = basic_json.copy()
        json_["start"] = 0
        self.assertTrue(self.validator.is_valid(json_))

        json_ = basic_json.copy()
        json_["start"] = -1
        self.assertFalse(self.validator.is_valid(json_))
