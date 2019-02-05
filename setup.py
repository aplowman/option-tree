"""Pip installation script."""

from setuptools import find_packages, setup

setup(
    name='optiontree',
    description=('Hierarchical storage of arbitrary option sets within a '
                 'relational database using the entity-attribute-value (EAV) '
                 'data model.'),
    version="0.1.0",
    author='Adam J. Plowman',
    packages=find_packages(),
    install_requires=[
        'sqlalchemy',
    ],
)
