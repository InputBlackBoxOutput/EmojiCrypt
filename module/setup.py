from setuptools import setup, find_packages

VERSION = "1.0.2"
DESCRIPTION = "AES encryption encoded using emojis"
LONG_DESCRIPTION = (
    "Module to perform AES encryption on text and than encoded it using emojis"
)

setup(
    name="emojicrypt",
    version=VERSION,
    author="Rutuparn Pawar",
    author_email="rutuparn.17U253@viit.ac.in",
    url="https://github.com/InputBlackBoxOutput/EmojiCrypt",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['pycryptodome==3.10.1'],
    keywords=["emojis", "encoding", "AES", "encryption"],
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
    ],
)
