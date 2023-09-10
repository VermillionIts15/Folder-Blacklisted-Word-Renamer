import os
import random
import string
import datetime

IsFolderPath = True  # Set to True if you want to use the script's directory as the target folder

blacklist = {
    "blacklisted_name1": "replacement1",
    "blacklisted_name2": "replacement2",
}

whitelist = {
    "file_to_keep1": "file_to_keep1",
}

if IsFolderPath:
    directory = os.path.dirname(os.path.abspath(__file__))
else:
    directory = "/path/to/your/directory"

log_directory = os.path.join(directory, "log")
os.makedirs(log_directory, exist_ok=True)

def generate_random_sequence():
    return ''.join(random.choices(string.digits, k=5))

def rename_files(directory, blacklist, whitelist):
    log_file_name = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S") + ".log"
    log_file_path = os.path.join(log_directory, log_file_name)
    with open(log_file_path, "w") as log_file:
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            for blacklisted_name, replacement in blacklist.items():
                if blacklisted_name in filename:
                    whitelisted_name = whitelist.get(blacklisted_name, None)
                    if whitelisted_name is None:
                        new_filename = filename.replace(blacklisted_name, replacement)
                        if not new_filename:
                            new_filename = (
                                whitelist.get("default_name", "default_name")
                                + generate_random_sequence()
                            )
                        new_path = os.path.join(directory, new_filename)
                        os.rename(file_path, new_path)
                        log_file.write(
                            f"Old Name: {filename} | New Name: {new_filename} ({datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')})\n"
                        )
                        print(f"Renamed: {filename} -> {new_filename}")
                    else:
                        print(f"Skipped: {filename} (Whitelisted)")

while True:
    print("(1) Start Renaming")
    print("(2) Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        rename_files(directory, blacklist, whitelist)
    elif choice == "2":
        break
    else:
        print("Invalid choice. Please choose again.")
