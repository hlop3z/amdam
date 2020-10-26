import setuptools

# python3.7 setup.py bdist_wheel
# python3.7 setup.py sdist

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name                            = "amdam",
    version                         = "0.0.1",
    author                          = "Hector M. Lopez",
    author_email                    = "fustack@googlegroups.com",
    python_requires                 = '>=3.7',
    description                     = "Fullstack Development",
    long_description                = long_description,
    long_description_content_type   = "text/markdown",
    url                             = "https://github.com/hlop3z/amdam",
    packages                        = setuptools.find_packages(exclude=(".git",)),
    include_package_data            = True,
    install_requires = [
        "aiofile>=0.20.1",
        "Quart>=0.11.3",
        "Quart-CORS>=0.3.0",
        "sanic>=9.6.2",
        "sanic_cors>=0.9.8",
        "cherrypy-cors>=1.6",
        "cherrypy>=18.5.0",
        "psutil>=5.7.0",
    ],
    classifiers = [
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
