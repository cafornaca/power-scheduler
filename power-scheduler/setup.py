from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='power-scheduler',
    version='0.1.0',
    packages=find_packages(),
    license="Kaiser Permanente",
    long_description=long_description,
    include_package_data=True,
    zip_safe=False
)
