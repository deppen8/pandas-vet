import setuptools

requires = [
    "flake8 > 3.0.0",
]

tests_requires = [
    "pytest > 4.0.0"
]

flake8_entry_point = 'flake8.extension'

with open("README.md", "rt") as f:
    long_description = f.read()

version = {}
with open("pandas_vet/version.py") as fp:
    exec(fp.read(), version)

setuptools.setup(
    name="pandas-vet",
    license="MIT",
    version=version["__version__"],
    description="A flake8 plugin to lint pandas in an opinionated way",
    author="Jacob Deppen",
    author_email="deppen.8@gmail.com",
    url="https://github.com/deppen8/pandas-vet",
    packages=[
        "pandas_vet",
    ],
    install_requires=requires,
    tests_require=tests_requires,
    entry_points={
        flake8_entry_point: [
            'PD = pandas_vet:VetPlugin',
        ],
    },
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Framework :: Flake8",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        # "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
)
