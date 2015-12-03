from setuptools import setup, find_packages

setup(name="drugstandards",
    install_requires = ["python-Levenshtein"],
    include_package_data=True,

    package_data = {'':['*.dat']},
    version="0.3",
    description="Tools for standardizing drug names.",
    url="http://github.com/mlbernauer/drugstandards",
    author="Michael L. Bernauer",
    author_email="mlbernauer@gmail.com",
    license="MIT",
    packages=["drugstandards"],
    zip_safe=False)

