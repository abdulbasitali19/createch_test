from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in createch_app/__init__.py
from createch_app import __version__ as version

setup(
	name="createch_app",
	version=version,
	description="software house app",
	author="abdul basit ",
	author_email="createch_app@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
