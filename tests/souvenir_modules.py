import unittest

from souvenir.zipcode import Endpoint, Zipcode
from souvenir.image import ImageBing, ImageGoogle


class TestComponent(unittest.TestCase):
    def setUp(self):
        """Generate instance of Department to test it."""
        self.my_dep = Endpoint.san_vicente.value
        self.zip = Zipcode(self.my_dep)
        self.image_bing = ImageBing(self.my_dep)
        self.image_google = ImageGoogle(self.my_dep)

    def test_enumeration(self):
        """Test if Enum has 14 values regarded to 14 departments."""
        keys = [dep.value for dep in Endpoint]
        self.assertEqual(14, len(keys))

    def test_summary(self):
        """
        Test if method returns None type, it mean that filter argument
        is wrong and bs4 doesn't find any match.
        """
        self.assertNotEqual(self.zip.summary, None)

    def test_zipcodes(self):
        """
        Test if method returns None type, it mean that array with
        HTML labels match doesn't exist in filter argument used.
        """
        self.assertNotEqual(self.zip.zip_codes, None)

    def test_bing_images(self):
        """Test if result are not None or empty array."""
        self.assertNotEqual(self.image_bing.images, None)
        self.assertNotEqual(self.image_bing.images, [])

    @unittest.skip("Google API is not free anymore")
    def test_google_images(self):
        """Test if result are not None or empty array."""
        self.assertNotEqual(self.image_google.images, None)
        self.assertNotEqual(self.image_google.images, [])
