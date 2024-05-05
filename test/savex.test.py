import unittest
from savex.main import file_filter


class TestFileFilter(unittest.TestCase):
    def test_sanitize_file_name(self):
        # Test valid file name
        valid_file = MockFile("image.jpg")
        self.assertEqual(file_filter(valid_file), "image.jpg")

        # Test invalid characters
        invalid_file = MockFile("image$%.jpg")
        self.assertFalse(file_filter(invalid_file))

        # Test multiple consecutive dots
        consecutive_dots_file = MockFile("image...jpg")
        self.assertEqual(file_filter(consecutive_dots_file), "image.jpg")

        # Test multiple consecutive spaces
        consecutive_spaces_file = MockFile("image  file.jpg")
        self.assertEqual(file_filter(
            consecutive_spaces_file), "image file.jpg")

        # Test path traversal attempt
        path_traversal_file = MockFile("../../image.jpg")
        self.assertFalse(file_filter(path_traversal_file))


class MockFile:
    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    unittest.main()
