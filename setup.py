from setuptools import setup

setup(
    name="Type9",
    version="0.0.1",
    description="Simple cli tool to generate password hashes that are compatible with Cisco's Type 9.",
    url="https://github.com/timway/type9",
    author="Tim Way",
    packages=['type9'],
    entry_points={
        "console_scripts": ["type9=type9.cli:main"]
        },
    install_requires=[
        "scrypt"
        ]
    )
