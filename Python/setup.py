import tifftoniff
from setuptools import setup, find_packages


version = tifftoniff.__version__

setup(
    name='tifftoniff',
    version=tifftoniff.__version__,
    packages=find_packages(),
    entry_points = {
        'console_scripts': ['tifftoniff = tifftoniff.__main__:main'],
    }
)
