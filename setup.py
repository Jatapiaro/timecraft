from setuptools import setup

with open("README.md") as f:
    readme = f.read()


def parse_requirements(filename):
    """load requirements from a pip requirements file"""
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


install_reqs = parse_requirements("requirements.txt")

setup(
    name="timecraft",
    version="1.0.0",
    description="Lightweight utilities for working with dates and time in Python.",
    long_description=readme,
    license="Proprietary",
    author="Jacobo Tapia",
    author_email="jatapiaro@gmail.com",
    url="https://github.com/Jatapiaro/timecraft.git",
    packages=[
        "timecraft",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    install_requires=install_reqs,
    include_package_data=True,
    python_requires=">=3.7",
)
