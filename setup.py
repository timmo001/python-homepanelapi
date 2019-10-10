"""Setup configuration."""
import setuptools


with open("README.md", "r") as fh:
    LONG = fh.read()
setuptools.setup(
    name="homepanelapi",
    version="1.0.1",
    author="Timmo",
    author_email="contact@timmo.xyz",
    description="",
    long_description=LONG,
    install_requires=["aiohttp", "click"],
    long_description_content_type="text/markdown",
    url="https://github.com/timmo001/python-homepanelapi",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    entry_points={"console_scripts": ["homepanelapi = homepanelapi.cli:cli"]},
)
