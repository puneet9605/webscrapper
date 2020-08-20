import unittest
from src.AssetFinder import fetch, getWebsiteAssets

class AssetFinder(unittest.TestCase):
    def test_fetch(self):
        assests = fetch('https://google.com')
        self.assertEqual(isinstance(assests, dict), True)

    def test_return_keys(self):
        keys = ('assets', 'links')
        assests = fetch('https://google.com')
        for key in keys:
            if key not in assests:
                assert False

    def test_getWebsiteAssets_return_type(self):
        imgs = getWebsiteAssets('https://google.com', 0)
        self.assertEqual(isinstance(imgs, list), True)

    def test_getWebsiteAssets_return_file_type(self):
        img_ends = {'apng', 'bmp', 'gif', 'ico', 'cur', 'jpg', 'jpeg', 'jfif', 'pjpeg', 'pjp', 'png', 'svg',
                    'tif', 'tiff', 'webp'}
        imgs = getWebsiteAssets('https://google.com', 0)
        for img in imgs:
            if img.split('.')[-1] not in img_ends:
                assert False







if __name__ == '__main__':
    unittest.main()
