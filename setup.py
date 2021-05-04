from os import path

from setuptools import setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='makemkv',
    version='0.1',
    description='Python wrapper for MakeMKV',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    author='d-k-bo',
    author_email='dkbo@mail.de',
    url='https://github.com/d-k-bo/python-makemkv',
    packages=['makemkv'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Topic :: Multimedia :: Video',
    ],
    license='MIT',
    keywords='mkv dvd bluray ripping makemkv remuxing metadata',
    install_requires=[
        'click',
        'iso639-lang',
        'rich'
    ],
    entry_points={
        'console_scripts': [
            'pymakemkv = makemkv.__main__:cli',
        ],
    },
)
