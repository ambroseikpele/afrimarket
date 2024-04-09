
from setuptools import setup, find_packages
from os import path

version='0.0.0.0'


here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Get required packages
with open(path.join(here, 'requirements.txt'), 'r') as file:
    requirements_content = file.readlines()
requirements_list = [requirement.strip() for requirement in requirements_content if requirement.strip()]


setup(
    name='afrimarket',
    version=version,
    description='Download african market data from https://afx.kwayisi.org/',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/sire-ambrose/afrimarket',
    author='Ambrose Ikpele',
    author_email='ikpeleambroseobinna@gmail.com',
    license='Apache',
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
         'Development Status :: 3 - Alpha',
        # 'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',


        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Office/Business :: Financial',
        'Topic :: Office/Business :: Financial :: Investment',
        'Topic :: Scientific/Engineering :: Interface Engine/Protocol Translator',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',

        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    platforms=['any'],
    keywords='pandas, finance, african market, stocks, african stocks, africa',
    packages=find_packages(exclude=['contrib', 'docs', 'tests', 'examples']),
    install_requires=requirements_list,
)

print("""
NOTE: afrimarket is not affiliated, endorsed, or vetted by https://afx.kwayisi.org/

You should refer to https://afx.kwayisi.org/ for terms of use for details on your rights
to use the actual data downloaded.""")