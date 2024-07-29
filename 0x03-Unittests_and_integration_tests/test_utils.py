#!/usr/bin/env python3
"""Test module for utility functions."""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Tests for access_nested_map function."""

    @parameterized.expand([
        ({"x": 5}, ("x",), 5),
        ({"x": {"y": 10}}, ("x",), {"y": 10}),
        ({"x": {"y": 10}}, ("x", "y"), 10)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map returns correct values."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("x",), "x"),
        ({"x": 5}, ("x", "y"), "y")
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_exception):
        """Test access_nested_map raises KeyError with correct message."""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), f"'{expected_exception}'")


class TestGetJson(unittest.TestCase):
    """Tests for get_json function."""

    @parameterized.expand([
        ("http://api.example.com", {"status": "ok"}),
        ("http://api.github.com", {"status": "error"})
    ])
    def test_get_json(self, url, expected_json):
        """Test get_json returns correct JSON data."""
        mock_response = Mock()
        mock_response.json.return_value = expected_json
        with patch('requests.get', return_value=mock_response) as mock_get:
            result = get_json(url)
            self.assertEqual(result, expected_json)
            mock_get.assert_called_once_with(url)


class TestMemoize(unittest.TestCase):
    """Tests for memoize decorator."""

    def test_memoize(self):
        """Test memoize caches method result."""
        class TestClass:
            def regular_method(self):
                return 100

            @memoize
            def memoized_method(self):
                return self.regular_method()

        with patch.object(TestClass, 'regular_method', return_value=100) as mock_method:
            test_instance = TestClass()
            self.assertEqual(test_instance.memoized_method(), 100)
            self.assertEqual(test_instance.memoized_method(), 100)
            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
