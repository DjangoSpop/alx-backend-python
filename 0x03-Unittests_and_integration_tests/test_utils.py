#!/usr/bin/env python3
"""module to make unit testing"""
import unittest
from parameterized import parameterized
from utils import access_nested_map

class TestAccessNestedMap(unittest.TestCase):
    """_summary_

    Args:
        unittest (_type_): _description_
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """_summary_

        Args:
            nested_map (_type_): _description_
            path (_type_): _description_
            expected_result (_type_): _description_
        """      
     
        self.assertEqual(access_nested_map(nested_map, path), expected_result)
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), repr(path[-1]))
    
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_access_nested_map_exception(self, url, payload):
        """_summary_

        Args:
            url (_type_): _description_
            payload (_type_): _description_
        """
        with self.assertRaises(KeyError) as cm:
            access_nested_map(payload, url)
        self.assertEqual(str(cm.exception), repr(url))
    class TestAccessNestedMap(TestGetJson):
        @parameterized.expand([
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
        def test_access_nested_map(self, nested_map, path, expected_result):
            self.assertEqual(access_nested_map(nested_map, path), expected_result)
            with self.assertRaises(KeyError) as cm:
                access_nested_map(nested_map, path)
            self.assertEqual(str(cm.exception), repr(path[-1]))

        @parameterized.expand([
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False})
        ])
        def test_access_nested_map_exception(self, url, payload):
            with self.assertRaises(KeyError) as cm:
                access_nested_map(payload, url)
            self.assertEqual(str(cm.exception), repr(url))import unittest
from parameterized import parameterized
from utils import access_nested_map

class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        self.assertEqual(access_nested_map(nested_map, path), expected_result)
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), repr(path[-1]))

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_access_nested_map_exception(self, url, payload):
        with self.assertRaises(KeyError) as cm:
            access_nested_map(payload, url)
            self.assertEqual(str(cm.exception), repr(url))