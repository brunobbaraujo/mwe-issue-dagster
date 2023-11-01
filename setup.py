from setuptools import find_packages, setup

setup(
    name="mwe_issue_dagster",
    packages=find_packages(exclude=["mwe_issue_dagster_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
