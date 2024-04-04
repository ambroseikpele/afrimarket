
from setuptools import setup, find_packages
import io
from os import path

version='0.0.1'


here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with io.open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='afrimarket',
    version=version,
    description='Download market data from https://afx.kwayisi.org/',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/sire-ambrose/afrimarket',
    author='Ambrose Ikpele',
    author_email='ikpeleambroseobinna@gmail.com',
    license='Apache',
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        # 'Development Status :: 3 - Alpha',
        'Development Status :: 4 - Beta',
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
    keywords='pandas, finance, africa market, stocks',
    packages=find_packages(exclude=['contrib', 'docs', 'tests', 'examples']),
    install_requires=['requests==2.31.0', 'pandas==2.2.1', 'pyarrow==15.0.2', 'lxml==5.2.1'],
)

print("""
NOTE: afrimarket is not affiliated, endorsed, or vetted by https://afx.kwayisi.org/

You should refer to https://afx.kwayisi.org/ for terms of use for details on your rights
to use the actual data downloaded.""")