
from setuptools import setup, find_packages

setup(
    name='poc_gcp',
    version='1.0',
    description='Poc GCP',
    author='Fabio Salinas',
    author_email='fabio.salinas1982@gmail.com',
    license='',
    packages=find_packages(
        where='src',
        include=['src', 'src.*']
    ),
    package_dir={
        'src':'src'
    },
    zip_safe=False
)
