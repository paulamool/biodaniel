#!/usr/bin/env python

from distutils.core import setup

LONG_DESCRIPTION = \
'''The program reads one or more input FASTA files.
For each file it computes a variety of statistics, and then
prints a summary of the statistics as output.

The goal is to provide a solid foundation for new bioinformatics command line tools,
and is an ideal starting place for new projects.'''


setup(
    name='biodaniel',
    version='0.2.0.0',
    author='Daniel Cameron',
    author_email='cameron.d@wehi.edu.au',
    packages=['biodaniel'],
    package_dir={'biodaniel': 'biodaniel'},
    entry_points={
        'console_scripts': ['biodaniel = biodaniel.biodaniel:main']
    },
    url='https://github.com/bjpop/biodaniel',
    license='LICENSE',
    description=('A prototypical bioinformatics command line tool'),
    long_description=(LONG_DESCRIPTION),
    install_requires=["biopython"],
)
