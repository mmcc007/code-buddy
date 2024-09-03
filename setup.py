from setuptools import setup, find_packages
from version import __version__

setup(
    name="code-buddy-assist",
    version=__version__,
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'code-buddy-assist=code_buddy.main:main',
        ],
    },
    install_requires=[
        'GitPython',
    ],
    author="Maurice McCabe",
    author_email="mmcc007@gmail.com",
    description="A command-line coding assistant using LLMs",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/mmcc007/code-buddy-assist",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)