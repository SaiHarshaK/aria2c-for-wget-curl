import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aria2stub",
    version="0.9.1",
    author="Sai Harsha Kottapalli",
    author_email="k.saiharsha7@gmail.com",
    description="Use aria2c instead for wget or curl to download large files using Debian alternatives subsystem instead of changing the shell scripts.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SaiHarshaK/aria2c-for-wget-curl",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires='>=3.6',
    entry_points={
        "console_scripts": [
            "wget = wget.stub:main",
            "curl = curl.stub:main"
        ]
    }
)
