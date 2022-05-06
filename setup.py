import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-package",
    version="0.0.3",
    author="Alexander Andryukov",
    author_email="andryukov@gmail.com",
    description="First package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/someth",
    project_urls={"Bug Tracker": "https://gitlab.com/someth/bug_tracker"},
    classifiers=["Programming Language :: Python :: 3", ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8"
)
