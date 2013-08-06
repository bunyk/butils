from distutils.core import setup

setup(
    name = 'butils',
    packages = [
        'butils',
    ],
    version = "0.0.1",
    description = "Python utils library",
    author = "Taras Bunyk",
    author_email = "tbunyk@gmail.com",
    url = "https://github.com/bunyk/butils",
    license='LICENSE',
    #download_url = "link to tgz",
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
