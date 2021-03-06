#!/usr/bin/env python3
""" Unittest module """

from unittest import TestCase, mock
from unittest.mock import patch, Mock
from parameterized import parameterized

from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(TestCase):
    """ testing Nested Map function """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])

    def test_access_nested_map(self, map, path, expected_output):
        """ return correct output """
        real_output = access_nested_map(map, path)
        self.assertEqual(real_output, expected_output)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])

    def test_access_nested_map_exception(self, map, path, wrong_output):
        """ raise correct exception """
        with self.assertRaises(KeyError) as e:
            access_nested_map(map, path)
            self.assertEqual(wrong_output, e.exception)


class TestGetJson(TestCase):
    """ testing function """
    @parameterized.expand([
        (test_url="http://example.com", test_payload={"payload": True}),
        (test_url="http://holberton.io", test_payload={"payload": False})
    ])

    def TestGet_Json(self, test_url, test_payload):
        """ return output """
        res = Mock()
        res.json.return_value = test_payload
        with patch('requests.get', return_value=res):
            real_response = get_json(test_url)
            self.assertEqual(real_response, test_payload)
            res.json.assert_called_once()

