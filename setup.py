import setuptools

with open("requirements.txt", "r") as fp:
    requirements = [i for i in fp.readlines()]

setuptools.setup(
    name="app", version="0.0.1", packages=setuptools.find_packages(), install_requires=requirements)
