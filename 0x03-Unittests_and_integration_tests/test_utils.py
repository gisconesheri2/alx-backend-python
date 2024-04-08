#!/usr/bin/env python3
"""Test Util methods"""
import unittest
from unittest.mock import MagicMock, patch
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized, param


class TestAccessNestedMap(unittest.TestCase):
    """
    Test Util methods
    """

    @parameterized.expand([
        param(nested_map={"a": 1}, path=("a",), result=1),
        param(nested_map={"a": {"b": 2}}, path=("a",), result={'b': 2}),
        param(nested_map={"a": {"b": 2}}, path=("a", "b"), result=2)
    ])
    def test_access_nested_map(self, nested_map, path, result):
        """Test access nested map method"""
        self.assertEqual(access_nested_map(nested_map, path), result)

    @parameterized.expand([
        param(nested_map={}, path=("a",), result='a'),
        param(nested_map={"a": 1}, path=("a", "b"), result='b'),
    ])
    def test_access_nested_map_exception(self, nested_map, path, result):
        """test exception raised"""
        with self.assertRaises(KeyError) as exc:
            access_nested_map(nested_map, path)

        exp_msg = exc.exception
        self.assertEqual(exp_msg.args[0], result)


class TestGetJson(unittest.TestCase):
    """Test get JSON response"""

    @parameterized.expand([
        param(test_url="http://example.com", test_payload={"payload": True}),
        param(test_url="http://holberton.io", test_payload={"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """Test requests get method"""
        config = {'return_value.json.return_value': test_payload}
        patcher = patch('requests.get', **config)
        mock = patcher.start()

        self.assertEqual(get_json(test_url), test_payload)
        mock.assert_called_once()
        patcher.stop()


class TestMemoize(unittest.TestCase):
    """Test memoize"""

    def test_memoize(self):
        """test for memoization"""

        class TestClass:
            """A test class for the memoization function"""

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mk:
            t_cls = TestClass()
            t_cls.a_property
            t_cls.a_property
            mk.assert_called_once()
