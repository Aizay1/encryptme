from setuptools import setup, find_packages

setup(
    name="encryptme",
    version="1.0",
    py_modules=["encryptme"],  # Ensures encryptme.py is recognized
    install_requires=[
        "pycryptodome",
    ],
    entry_points={
        "console_scripts": [
            "encryptme=encryptme:main",
        ],
    },
    author="ZayTech",
    description="EncryptMe - Multi-layer encryption tool",
    long_description="A CLI-based encryption tool that applies multiple layers of encoding and encryption to secure text and credentials.",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
