from setuptools import setup, find_packages

setup(
    name="encryptme",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "pycryptodofrom setuptools import setup, find_packages

setup(
    name="encryptme",
    version="1.0",
    py_modules=["encryptme"],  # Updated to match script-based structure
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
    python_requires='>=3.6',
)
me",
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
    python_requires='>=3.6',
)

