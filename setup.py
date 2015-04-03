from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='django_ladon',
    version='0.1.0',
    description='A simple ladon wrapper for Django',
    long_description=long_description,
    url='https://github.com/TargetHolding/django-ladon',
    author='Harmen Wassenaar',
    author_email='harmen.wassenaar@target-holding.nl',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='django ladon soap rest rpc',
    packages=['django_ladon'],
    install_requires=['django', 'ladon']
)
