import setuptools  # type: ignore

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="oh-my-pika",
    version="0.1.0",
    author="so1n",
    author_email="so1n897046026@gmail.com",
    description="oh-my-pika is not an ORM, but it can give Python developers a better SQL writing experience",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/so1n/oh-my-pika",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
