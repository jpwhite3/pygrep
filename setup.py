from setuptools import setup

setup(
    name="pygrep",
    version="0.1.0",
    description="A pure Python implementation of GREP",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Topic :: Utilities",
    ],
    keywords="linux grep regex utility search",
    url="https://github.com/jpwhite3/pygrep",
    author="JP White",
    author_email="jpwhite3@gmail.com",
    license="MIT",
    packages=["pygrep"],
    entry_points={"console_scripts": ["pygrep=pygrep.cli:main"]},
    include_package_data=True,
    zip_safe=False,
)
