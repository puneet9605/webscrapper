# webscrapper

webscrapper is a Python library for getting image tags and url links

## Installation

Use the setup.py to install webscrapper 

```bash
setup.py install
```

## Usage

```python
from webscrapper.AssetFinder import fetch,getWebsiteAssets
fetch(url) # will return dict 
getWebsiteAssets(url) # will return list of image urls
```

## testing
Install all dependencies in requirment.txt
```bash
pip install -r requirment.txt
```
run test
```bash
python test_fetch.py
```
