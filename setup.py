"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
Autogenerated by poetry-setup:
https://github.com/orsinium/poetry-setup
"""
# IMPORTANT: this file is autogenerated. Do not edit it manually.
# All changes will be lost after `poetry-setup` command execution.
# ----------------------------------------------------------------
# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path
# io.open is needed for projects that support Python 2.7
# It ensures open() defaults to text mode with universal newlines,
# and accepts an argument to specify the text encoding
# Python 3 only projects can skip this import
from io import open
here = path.abspath(path.dirname(__file__))
# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.
setup(
    # https://packaging.python.org/specifications/core-metadata/#name
    name='poetry-setup',  # Required
    # https://www.python.org/dev/peps/pep-0440/
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.1.0',  # Required
    # https://packaging.python.org/specifications/core-metadata/#summary
    # Required
    description="make setup.py (setutools) from pyproject.toml (poetry)",
    # https://packaging.python.org/specifications/core-metadata/#description-optional
    long_description=long_description,  # Optional
    # https://packaging.python.org/specifications/core-metadata/#description-content-type-optional
    long_description_content_type='text/markdown',  # Optional (see note above)
    url="https://github.com/orsinium/poetry-setup",  # Optional
    author="Gram Orsinium",  # Optional
    author_email="master_fess@mail.ru",  # Optional
    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[  # Optional
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords=' '.join(
        ['packaging', 'dependency', 'poetry', 'setuptools', 'pip']),  # Optional
    packages=find_packages(),  # Required
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=['autopep8', 'jinja2', 'pip', 'poetry', 'pytest',
                      'yapf'],  # Optional
    # NOT SUPPORTED YET
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files
    data_files=[],  # Optional
    entry_points={  # Optional
        'console_scripts': [
            'poetry-setup=poetry_setup:main',
        ],
    },
    # https://packaging.python.org/specifications/core-metadata/#project-url-multiple-use
    project_urls={  # Optional
        'homepage': 'https://github.com/orsinium/poetry-setup',
    },
)
