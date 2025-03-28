# EncryptMe

EncryptMe is a multi-layer encryption tool that secures text and credentials using various encoding techniques and RSA encryption.

## Features

- Multi-layer encoding and encryption
- Secure storage of encrypted credentials
- CLI-based interface for easy use

## Installation

To install EncryptMe globally and make it executable using `encryptme` in the CLI:


# Clone the repository
    git clone https://github.com/Aizay1/encryptme
    cd encryptme
# Create a virtual environment

    python3 -m venv venv

## Activate the virtual environment
# On Linux/Mac:

    source venv/bin/activate

# On Windows (Command Prompt):

    venv\Scripts\activate

# Install the package
    pip install .

  #  Usag

### Encrypt a text
    encryptme -e "YourSecretText"


### Decrypt a text
    encryptme -d "EncryptedText"


### Store encrypted credentials
    encryptme -s username password


### Retrieve stored password
    encryptme -r username







