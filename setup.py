from setuptools import find_packages, setup

long_description = ""
with open("README.md") as ifp:
    long_description = ifp.read()

setup(
    name="multicall-py",
    version="0.0.1",
    packages=find_packages(),
    package_data={"multicall": ["build/contracts/*.json"]},
    include_package_data=True,
    install_requires=["eth-brownie"],
    extras_require={
        "dev": [
            "black",
            "moonworm >= 0.2.4",
        ],
        "distribute": ["setuptools", "twine", "wheel"],
    },
    description="Python interface to multicall contracts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Moonstream Engineering",
    author_email="engineering@moonstream.to",
    url="https://github.com/bugout-dev/multicall",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "multicall2=multicall.Multicall2:main",
        ]
    },
)
