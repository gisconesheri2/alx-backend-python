import unittest
from unittest.mock import patch, Mock, PropertyMock
from client import GithubOrgClient
from parameterized import parameterized, param, parameterized_class
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Test Github orgclient"""

    @parameterized.expand([
        ('google', {'status': 'OK'}),
        ('abc', {'status': 'OK'})
    ])
    @patch('client.get_json')
    def test_org(self, com, resp, mock_get_json):
        """Test org method"""
        org1 = GithubOrgClient(com)

        mock_get_json.return_value = resp
        self.assertEqual(org1.org, resp)
        org1.org
        mock_get_json.assert_called_once()

    def test_public_repos_url(self):
        """How to mock a read only property"""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mk:
            mk.return_value = {'repos_url': "a good url"}
            gc_org = GithubOrgClient('google')
            url = gc_org._public_repos_url
            self.assertEqual(url, "a good url")

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """test public repos"""

        mock_get_json.return_value = [{'name': 'repo1'}]
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mk:
            mk.return_value = "a valid url"
            gc_org = GithubOrgClient('test')
            res = gc_org.public_repos()
            self.assertEqual(res, ['repo1'])
            gc_org.public_repos()

            mock_get_json.assert_called_once()
            mk.assert_called_once()

    @parameterized.expand([
      param(repo={"license": {"key": "my_license"}},
            license_key="my_license", resp=True),
      param(repo={"license": {"key": "other_license"}},
            license_key="my_license", resp=False),
    ])
    def test_has_license(self, repo, license_key, resp):
        """Test for has_licence method"""
        gh_clt = GithubOrgClient('test')
        self.assertEqual(gh_clt.has_license(repo,
                                            license_key), resp)


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Intergration tests"""

    @classmethod
    def setUpClass(cls):
        """Set up requests.mock tests"""

        config = {'return_value.json.side_effect':
                  [
                      cls.org_payload, cls.repos_payload,
                      cls.org_payload, cls.repos_payload
                  ]
                  }
        cls.get_patcher = patch('requests.get', **config)
        cls.mock = cls.get_patcher.start()

    def test_public_repos(self):
        """ test for public repos"""
        tst_cls = GithubOrgClient("google")

        self.assertEqual(tst_cls.org, self.org_payload)
        self.assertEqual(tst_cls.repos_payload, self.repos_payload)
        self.assertEqual(tst_cls.public_repos(), self.expected_repos)
        self.assertEqual(tst_cls.public_repos("NOLICENCE"), [])

    def test_public_repos_with_license(self):
        """ test for repos with License """
        tst_cls = GithubOrgClient("google")

        self.assertEqual(tst_cls.public_repos(
            "apache-2.0"), self.apache2_repos)

    @classmethod
    def tearDownClass(cls):
        """stop the requests.get patch"""
        cls.get_patcher.stop()
