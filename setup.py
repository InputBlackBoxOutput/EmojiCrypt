from setuptools import setup, find_packages

VERSION = '0.1.0' 
DESCRIPTION = 'AES encryption encoded using emojis'
LONG_DESCRIPTION = 'Module to perform AES encryption on text and than encoded it using emojis'

setup(
        name="emojicrypt", 
        version=VERSION,
        author="Rutuparn Pawar",
        author_email="rutuparn.17U253@viit.ac.in",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], 
        keywords=['emojis', 'encoding', 'AES', 'encryption'],
        classifiers= [
            "Environment :: Console",
            "Intended Audience :: Developers",
            "Programming Language :: Python :: 3"
        ]
)