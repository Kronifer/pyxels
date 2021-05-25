from setuptools import setup

with open("README.md", "r") as file:
    long_des = file.read()

setup(
    name="Pyxels",
    packages=["pyxels"],
    description="An API wrapper for the Python Discord Pixels API",
    version="1.0.2",
    long_description=long_des,
    long_description_content_type="text/markdown",
    license="MIT",
    author="Dillon Runke",
    author_email="runkedillon@gmail.com",
    url="https://github.com/kronifer/pyxels",
    download_url="https://github.com/Kronifer/pyxels/archive/v1.0.0.tar.gz",
    keywords=["API"],
    classifiers = [
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers"
    ]
)