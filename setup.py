from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="Library",
    use_scm_version={"version_scheme": "post-release", "write_to": "pyrival/version.py"},
    url="https://github.com/moyomogi/python_2022_lib",
    project_urls={
        "Bug Tracker": "https://github.com/moyomogi/python_2022_lib/issues",
        "Documentation": "https://pyrival.readthedocs.io/",
        "Source Code": "https://github.com/moyomogi/python_2022_lib",
    },
    author="moyomogi",
    classifiers=[
        "Programming Language :: Python :: 3.8",
    ],
    description="Competitive Programming Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=["competitive-programming", "data-structures", "algorithms"],
    setup_requires=["setuptools_scm"],
    packages=find_packages(),
)
