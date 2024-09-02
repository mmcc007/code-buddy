from setuptools import setup, find_packages

setup(
    name="code-buddy",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'code-buddy=code_buddy.main:main',
        ],
    },
    install_requires=[
        'GitPython',
    ],
    author="Maurice McCabe",
    author_email="mmcc007@gmail.com",
    description="A command-line coding assistant",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/mmcc007/code-buddy",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)