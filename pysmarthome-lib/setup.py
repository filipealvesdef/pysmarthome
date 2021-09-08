from setuptools import setup, find_packages

setup(
    name='pysmarthome_lib',
    description='A python lib that abstracts pysmarthome entities',
    version='1.0.0',
    author='Filipe Alves',
    author_email='filipe.alvesdefernando@gmail.com',
    install_requires=[
        'vesla_pymvc>=2.0.0',
        'bs4',
        'requests',
    ],
    packages=find_packages(),
    url='https://github.com/filipealvesdef/pysmarthome/tree/master/pysmarthome-lib',
    zip_safe=False,
)
