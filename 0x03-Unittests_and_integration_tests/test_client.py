#!/usr/bin/env python3
'''Module to test utils file
'''
from parameterized import parameterized
import unittest
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch
from github_org_client import GithubOrgClient


class TestAccessNestedMap(unittest.TestCase):
    '''class for testing access_nestd_map function
    '''

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Test that the method returns what it is supposed to
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """ Test that a KeyError is raised for the respective inputs """
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
        self.assertEqual(f"KeyError('{expected}')", repr(e.exception))


class TestGetJson(unittest.TestCase):
    """ Class for Testing Get Json """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """ Test for the utils.get_json function to check
        that it returns the expected result."""
        config = {'return_value.json.return_value': test_payload}
        patcher = patch('requests.get', **config)
        mock = patcher.start()
        self.assertEqual(get_json(test_url), test_payload)
        mock.assert_called_once()
        patcher.stop()


class TestGithubOrgClient(unittest.TestCase):
    """Class for testing GithubOrgClient"""
    
    def setUp(self):
        """Set up the test case"""
        self.org_name = "test_org"
        self.client = GithubOrgClient(self.org_name)
        
    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    def test_public_repos_url(self, org_name):
        """Test that the result of _public_repos_url is the expected one"""
        mocked_payload = {"repos_url": f"https://api.github.com/orgs/{org_name}/repos"}
        
        with patch.object(GithubOrgClient, "org", return_value=mocked_payload):
            expected_url = f"https://api.github.com/orgs/{org_name}/repos"
            result_url = self.client._public_repos_url
            self.assertEqual(result_url, expected_url)
# ....
    