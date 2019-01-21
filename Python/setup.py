import tifftoniff
from setuptools import setup


version = tifftoniff.__version__

setup(
    name='tifftoniff',
    version=tifftoniff.__version__,
    py_modules=['tifftoniff'],
    install_requires=[
        'Click', 'Tyf'
    ],
    entry_points='''
        [console_scripts]
        tifftoniff=tifftoniff:cli
    ''',
)
