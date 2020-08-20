from setuptools import setup

setup(
    name='webscrapper',
    version='0.1',
    packages=['webscrapper'],
    url='',
    license='',
    author='puneet',
    author_email='singh.puneet@gmail.com',
    description='web scrapper build ',
    install_requires=['requests==2.23.0',
                      'beautifulsoup4==4.9.1',
                      'lxml==4.5.2',
                      'urllib3==1.25.8'
    ]
)
