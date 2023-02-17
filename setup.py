import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="chorder_py",
    version="1.0.0",
    author="TuneFlow",
    author_email="contact@info.tuneflow.com",
    description="A modified version of chorder with drums fix",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tuneflow/chorder-py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)