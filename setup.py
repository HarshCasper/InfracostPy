import os
from setuptools import setup
from setuptools import find_packages


setup(
    name="InfracostPy",
    description="Python wrapper for the Infracost CLI tool",
    author="Harsh Mishra",
    author_email="erbeusgriffincasper@gmail.com",
    url="https://github.com/HarshCasper/InfracostPy",
    keywords=["infracost", "terraform", "finops", "cost-estimate", "cost-report"],
    packages=find_packages(),
    long_description_content_type="text/markdown",
    long_description=open(os.path.join(os.path.dirname(__file__), "README.md")).read(),
    include_package_data=True,
    install_requires=[],
    extras_require={},
    entry_points={
        "console_scripts": [
            "infracostpy = infracostpy.infracost:main",
        ],
    },
)
