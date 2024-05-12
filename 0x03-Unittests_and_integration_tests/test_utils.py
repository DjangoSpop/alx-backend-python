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
    @mock.patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test that utils.get_json returns the expected result."""
        mock_get.return_value.json.return_value = test_payload

        response = utils.get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(response, test_payload)
        
    