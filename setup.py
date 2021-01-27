import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="chorder",
    version="1.0.0",
    author="Mingzhi Zeng",
    author_email="zeostudio@gmail.com",
    description="A modified version of chorder with drums fix",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitee.com/panacea123/chorder",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)