from setuptools import setup

setup(
    name = 'butils',
    packages = [
        'butils',
    ],
    version = "0.0.2",
    description = "Python utils library",
    author = "Taras Bunyk",
    author_email = "tbunyk@gmail.com",
    url = "https://github.com/bunyk/butils",
    license='PUBLIC',
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    long_description = open('README.md').read(),
    install_requires=[
        'pygments',
    ],
)
