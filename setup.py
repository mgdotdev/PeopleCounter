from setuptools import setup, find_packages
from os import path

here = path.dirname(path.abspath(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='PeopleCounter',
    version='0.0.1',
    description='Python library for counting people at the beach',
    long_description=long_description,
    url='https://github.com/1mikegrn/peoplecounter',
    author='Michael Green, Shane May',
    license='GPL-3.0',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Hackathon',
        'License :: OSI Approved :: GPL-3.0 License',
    ],

    packages=find_packages(),

    include_package_data=True,

    python_requires='>=3.6',

    project_urls={
        'GitHub': 'https://github.com/1mikegrn/PeopleCounter'
    }

)