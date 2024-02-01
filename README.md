# Lab: Class 18 - Cryptography

## Author: Xin Deng

### Links and Resources

- chatGPT
- [Class 18 Demo](https://github.com/codefellows/seattle-code-python-401d24/tree/main/class-18/demo/crypto)
- TA: Brandon

### Set up

Type into your terminal:

```bash
mkdir caesar-cipher
cd caesar-cipher
touch README.md
python3 -m venv .venv
source .venv/bin/activate
git init
touch .gitignore
mkdir caesar_cipher
touch caesar_cipher/cipher.py
mkdir tests
mkdir tests/test_caesar.py


```

Add `.venv` folder to `.gitignore`

```bash
git add .
git commit -m "first commit"
```

Create remote repo and follow instructions

```bash
pip install pytest
pip install nltk

pip freeze > requirements.txt

```

### Overview - Caesar Cipher

Tackling a cryptographic classic - the Caesar Cipher. This project involves creating a Python application to encrypt and decrypt messages using the Caesar Cipher algorithm. The application should not only perform basic encryption and decryption with a given key but also include a cracking mechanism to decipher messages without the key.

#### Version 1.0

Build 1.0 Feature Tasks

1. An `encrypt` function that takes a plain text phrase and a numeric shift as inputs.
2. A `decrypt` function that takes in encrypted text and the numeric shift.
3. A `crack` function that decodes the cipher, transforming an encrypted message into its original state without access to the key.
4. Import and implement `nltk` library to access a corpus of English words

### To run caesar_cipher:

    ```bash
    python -m caesar_cipher.cipher
    ```

### To test caesar_cipher:

    ```bash
    pytest tests/test_caesar.py
    ```
