from setuptools import setup, find_packages

config = {
    'description': 'TEST',
    'author': 'andriy',
    'url': 'https://github.com/AndriyPlakhotnyk',
    'download_url': 'https://github.com/AndriyPlakhotnyk/andriy',
    'author_email': 'andriy.plakhotnyk@ucalgay.ca',
    'version': '0.0.1',
    'install_requires': ['pandas', 'seaborn'],
    'packages': find_packages(),
    'scripts': [],
    'name': 'andriy'
}

setup(**config)
