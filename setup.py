import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read()

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="async_lichess_sdk",
    version=version,
    author="Amaedeusz Masny",
    author_email="amadeuszmasny@gmail.com",
    description="Asynchronous Python API client for accessing the lichess.org API.",
    url="https://github.com/amasend/lichees_python_SDK",
    packages=setuptools.find_packages(exclude=["tests"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
