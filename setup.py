from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='shudder-py',
    url='https://github.com/mrwilson/shudder-py',
    version='0.1.0',
    description='A python API client for horror streaming service Shudder',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Alex Wilson',
    author_email='alex+github@probablyfine.co.uk',
    license='MIT',
    packages=find_packages(),
    install_requires=(
        'requests',
        'lxml'
    ),
    classifiers=[
        "Programming Language :: Python :: 3.8",
    ]
)
