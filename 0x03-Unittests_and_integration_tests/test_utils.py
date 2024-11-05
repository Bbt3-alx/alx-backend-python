#!/usr/bin/env python3
"""Parametorize a unit test"""


import unittest
from parameterized import parameterized
from unittest.mock import Mock, patch, MagicMock
from utils import access_nested_map, get_json, memoize


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


class TestMemoize(unittest.TestCase):
    """Memoization test"""

    def test_memoize(self):
        """Tes memoize decorator"""

        class TestClass:
            """Class to Test memoize decorator"""

            def a_method(self):
                """only called once using assert_called_once."""
                return 42

            @memoize
            def a_property(self):
                """
                When calling twice, the correct result is returned
                """
                return self.a_method()

        test_instance = TestClass()
        test_instance.a_method = MagicMock(return_value=42)

        # First access: calls `a_method` and caches the result
        result_first_call = test_instance.a_property
        test_instance.a_method.assert_called_once()
        self.assertEqual(result_first_call, 42)

        # Second access: should return cached result, not `a_method`
        result_second_call = test_instance.a_property
        test_instance.a_method.assert_called_once()
        self.assertEqual(result_second_call, 42)


if __name__ == "__main__":
    unittest.main()
