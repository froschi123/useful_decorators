import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='useful_decorators',
    version='1.0.2',
    packages=setuptools.find_packages(),
    url='https://github.com/froschi123/useful_decorators',
    license='MIT License',
    author='Bernd Wehmöller',
    author_email='bernd@wehmoeller.net',
    description='Some useful decorators for debugging and logging',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
