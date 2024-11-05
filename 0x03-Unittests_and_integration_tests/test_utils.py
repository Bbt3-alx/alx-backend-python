#!/usr/bin/env python3
"""Parametorize a unit test"""


import unittest
from parameterized import parameterized
from unittest.mock import Mock, patch, MagicMock
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """Test access nested map"""

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, nested_map, path, expected):
        """
        method to test that the method returns what it is supposed to.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([({}, ("a",)), ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        context manager to test that a KeyError is raised for the following
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Mock HTTP calls"""

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    @patch("utils.requests")
    def test_get_json(self, test_url, test_payload, mock_request):
        """Mock get_json to check response handling."""
        mock_response = MagicMock(status_code=200)
        mock_response.json.return_value = test_payload
        mock_request.get.return_value = mock_response
        self.assertEqual(get_json(test_url), test_payload)


if __name__ == "__main__":
    unittest.main()
