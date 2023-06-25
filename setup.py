from setuptools import find_packages, setup

VERSION = "1.0.0"

with open("README.md", "r", encoding="utf-8") as readme:
    long_description = readme.read()

setup(
    name="fastapi-maintenance-mode",
    version=VERSION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    url="https://github.com/iunary/fastapi-maintenance-mode",
    license="MIT",
    author="Yusuf",
    author_email="contact@yusuf.im",
    description="FastAPI middleware for enabling maintenance mode",
    install_requires=[
        "fastapi",
        "httpx",
    ],
    classifiers=[
        "Framework :: FastAPI",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
    ],
)
