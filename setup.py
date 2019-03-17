from setuptools import setup
import setuptools
with open("README.md", 'r') as fh:
    long_description = fh.read()

__version__ = "0.0.1"

setup(name="paynow2",
	version="0.0.1",
	description="Paynow Implementation for Python2.x",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/ignertic/paynow2",
	author="Gishobert (SuperCode) Gwenzi",
	author_email="ilovebugsincode@gmail.com",
	licence="MIT",
	classifiers=[
		"Programming Language :: Python :: 2",
		"Operating System :: OS Independent"],
	packages=setuptools.find_packages(),
	include_package_data=True,
	install_requires=["requests"],
	entry_points={"console_scripts" : ["paynow2=paynow2.__main__:main" ]},
	) # TODO: Add more console scripts
