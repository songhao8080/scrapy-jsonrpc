from os.path import dirname, join
from setuptools import setup, find_packages


setup(
    name='scrapy-jsonrpc-api',
    version='1.0.0',
    url='https://github.com/xiayus/scrapy-jsonrpc',
    description='Scrapy extenstion to control spiders using JSON-RPC By Allen',
    author='Scrapy developers,Allen',
    license='BSD',
    packages=find_packages(exclude=('tests', 'tests.*')),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Framework :: Scrapy',
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
    ],
    install_requires=[
        'Twisted>=10.0.0',
        'Scrapy>=2.4.0',
        'six>=1.15.0',
        'w3lib>=1.22.0',
        'urllib3>=1.26.2',
    ],
)
