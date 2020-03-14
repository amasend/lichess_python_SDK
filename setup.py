import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read()

with open("README.md", "r") as fh:
    long_description = fh.read()

PROJECT_URLS = {
    'Bug Tracker': 'https://github.com/amasend/lichess_python_SDK/issues',
    'Documentation': 'https://amasend.github.io/lichess_python_SDK/html/index.html',
    'Source Code': 'https://github.com/amasend/lichess_python_SDK'
}

setuptools.setup(
    name="async_lichess_sdk",
    version=version,
    author="Amaedeusz Masny",
    author_email="amadeuszmasny@gmail.com",
    description="Asynchronous Python API client for accessing the lichess.org API.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/amasend/lichees_python_SDK",
    packages=setuptools.find_packages(exclude=["tests"]),
    license="Apache Software License",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
