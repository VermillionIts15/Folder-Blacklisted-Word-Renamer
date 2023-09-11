import os
import json
import random
import string
import datetime
import shutil

def load_config():
    try:
        with open("config.json", "r") as config_file:
            config_data = json.load(config_file)
        return config_data
    except FileNotFoundError:
        print("Error: config.json not found. Please create a config file.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error: Unable to parse config.json. {str(e)}")
        return None
    except Exception as e:
        print(f"Error: An unexpected error occurred while loading the config file. {str(e)}")
        return None

def generate_random_sequence():
    return ''.join(random.choices(string.digits, k=5))

def create_backup(directory, backup_directory):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    backup_directory = os.path.join(backup_directory, f"backup_{timestamp}")
    os.makedirs(backup_directory, exist_ok=True)
    
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            shutil.copy(file_path, os.path.join(backup_directory, filename))

def rename_files(directory, blacklist, whitelist, create_backup=False):
    if create_backup:
        create_backup(directory, directory)
    
    log_directory = os.path.join(directory, "log")
    os.makedirs(log_directory, exist_ok=True)
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

def main():
    config = load_config()
    if config is None:
        return

    blacklist = config.get("blacklist", {})
    whitelist = config.get("whitelist", {})
    IsFolderPath = config.get("IsFolderPath", True)
    create_backup_flag = config.get("create_backup", False)  # New config option for creating backups
    
    if not IsFolderPath:
        directory = os.path.dirname(os.path.abspath(__file__))
    else:
        directory = config.get("folder_path", os.path.dirname(os.path.abspath(__file__)))

    # Check if the specified target folder exists
    if not os.path.exists(directory):
        print(f"Error: Target folder '{directory}' does not exist.")
        return

    while True:
        print("(1) Start Renaming")
        print("(2) Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            rename_files(directory, blacklist, whitelist, create_backup_flag)  # Pass create_backup_flag
        elif choice == "2":
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
