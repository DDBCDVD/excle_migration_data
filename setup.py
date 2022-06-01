from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in excle_migration_data/__init__.py
from excle_migration_data import __version__ as version

setup(
	name="excle_migration_data",
	version=version,
	description="migrations data doctypes",
	author="excle",
	author_email="excle@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
