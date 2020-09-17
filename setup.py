import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jitterbit-pkg-bbrummer", # Replace with your own username
    version="0.0.1",
    author="Byron Brummer",
    author_email="byron.brummer@gmail.com",
    description="Frontend for Jitterbit Management API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bbrummer/jitterbit_admin_python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
