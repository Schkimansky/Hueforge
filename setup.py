from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    readme = "\n" + fh.read()

VERSION = '1.30'  # Increment on next change
DESCRIPTION = 'Python color engine.'

setup(
    name="hueforge",
    version=VERSION,
    author="Schkimansky",
    author_email="<ahmadchawla1432@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    keywords=["python", "color", "engine", "colorengine", "hue", "contrast", "saturation", "hueforge", "manager"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
