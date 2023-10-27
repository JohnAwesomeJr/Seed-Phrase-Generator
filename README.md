# Seed-Phrase-Generator
This will take 256 ones and zeros and turn it into a 24 word seed phrase.

This Python script generates a BIP-39-compliant cryptocurrency seed phrase using a 256-character binary input, which can be obtained by flipping coins 256 times. The generated seed phrase can be used to secure your cryptocurrency wallet.

## How to Use

1. **Install Python:**

   - If you don't have Python installed, follow these simple steps:
   
     - Visit the Python download page: [https://www.python.org/downloads/](https://www.python.org/downloads/).
     - Download the latest version of Python for your operating system (Windows, macOS, or Linux).
     - Run the installer and follow the installation instructions.

2. **Run the Script:**

   - Download the script file from this GitHub repository.
   - Open a terminal or command prompt on your computer. You can usually find this in your computer's applications menu or by searching for "Command Prompt" (Windows) or "Terminal" (macOS and Linux).
   - Navigate to the folder where you saved the script using the `cd` command. For example, if you saved it on your desktop, you might type `cd Desktop`.
   - Run the script by entering `python script_name.py`, where `script_name.py` is the name of the script file you downloaded. For example, if you saved the script as `seed_phrase_generator.py`, you would enter `python seed_phrase_generator.py`.

3. The script will prompt you to enter your 256-character binary sequence.

4. The script will generate your BIP-39 seed phrase.

5. Ensure the security of your seed phrase and use it to access your cryptocurrency wallet.

## Important Note

**Don't trust, verify:** It's essential to review the code yourself and understand how it works before using it for generating a seed phrase. The code is designed to be simple and transparent, with comments provided to help you understand its operations and ensure its safety.

**Security Warning:** Ensure that your binary input is generated securely, and keep your seed phrase safe and confidential, as it grants access to your cryptocurrency funds.

## How It Works

1. The script begins by prompting the user to enter a 256-character binary input. It ensures that the input is exactly 256 characters long and a multiple of 8 (1 byte).

2. The binary input is converted to bytes.

3. The SHA-256 hash of the binary input is calculated and displayed.

4. The first two characters of the SHA-256 hash are extracted and converted from hexadecimal to binary.

5. The binary input and the binary result are concatenated.

6. The script reads a file called "bip39.txt" to create a dictionary that maps numeric numbers to BIP-39 words.

7. The concatenated binary is split into sets of 11 characters each, and the corresponding BIP-39 words are extracted.

8. The BIP-39 words are joined to form the seed phrase.
