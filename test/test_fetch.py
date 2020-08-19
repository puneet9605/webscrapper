import unittest
from src.AssetFinder import fetch

class AssetFinder(unittest.TestCase):
    def test_fetch(self):
        assests = fetch('https://google.com')
        self.assertEqual(isinstance(assests, dict), True)

    def test_keys(self):
        keys = ('assets', 'links')
        assests = fetch('https://google.com')
        for key in keys:
            if key not in assests:
                assert False

if __name__ == '__main__':
    unittest.main()
