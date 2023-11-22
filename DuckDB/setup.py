from setuptools import find_packages, setup

setup(
    name="DuckDB_data_import",
    packages=find_packages(exclude=["data_import"]),
    install_requires=["dackdb", "pandas", "sqlescapy"]
)
