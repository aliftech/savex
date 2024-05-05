from setuptools import setup

setup(
    name="savex",
    version="0.1.0",
    description="Savex is a Python library crafted to bolster the security of file uploads within web applications. With an emphasis on mitigating prevalent vulnerabilities associated with file handling, Savex furnishes sturdy sanitization and validation capabilities to ensure that uploaded files are safe for utilization within your application.",
    long_description=open("README.md").read(),
    url="https://github.com/aliftech/savex",
    author="Wahyu Krisna Aji",
    author_email="wahyukrisnaaji32@gmail.com",
    license="MIT",
    classifiers=[
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3"
    ],
    keywords=["savex", "file filtering", "backdoor detection"],
)
