from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in fgarcia_frappe_eval/__init__.py
from fgarcia_frappe_eval import __version__ as version

setup(
	name="fgarcia_frappe_eval",
	version=version,
	description="Gym Management System",
	author="Fernando Garcia",
	author_email="andy@xurpas.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
