import setuptools

# python3.7 setup.py bdist_wheel
# python3.7 setup.py sdist

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name                            = "amdam",
    version                         = "0.0.1",
    author                          = "Hector M. Lopez",
    author_email                    = "hlopez.devops@gmail.com",
    python_requires                 = '>=3.7',
    description                     = "Fullstack Development",
    long_description                = long_description,
    long_description_content_type   = "text/markdown",
    url                             = "https://github.com/hlop3z/pgtiny",
    packages                        = setuptools.find_packages(exclude=(".git",)),
    classifiers = [
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
