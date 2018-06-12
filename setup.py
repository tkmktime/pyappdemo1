import setuptools

with open("README.md","r") as fh:
	long_description = fh.read()

setuptools.setup(
	name='pyappdemo1',
	version='0.1',
	description='An pyinstaller demo',
	long_description=long_description,
	long_description_content_type="text/markdown",	
	packages=setuptools.find_packages(),
	url='https://github.com/tkmktime/pyappdemo1.git',
	author='Tim',
	author_email='tkmktime@gmail.com',
	classifiers=[
		'Programming Language :: Python :: 2',
		'Development Status :: 1 - Alpha',
		'License :: OSI Approved :: MIT License',  
	],
)	
