#!/usr/bin/env python3
"""Unittests for GithubOrgClient"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from github_org_client import GithubOrgClient
from fixtures import (
    TEST_PAYLOAD,
    EXPECTED_REPOS,
    EXPECTED_APACHE_REPOS,
)

class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient class"""

    @parameterized.expand([
        ("google", TEST_PAYLOAD),
        ("abc", TEST_PAYLOAD),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, expected_payload, mock_get_json):
        """Test GithubOrgClient.org returns the correct value"""
        mock_get_json.return_value = expected_payload
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, expected_payload)
        mock_get_json.assert_called_once_with(f'https://api.github.com/orgs/{org_name}')

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """Test GithubOrgClient._public_repos_url"""
        mock_org.return_value = {'repos_url': 'https://api.github.com/orgs/org_name/repos'}
        client = GithubOrgClient('org_name')
        expected_url = 'https://api.github.com/orgs/org_name/repos'
        self.assertEqual(client._public_repos_url, expected_url)

    @patch('client.get_json')
    @patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock)
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """Test GithubOrgClient.public_repos"""
        mock_public_repos_url.return_value = 'https://api.github.com/org/repos'
        mock_get_json.return_value = EXPECTED_REPOS
        client = GithubOrgClient('org_name')
        self.assertEqual(client.public_repos(), ['repo_1', 'repo_2'])
        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """Test GithubOrgClient.has_license"""
        client = GithubOrgClient('org_name')
        self.assertEqual(client.has_license(repo, license_key), expected_result)

@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    [
        (TEST_PAYLOAD, EXPECTED_REPOS, EXPECTED_REPOS, EXPECTED_APACHE_REPOS),
    ],
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """TestIntegrationGithubOrgClient class"""

    @classmethod
    def setUpClass(cls):
        """Set up class fixtures before running tests"""
        cls.get_patcher = patch('utils.requests.get')
        cls.mock_get = cls.get_patcher.start()
        options = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }
        cls.mock_get.side_effect = lambda url: options.get(url)

    @classmethod
    def tearDownClass(cls):
        """Stop the patcher"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Integration test for GithubOrgClient.public_repos"""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Integration test for GithubOrgClient.public_repos with license"""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(license="apache-2.0"), self.apache2_repos)

if __name__ == '__main__':
    unittest.main()