try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Web Scraping NBA Stats'
    'author': 'Pranav Yadav',
    'author_email': 'pranavyadav@live.com',
    'version': '0.0.1',
    'packages': find_packages(),
    'name': 'pandas', 'requests'
}

setup(**config)
