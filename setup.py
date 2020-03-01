with open('VERSION.txt', 'r') as f:
    version = f.read()

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Lichess-Python-Client-AMADEUSZ-MASNY",
    version=version,
    author="Amaedeusz Masny",
    author_email="amadeuszmasny@gmail.com",
    description="Python API client for accessing the lichess.org API.",
    url="...",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
