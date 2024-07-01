# Ransomware-Attack-Simulation

This Python script simulates a ransomware attack for educational purposes. It provides a hands-on demonstration of file encryption and decryption techniques using AES encryption from the cryptography library. The script includes a visual loading animation using tqdm and utilizes ASCII art from art for a visually appealing command-line interface.

## Features

- **File Encryption**: Encrypts files in the current directory, excluding certain system files, using AES encryption.
- **File Decryption**: Decrypts previously encrypted files using a passphrase provided by the user.
- **Visual Feedback**: Displays a progress bar during encryption and decryption processes, enhancing user experience.
- **Educational Tool**: Intended for educational purposes only to understand how ransomware operates and the importance of data security.

## Requirements

- Python 3.x
- cryptography
- tqdm
- art
- psutil

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/RapidScripter/Ransomware-Attack-Simulation.git

2. Navigate into the directory:
   ```bash
   cd Ransomware-Attack-Simulation

3. Install dependencies:
   ```bash
   pip install -r requirements.txt

## Usage

1. Run the script
   ```bash
   python ransomware.py

2. **Follow the prompts to select an action**:
- Enter `1` to encrypt files.
- Enter `2` to decrypt files.
- Enter `3` to exit.

## ALERT for `ransomware-whole-system.py` script
- **Use with Caution:** This script encrypts files across all drives and directories on the system, excluding certain OS directories and file types.
- **Important:** Ensure you have backed up important data before running this script, as it can lead to irreversible data loss without proper decryption.
- **Usage:** Run the script and follow the prompts to encrypt files (`1`), decrypt files (`2`), or exit (`3`).

## Screenshots

![Alt text](/Screenshots/main_window.jpg?raw=true "Ransomware Simulator")
